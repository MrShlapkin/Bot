from telegram import LabeledPrice, Update
from telegram.error import Forbidden
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    PreCheckoutQueryHandler,
    filters,
)

# 1. Константы и настройки
TOKEN = "8911190058:AAEgylsDOOuIvy6DYwPRNnMMOGh5IMNFE0w"
STICKER_ID = (
    "CAACAgIAAxkBAAMrasUnMQRgzW6JkIqeEdoVrV0JfJwAAiJvAAJQo2FIY6s-OzOLTPU9BA"
)
ADMIN_ID = 6758746687  # Ваш Telegram ID

stars_balance = 0  # Общий накопленный баланс

# Состояние разговорного хэндлера для ввода суммы
WAITING_FOR_AMOUNT = 1

# Хранилище последних транзакций пользователей: {user_id: (charge_id, amount)}
user_transactions = {}


# Вспомогательная функция для безопасной отправки сообщений админу
async def notify_admin(context: ContextTypes.DEFAULT_TYPE, text: str):
    try:
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=text,
            parse_mode="Markdown",
        )
    except Forbidden:
        print(f"[ОШИБКА] Админ еще не нажал /start в боте!")
    except Exception as e:
        print(f"Ошибка при отправке уведомления админу: {e}")


# 2. Обработчики базовых команд
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет, зетник! Чтобы зигануть введи /z\n"
        "Для доната на СВО введи /donate\n"
        "Для возврата доната введи /refund"
    )


async def z_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_sticker(STICKER_ID)


# 3. Логика пошагового ввода суммы доната
async def donate_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Шаг 1: Запрашиваем у пользователя сумму."""
    await update.message.reply_text(
        "Сколько звёзд вы хотите задонатить на СВО?"
    )
    return WAITING_FOR_AMOUNT


async def receive_donation_amount(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    """Шаг 2: Проверяем введённую сумму и отправляем счёт."""
    user_text = update.message.text.strip()

    if not user_text.isdigit() or int(user_text) <= 0:
        await update.message.reply_text(
            "Ебень, введи натуральное число:"
        )
        return WAITING_FOR_AMOUNT

    amount = int(user_text)
    chat_id = update.message.chat_id
    prices = [LabeledPrice("Задонатить на СВО", amount)]

    await context.bot.send_invoice(
        chat_id=chat_id,
        title="Донат на СВО",
        description=f"Добровольное пожертвование: {amount} звёздочек",
        payload=f"donate_{amount}_stars",
        currency="XTR",  # Код валюты Telegram Stars
        prices=prices,
        provider_token="",  # Для Stars оставляем пустым
    )

    return ConversationHandler.END


async def cancel_donate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Донат отменён.")
    return ConversationHandler.END


# 4. Логика возврата звёзд (Refund)
async def refund_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда для пользователя: вернуть свой последний донат."""
    global stars_balance
    user = update.effective_user
    user_id = user.id

    if user_id not in user_transactions:
        await update.message.reply_text("Хаха, нехуй тебе возвращать.")
        return

    charge_id, amount = user_transactions[user_id]

    try:
        # Возврат средств через Telegram API
        await context.bot.refund_star_payment(
            user_id=user_id, telegram_payment_charge_id=charge_id
        )

        stars_balance = max(0, stars_balance - amount)
        del user_transactions[user_id]

        await update.message.reply_text(
            f"✅ Успешно! Твоя мать умрёт завтра, нищеброд."
        )

        # Уведомляем админа о возврате
        user_mention = f"@{user.username}" if user.username else f"ID {user_id}"
        await notify_admin(
            context,
            f"🤡 Ебень под ником {user_mention} вернул {amount} звёзд себе. Из-за него осталось только {stars_balance}."
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Ошибка при возврате звёзд: {e}")


# 5. Обработчики оплаты
async def precheckout_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    query = update.pre_checkout_query
    await query.answer(ok=True)


async def successful_payment_callback(
    update: Update, context: ContextTypes.DEFAULT_TYPE
):
    global stars_balance

    payment = update.message.successful_payment
    amount = payment.total_amount  # Количество полученных звёзд
    user = update.effective_user
    user_id = user.id
    charge_id = payment.telegram_payment_charge_id  # ID транзакции для возврата

    # Сохраняем платёж в словарь
    user_transactions[user_id] = (charge_id, amount)

    # Накапливаем баланс
    stars_balance += amount

    await update.message.reply_text(
        f"✅Спасибо за поддержку СВО! Списано {amount} звёзд.\n"
        f"Благодаря тебе накоплено уже: {stars_balance} звёзд."
    )

    # Уведомляем админа о донате
    user_mention = f"@{user.username}" if user.username else f"ID {user_id}"
    await notify_admin(
        context,
        f"💰 Кормилец с ником {user_mention} жёстко саппортит, скинул целых {amount} звёзд. Теперь на СВО пойдёт {stars_balance} звёздочек!",
    )


# 6. Запуск бота
def main():
    app = Application.builder().token(TOKEN).build()

    # Диалоговый обработчик для команды /donate
    donate_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("donate", donate_start)],
        states={
            WAITING_FOR_AMOUNT: [
                MessageHandler(
                    filters.TEXT & ~filters.COMMAND, receive_donation_amount
                )
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel_donate)],
    )

    # Регистрация команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("z", z_command))
    app.add_handler(CommandHandler("refund", refund_command))
    app.add_handler(donate_conv_handler)

    # Регистрация обработчиков оплаты
    app.add_handler(PreCheckoutQueryHandler(precheckout_callback))
    app.add_handler(
        MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_callback)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
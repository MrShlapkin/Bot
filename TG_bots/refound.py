import asyncio
from telegram import Bot

# Настройки
TOKEN = "8911190058:AAEgylsDOOuIvy6DYwPRNnMMOGh5IMNFE0w"
USER_ID = 6012723041  # Telegram ID пользователя, которому возвращаем звёзды
CHARGE_ID = "stxww-BL1iMA8Ifny4XDgeGiR2GsiqRwIvNWT6JPgg0LbmETP0zKtwv653zZ78E15ntiNbmI1bOi_TM_Ex0krhj0VYO676RbnKlxBq58epaPrY"  # Вставьте сюда ID операции


async def main():
    bot = Bot(token=TOKEN)
    try:
        # Вызов API-метода возврата
        await bot.refund_star_payment(
            user_id=USER_ID, telegram_payment_charge_id=CHARGE_ID
        )
        print("✅ Звёзды успешно возвращены пользователю!")
    except Exception as e:
        print(f"❌ Ошибка при возврате: {e}")


if __name__ == "__main__":
    asyncio.run(main())
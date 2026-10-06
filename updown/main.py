import random
comp_number = random.randint(1,100)
print("Я загадал число от 1 до 100, попробуй отгадать")
is_guessed=False
while is_guessed == False:
    user_number=int(input("Введи своё число от 1 до 100: "))
    if user_number>comp_number:
        print("Бери меньше")
    elif user_number<comp_number:
        print("Бери больше")
    else:
        is_guessed=True
        print("Ты угадал")       

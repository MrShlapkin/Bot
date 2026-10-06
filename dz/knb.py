import random
print("Привет, как я могу к вам обращаться?")
player_name=input()
wins=0
draws=0
loses=0
while 1==1:
    print(f"Не хотите сыграть, {player_name}?")
    answer=input()
    while answer!="да" and answer!="хочу" and answer!="нет" and answer!="не хочу":
        if answer!="да" and answer!="хочу" and answer!="нет" and answer!="не хочу":
            print("Не могли бы вы ответить точнее?")
            answer=input()
    if answer=="да" or answer=="хочу":
        print("Ознакомтесь с правилами:")
        print("1 - камень")
        print("2 - ножницы")
        print("3 - бумага")
        print(f"Камень тупит ножницы, ножницы режут бумагу, бумага накрывает камень. Ваша задача - не остаться в дураках, удачи {player_name}.")
        rounds=int(input("Сколько раундов хотите сыграть?   "))
        repeat=0
        while rounds<=0 and repeat<3:
            rounds=int(input("Введите нормальное число раундов:   "))
            repeat+=1
        while rounds<=0:
            rounds=int(input("Да введи нормально, дегенерат!   "))
        for i in range(rounds):
            print("Время сделать выбор:")
            a="Ваш выбор -"
            player_number=int(input())
            while 1>player_number or player_number>3:
                print("Такой предмет ещё не добавили, сделайте выбор ещё раз:")
                player_number=int(input())
            if player_number==1:
                a+=" камень"
            elif player_number==2:
                a+=" ножницы"
            elif player_number==3:
                a+=" бумага"
            computer_number=random.randint(1,3)
            a+=", мой выбор -"
            if computer_number==1:
                a+=" камень"
            elif computer_number==2:
                a+=" ножницы"
            elif computer_number==3:
                a+=" бумага"
            print(a)
            if player_number==computer_number:
                result="Ничья"
                draws+=1
            elif player_number-computer_number==-1 or player_number-computer_number==2:
                result="Победа"
                wins+=1
            else:
                result="Поражение"
                loses+=1
            print(result)         
            print(f"Победы - {wins}   Поражения - {loses}   Ничьи - {draws}")
    elif answer=="нет" or answer=="не хочу":
        print("Жаль, приходите как только будет желание")
        break
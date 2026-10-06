symbol = input("введите любой символ с клавиатуры: ")
import sys
if len(symbol)==1:
    if symbol >= "a" and symbol <= "z" or symbol >= "A" and symbol <= "Z":
        print("это английская буква")
        if symbol >= "a" and symbol <= "z":
            print("маленькая")
        else:
            print("большая")

    elif symbol >= "0" and symbol <= "9":
        print("это цифра")
        if ord(symbol) % 2 == 0:
            print("чётная")
        else:
            print("нечётная")

    else:
        print("это неизвестный символ")
else:
            
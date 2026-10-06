floor=int(input("Введите количество этажей: "))
steps_in_floor=int(input("Введите количество ступенек в пролёте: "))
SEC_IN_STEPS=10
STAIRS_IN_FLOOR=2
steps=floor*steps_in_floor*STAIRS_IN_FLOOR
time=steps*SEC_IN_STEPS
mins=time//60
secs=time%60
print(f"Ваша жизнь увеличится на {mins} минут и {secs} секунд")
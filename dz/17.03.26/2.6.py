secs = int(input("Введите количество секунд:"))
hours=secs//3600
mins=secs%3600//60
secs=secs%3600%60
print(f"Прошло {hours} часов, {mins} минут и {secs} секунд")
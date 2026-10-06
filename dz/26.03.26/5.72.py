path=10
week_path=10
percent=10
i=2
while i<=10:
    path+=path*percent/100
    if i<=7:
        week_path+=path
    print(f"пробег за {i} день - {path} километров")
    i+=1
print(f"за первые 7 дней лыжник пробежал {week_path} километров")
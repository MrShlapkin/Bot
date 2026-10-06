import random

count_workers = int(input("введите кол-во ваших сотрудников:  "))

salaries = []


for _ in range(count_workers):
    salaries.append(random.randint(50000, 150000))

for i in range(count_workers):
    print(f"Сотрудник №{i+1} зп - {salaries[i]} руб.")

for i in range(count_workers):
    if slaries[i]>100000:
        print
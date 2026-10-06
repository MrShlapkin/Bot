import random
current_mark=0
total_count_5=0 
current_mark_3=0

for i in range(1,19):
    print(f"ученик №{i:3d} ", end="")
    current_mark_3=0
    for j in range(1,4):
        current_mark=random.randint(2,5)
        if current_mark==3:
            current_mark_3+=1      

        print(f"{current_mark:3d}", end="")
        if current_mark==5:
            total_count_5+=1
    print(f"    количество троек у текущего ученика {current_mark_3}", end="")        
    print()
print()            
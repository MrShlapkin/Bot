arr2d = []
rows_count = 5
cols_count = 5

for i in range(rows_count):
    arr2d.append([])
    for j in range(cols_count):
        if (i==rows_count//2 or j==cols_count//2) or (i<=rows_count//2 and j==0) or (i==0 and j>=cols_count//2)  or (i==rows_count-1 and j<=cols_count//2) or (i>=rows_count//2 and j==cols_count-1):
            arr2d[i].append(1)
        else:
            arr2d[i].append(0)   

for i in range(rows_count):
    for j in range(cols_count):
        print(f"{arr2d[i][j]} ", end="")
    print()

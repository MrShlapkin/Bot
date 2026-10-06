x, y, z, w = map(int, input().split())
count = 0
for i in range(w // x + 1):
    for m in range(w // y + 1):
        current_weight = i * x + m * y 
        if current_weight > w:
            break
        remaining = w - current_weight 
        if remaining % z == 0:
            count += 1
print(f"{count}")          
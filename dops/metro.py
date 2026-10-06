n, i, j = map(int, input().split())

dist_positive = 0
dist_negative = 0

if j > i:
    dist_positive = j - i - 1
    dist_negative = i + (n - j) - 1
elif i > j:
    dist_positive = (n - i) + j + -1
    dist_negative = i - j - 1

min_dist = 0

if dist_positive < dist_negative:
    min_dist = dist_positive
else:
    min_dist = dist_negative

print(min_dist)  
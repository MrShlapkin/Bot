import random

arr=[]
arr_count=100
for _ in range(arr_count):
    arr.append(random.randint(1,10))
print(arr)

print(f"min = {min(arr)}")    
print(f"max = {max(arr)}")
print(f"sum = {sum(arr)}")
print(f"avg = {sum(arr)/len(arr)}")
arr.reverse()
print(f"index_5 = {len(arr)-arr.index(5)-1}")
arr.reverse()

is_exist = False
index_exist = -1
find_elem = 5

for i in range(len(arr)):
    if arr[i] == find_elem:
        index_exist=i
        is_exist=True
        break  

for i in range(len(arr),):
    if arr[i] == find_elem:
        index_exist=i
        is_exist=True
        break 
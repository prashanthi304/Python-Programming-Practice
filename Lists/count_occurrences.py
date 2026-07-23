numbers = [10, 20, 30, 20, 40, 20]
key = int(input())
count = 0
for num in numbers:
  if num == key:
    count += 1
print(key,"appears",count,"times")
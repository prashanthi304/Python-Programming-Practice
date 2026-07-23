numbers = [10, 20, 30, 20, 40, 20]
target = 20
filtered_list = []
for num in numbers:
  if num != target:
    filtered_list.append(num)
print(filtered_list)
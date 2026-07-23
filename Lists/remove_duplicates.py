numbers = [10, 20, 10, 30, 20, 40]
unique_list = []
for num in numbers:
  for index in range(len(unique_list)):
    if num == unique_list[index]:
      break
  else:
    unique_list.append(num)
print(unique_list)
numbers = [10, 20, 10, 30, 20, 10]
unique_list = []
count = 0
for num in numbers:
  for index in range(len(unique_list)):
    if num == unique_list[index]:
      break
  else:
    unique_list.append(num)
print(unique_list)
for num in unique_list:
  for index in range(len(numbers)):
    if num == numbers[index]:
      count += 1
  print(num,'=',count)
  count = 0
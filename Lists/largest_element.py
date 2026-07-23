numbers = [78, 85, 92, 66, 88]
largest = numbers[0]
for index in range(1,len(numbers)):
  if numbers[index] > largest:
    largest = numbers[index]
print(largest)
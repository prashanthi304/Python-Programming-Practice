numbers = [78, 85, 92, 66, 88]
largest = numbers[0]
second_largest = numbers[0]
for num in numbers:
  if num > largest:
    second_largest = largest
    largest = num
  else:
    if num < largest and num > second_largest:
      second_largest = num
print(second_largest)

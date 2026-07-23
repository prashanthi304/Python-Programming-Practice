numbers = [78, 85, 92, 66, 88]
smallest = numbers[0]
second_smallest = numbers[0]
for num in numbers:
  if num < smallest:
    second_smallest = smallest
    smallest = num
  else:
    if num > smallest and num < second_smallest:
      second_smallest = num

print(smallest,second_smallest)
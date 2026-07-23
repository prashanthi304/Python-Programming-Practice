numbers = [1, 2, 3, 4, 5]
minimum = numbers[0]
maximum = numbers[0]
for num in numbers:
  if num < minimum:
    minimum = num
  elif num > maximum:
    maximum = num
print("MIN =",minimum)
print("MAX =",maximum) 
numbers = [78, 85, 92, 66, 88]
target = int(input())
found = False
for index in range(len(numbers)):
  if numbers[index] == target:
    found = True
    break
if found:
  print("Found at index",index)
else:
  print("NOT FOUND")


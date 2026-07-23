list1 = [10, 20, 30, 40]
list2 = [20, 40, 50, 60]
common_elements = []
for num in list1:
  for item in list2:
    if num == item:
      common_elements.append(num)
print(common_elements)
numbers = [1, 2, 3, 4, 5, 2,1]
new_numbers = [7, 8, 9, 10]
numbers.append(6)
print(numbers)
numbers.insert(0,0)
print(numbers)
numbers.pop(3)
print(numbers)
numbers.remove(1)
print(numbers)
numbers.extend(new_numbers)
print(numbers)
numbers = [1, 2, 3, 2, 1]
reversed_list = []
for index in range(len(numbers) - 1,-1,-1):
  reversed_list.append(numbers[index])
if numbers == reversed_list:
  print("palindrome")
else:
  print("not palindrome")






new_list = [1, 2, 3]
result = new_list[0]
print(result)

# in operator to find item in a list
if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)
    break

  # inserting element
numbers = []
numbers.append(2)
numbers.append(200)
numbers.extend([3, 4, 5, 6, 7, 8])
print(numbers)

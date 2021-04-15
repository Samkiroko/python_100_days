# color = ["red", "blue", "green"]
# print(color[0])

# Assignment make the two variables point to the list in memory
# b = color  # Does not copy the list
#  Empty list is just pair of brackets []. The "+" works to append two lists, so
# [1,2]+ [3,4] yields[1,2,3,4] same as strings.

# squares = [1, 4, 9, 16]
# sum = 0
# for num in squares:
#     sum += num
# print(sum)  # 30

#  checking value is in a collection

# if "reds" in color:
#     print("yes")
# else:
# print("No")

#  for/in constructs are very commonly used in python code and work on data other than list
#  Anytime you need to iterating over a collection use for/in

#########_RANGE_########
#  The range(n) function yields the numbers 0,1,...n-1, and range(a,b) returns a, a+1, ...b-1 up
#  to but not including the last number.
#  Combination of for-loop and range() function allow you to build a traditional numberic loop

# Print the number from 0 through 99
# for i in range(100):
#     print(i)

######_while loop_########

#  Access every 3rd element in a list
# Access every 3rd element in a list
# i = 0
# while i < len(a):
#   print (a[i])
#   i = i + 3

#######_LIST METHODS_########
# _list.append(elem)_## -- adds a single element to the end of the list. Common error:
#  does not return the new list, just modifies the original.
#  list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
# list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
# list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
# list.remove(elem) -- searches for the first instance of the given element and removes it (throws
# ValueError if not present)
# list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
# list.reverse() -- reverses the list in place (does not return it)
# list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).

# list = ['larry', 'curly', 'moe']
# list.append('shemp')  # append elem at end
# list.insert(0, 'xxx')  # insert elem at index 0
# list.extend(['yyy', 'zzz'])  # add list of elems at end
# print(list)  # ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
# print(list.index('curly'))  # 2

# list.remove('curly')  # search and remove that element
# list.pop(1)  # removes and returns 'larry'
# print(list)  # ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

# #  note the the above methods do not "return" they just modify the original list

# ######_List Build up_########
# #  common pattern is to start a list with an empty list [], then use append()
# # or extend() to add elements to it:

# lists = []  # Start as the empty lists
# lists.append('a')  # Use append() to add elements
# lists.append('b')
# print(lists)

# ######_list Slices_#######
# # Slices work on list as with strings, and can also be used to change sub-parts of the list.
# list1 = ['a', 'b', 'c', 'd']
# print(list1[-1])
# print(list1[1:-1])  # ['b', 'c']
# list1[0:2] = 'z'  # replace ['a', 'b'] with ['z']
# print(list1)  # ['z', 'c', 'd']


# check_letter = guess_letter in random_word
# print(check_letter)

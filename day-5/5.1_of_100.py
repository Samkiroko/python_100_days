# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇
# #  Highest score without using max or min
# max_score = student_scores[0]
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(f"The highest score in the class is: {max_score}")

# if i was to add all the number from 1 to 100 using loop

# total = 0
# # note it does not include the last number in this case it will count till 100.
# for number in range(1, 101):
#     total += number
# print(total)

#  Challenge: and the sum of all the evens in the range of 1,100

# total_even = 0
# for even in range(1, 101):
#     if even % 2 == 0:
#         total_even += even
# print(total_even)

#  fizz buzz challenge
#  if num % 3 =0 (fizz)
# if num % 5 = ) (Buzz)
# if num % both (fizzBuzz)

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

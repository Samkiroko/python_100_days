# for loop

# fruits = ["Apple", "peas", "potatoes"]

# for fruit in fruits:
#     print(fruit + " pizza")
#     print(f"{fruit}   pizza")
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

counter = 0
total = 0

for height in student_heights:
    counter += 1
    total += height

average_height = round(total/counter)

print(average_height)


# Write your code below this row 👇

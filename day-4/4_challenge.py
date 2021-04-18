import random


print("Who is paying the bill")

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_of_person = len(names)

random_person_number = random.randint(0, number_of_person - 1)

paying_bill = names[random_person_number]

print(paying_bill + "is going to buy the meal today")

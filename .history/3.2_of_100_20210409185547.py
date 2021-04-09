# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


name1_lower = name1.lower()
name2_lower = name2.lower()

name_lower = name1_lower + name2_lower

t = name1_lower.count("t")
r = name1_lower.count("r")
u = name1_lower.count("u")
e = name1_lower.count("e")

print(t+r+u+e)

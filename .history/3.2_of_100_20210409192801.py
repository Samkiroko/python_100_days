# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


name1_lower = name1.lower()
name2_lower = name2.lower()

name_lower = name1_lower + name2_lower

t = name_lower.count("t")
r = name_lower.count("r")
u = name_lower.count("u")
e = name_lower.count("e")

true_count = str(t+r+u+e)

l = name_lower.count("l")
o = name_lower.count("o")
v = name_lower.count("v")
e = name_lower.count("e")

love_count = str(l+o+v+e)

true_love_score = true_count + love_count

print(true_love_score)

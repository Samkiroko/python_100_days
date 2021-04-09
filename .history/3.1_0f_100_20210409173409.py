
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
    print(f"you final bill is: ${bill}")
elif size == "M":
    bill = 20
    print(f"your final bill is: ${bill}")
elif size == "L":
    bill = 25
    print(f"your final bill is ${bill}")
else:
    print("Please choose the pizza size")
if (add_pepperoni == "Y") & (size == "S"):
    bill += 2
    print(f"your final bill is: ${bill}")
else:
    bill += 3
    print(f"Your final bill: ${bill}")
if extra_cheese == "Y":
    bill += 3
    print(f"Your final bill: ${bill}")

def greet():
    print("Hope well")
    print("Did you finish the assignment")
    print("Advice")


greet()

# function with input


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do  {name}")


greet_with_name("Joyce Wanjiku")

#  name => paramenter
#  "Joyce wanjiku" => Argument

# function with more than 1 input


def greet_with(name, phone):
    print(f"What your name? {name}")
    print(f"What your phone number? {phone}")


# positional arguments
greet_with("Kiroko", +254713356169)

# keyword arguments
greet_with(name="Kiroko", phone=+254713356169)

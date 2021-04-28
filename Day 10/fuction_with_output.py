#  function with output

first = input("what your first name?\n")
last = input("What your last name?\n")


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid input"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name(first, last)
print(formated_string)

# more that one return statement

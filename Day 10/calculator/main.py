from art import logo


# Calculator

# Add


def add(n1, n2):
    return n1 + n2
# subtract


def subtract(n1, n2):
    return n1 - n2
# Multiply


def Multiply(n1, n2):
    return n1*n2
# Divide


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": Multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: \n"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above:")
        num2 = float(input("What's the next number?: \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} ={answer}")
        continue_input = (input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")).lower()

        if continue_input == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

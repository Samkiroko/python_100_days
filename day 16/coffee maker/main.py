from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

print(coffee_maker.report())
print(money_machine.report())

while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        is_sufficient = coffee_maker.is_resource_sufficient(drink)
        is_enough_money = money_machine.make_payment(drink.cost)
        if is_sufficient and is_enough_money:
            coffee_maker.make_coffee(drink)

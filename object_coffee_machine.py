from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machineOn = True;
this_menu = Menu()
this_coffee_maker = CoffeeMaker()
drink_list = this_menu.get_items()
this_money_machine = MoneyMachine()

while machineOn:
    order = input("What would you like?" + " " + drink_list + " ").lower()
    if order == "off":
        machineOn = False
    elif order == "report":
        print(this_coffee_maker.report())
    else:
        drink_order = this_menu.find_drink(order)
        if this_coffee_maker.is_resource_sufficient(drink_order):
            is_cost_sufficient = this_money_machine.make_payment(drink_order.cost)
            if is_cost_sufficient:
                this_coffee_maker.make_coffee(drink_order)

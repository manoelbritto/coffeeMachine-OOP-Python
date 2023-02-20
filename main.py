from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

name_menu = True
while name_menu:
    # Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
    client_option = input('What would you like? (espresso/latte/cappuccino/: ').lower()
    # Print report
    if client_option == 'report':
        coffee_maker.report()
    # Turn off the Coffee Machine by entering “off” to the prompt
    elif client_option == 'off':
        print("Turn off the machine - Bye")
        break
    elif menu.find_drink(client_option) is not None:
        name_menu = False

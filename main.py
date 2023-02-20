from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# instantiate objects
menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()


# function to play the whole program
def machine():
    machine_work = True
    while machine_work:
        name_menu = True
        while name_menu:
            # Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”
            client_option = input(f'(What would you like? {menu.get_items()}: ').lower()
            # Print report
            if client_option == 'report':
                coffee_maker.report()
                money.report()
            # Turn off the Coffee Machine by entering “off” to the prompt
            elif client_option == 'off':
                print("Turn off the machine - Bye")
                break
            elif menu.find_drink(client_option) is not None:
                name_menu = False
        if client_option == 'off':
            break
        # get the ingredients
        ingredients = menu.find_drink(client_option)

        check_coffe = coffee_maker.is_resource_sufficient(ingredients)
        if check_coffe:
            # process coin
            print(f"Price is {ingredients.cost}")
            process = money.make_payment(ingredients.cost)
            if process:
                coffee_maker.make_coffee(ingredients)


# start machine
machine()

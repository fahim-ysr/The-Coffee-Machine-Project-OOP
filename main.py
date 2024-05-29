from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

running = True

m = Menu()
machine = CoffeeMaker()
money = MoneyMachine()

while running:

    print("Items Available:")
    for items in m.menu:
        print(items.name +   ": $" + str(items.cost))

    # TODO: 1. Prompt for user's input
    choice = input("What would you like? (" + m.get_items() + "): ")

    # TODO: 3. Print report
    if choice == "report":
        machine.report()
        money.report()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
    elif choice == "off":
        running = False

    else:
        drink = m.find_drink(choice)
        if drink == "cappuccino" or "latte" or "espresso":

            # TODO: 4. Check resources sufficient?
            sufficient = machine.is_resource_sufficient(drink)

            if sufficient == True:

                # TODO: 5. Process coins
                payment_successful = money.make_payment(drink.cost)

                # TODO: 6. Check transaction successful?
                if payment_successful == True:

                    # TODO: 7. Make Coffee (update ingredients)...
                    machine.make_coffee(drink)

        else:
            print("Input Error.")
            running = False
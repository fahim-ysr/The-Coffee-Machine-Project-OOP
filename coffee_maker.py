"""

This class represents a coffee maker machine that manages resources and makes coffee for the coffee machine program.

Attributes:
- resources (dict): A dictionary containing the available resources for making coffee.

Methods:
- __init__(): Initializes a new CoffeeMaker object with default resource values.
- report(): Prints a report of all available resources.
- is_resource_sufficient(drink): Checks if there are sufficient resources to make the given drink.
- make_coffee(order): Deducts the required ingredients from the resources to make the given drink.

"""

class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

MENU = {
    "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 50},
    "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 80},
    "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 100}
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
    "money": 0
}

def report():
    print(f"Water = {resources['water']}ml")
    print(f"Milk = {resources['milk']}ml")
    print(f"Coffee = {resources['coffee']}g")
    print(f"Money = Rs. {resources['money']}")

def is_resource_sufficient(order_ingredients):
    """Checks if enough resources are there to make the drink"""
    for item in ("water", "milk", "coffee"):
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Takes coin input and returns total amount"""
    print("Please insert coins")
    total = 0
    total += int(input("How many 5Rs. coins: ")) * 5
    total += int(input("How many 10Rs. coins: ")) * 10
    total += int(input("How many 20Rs. coins: ")) * 20
    return total

def make_coffee(drink_name, order_ingredients):
    """Deducts the ingredients from resources and serves coffee"""
    for item in ("water", "milk", "coffee"):
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")

# ------------------------------
# Start of the coffee machine loop
# ------------------------------
is_on = True

while is_on:
    choice = input("What would you like to have? (latte/espresso/cappuccino): ").lower()
    if choice == "off":
        is_on = False
        print("Coffee Machine is turned off.")
    elif choice == "report":
        report()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink):
            payment = process_coins()
            if payment < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = payment - drink["cost"]
                if change > 0:
                    print(f"Here is your Rs{change} in change.")
                resources["money"] += drink["cost"]
                make_coffee(choice, drink)
    else:
        print("Invalid input. Please try again.")

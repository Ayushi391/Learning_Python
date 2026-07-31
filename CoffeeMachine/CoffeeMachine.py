#Coffee Machine ☕🐍
from main import MENU, resources
#money
money=0

def print_report():
    """return report"""
    print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}ml\nMoney: ${money}")

def check_resources(user_input):
    "returns true if enough resources otherwise false."
    for resource,value in MENU[user_input]["ingredients"].items():
        if resources[resource]<value:
            print(f"Sorry there is not enough {resource}")
            return False
    return True

def process_coins(user_input):
    "returns true if enough coins provided otherwise false."
    drink_cost=MENU[user_input]["cost"]
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = round(0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies,2)
    print(total)
    if total>drink_cost:
        change = total-drink_cost
        print(f"Here is your ${change:.2f} change")
        return True
    elif total==drink_cost:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
        
    
should_continue=True
while should_continue:
    user_input=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input=="off":
        should_continue=False
    elif user_input=="report":
        print_report()
    elif user_input in ("espresso", "latte", "cappuccino"):
        if check_resources(user_input):
            #proceed to coin
            if process_coins(user_input):
                money+=MENU[user_input]["cost"]
                for resource,value in MENU[user_input]["ingredients"].items():
                    resources[resource]-=value
                #make coffee
                print(f"Here is your {user_input}☕ Enjoy!")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = input("What toppings do you want? (comma-separated): ").split(',')

for requested_topping in requested_toppings:
    topping = requested_topping.strip()
    if topping in available_toppings:
        print(f"Adding {topping}.")
    else:
        print(f"Sorry, we don't have {topping}.")

print("\nFinished making your pizza!")

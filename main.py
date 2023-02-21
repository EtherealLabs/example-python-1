FOOD_PRICES = {
    'Bread': 2.50,
    'Sliced turkey': 5.50,
    'Sliced cheese': 4.50,
    'Spaghetti noodles': 2.00,
    'Tomato sauce': 3.50,
    'Spices': 4.50,
    'Milk': 3.00,
    'Eggs': 2.50
}

FOOD_LIST = list(FOOD_PRICES.keys())


def create_menu_item(idx, name):
    return f'{idx+1}. {name}'


def create_menu():
    menu_options = [create_menu_item(idx, f'{name} - ${FOOD_PRICES[name]}') for (idx, name) in enumerate(FOOD_LIST)]
    menu_options.append(create_menu_item(len(menu_options), 'Done shopping'))
    return menu_options


def output_choice(name, cost):
    return f'You added {name} to your basket. This will cost ${cost}.'


if __name__ == '__main__':
    print("Welcome to the grocery store. Please fill your basket with items.")

    menu = create_menu()

    running_total = 0

    while True:
        print("Select the numeric option to add an item to your bag.")
        for item in menu:
            print(item)

        choice = input("Enter your choice: ")
        try:
            choice_idx = int(choice) - 1
        except:
            print("Error reading your choice. Please try again.")
            continue

        if choice_idx == len(menu) - 1:
            break

        if choice_idx < 0 or choice_idx >= len(FOOD_LIST):
            print("Error with the selected choice. Please choose from the list.")

        choice_name = FOOD_LIST[choice_idx]
        choice_value = FOOD_PRICES[choice_name]
        quantity = input("Enter your quantity: ")

        try:
            quantity_int = int(quantity)
        except:
            print("Error reading your quantity. Please try again.")
            continue

        if quantity_int <= 0:
            print("You must place at least one of that item in the basket.")
            continue

        quantity_cost = quantity_int * choice_value
        print(output_choice(choice_name, quantity_cost))

        running_total += quantity_cost

    print(f"Thanks for shopping. You spent ${running_total}")

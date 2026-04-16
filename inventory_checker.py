def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    inventory_level = get_valid_integer("Enter the current inventory level: ")
    reorder_threshold = get_valid_integer("Enter the minimum reorder threshold: ")

    if inventory_level < reorder_threshold:
        print("Reorder alert: Inventory is below the minimum reorder threshold.")
    else:
        print("Inventory level is sufficient.")

    try:
        inventory_percentage = (inventory_level / reorder_threshold) * 100
        print(f"Inventory is {inventory_percentage:.2f}% of the reorder threshold.")
    except ZeroDivisionError:
        print("Cannot calculate percentage because the reorder threshold is zero.")


if __name__ == "__main__":
    main()
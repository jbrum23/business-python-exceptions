def get_valid_number(prompt, number_type):
    """
    Repeatedly ask the user for input until a valid non-negative number is entered.
    """
    while True:
        try:
            value = number_type(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    units_sold = get_valid_number("Enter the number of units sold: ", int)
    price_per_unit = get_valid_number("Enter the price per unit: ", float)

    total_revenue = units_sold * price_per_unit
    print(f"Total revenue: ${total_revenue:.2f}")


if __name__ == "__main__":
    main()
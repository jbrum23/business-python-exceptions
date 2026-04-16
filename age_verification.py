def get_customer_age():
    while True:
        try:
            age = int(input("Enter the customer's age: "))
            if age <= 0:
                print("Invalid input. Please enter a positive integer.")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    age = get_customer_age()

    try:
        if age >= minimum_age:
            print("The customer is eligible for the promotion.")
        else:
            print("The customer is not eligible for the promotion.")
    except NameError:
        minimum_age = 18
        if age >= minimum_age:
            print("The customer is eligible for the promotion.")
        else:
            print("The customer is not eligible for the promotion.")


if __name__ == "__main__":
    main()
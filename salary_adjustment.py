def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    current_salary = get_valid_float("Enter the employee's current salary: ")

    while True:
        adjustment_percentage = get_valid_float("Enter the adjustment percentage: ")

        if adjustment_percentage < 0:
            print("Adjustment percentage cannot be negative.")
        elif adjustment_percentage > 100:
            print("Adjustment percentage must be between 0 and 100.")
        else:
            break

    new_salary = current_salary + (current_salary * adjustment_percentage / 100)
    print(f"New salary: ${new_salary:.2f}")


if __name__ == "__main__":
    main()
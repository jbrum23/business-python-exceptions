def main():
    while True:
        try:
            profit = float(input("Enter the profit: "))
            revenue = float(input("Enter the revenue: "))

            profit_margin = (profit / revenue) * 100

        except ValueError:
            pass
        except ZeroDivisionError:
            print("Revenue cannot be zero.")
        else:
            print(f"Profit margin ratio: {profit_margin:.2f}%")
            break


if __name__ == "__main__":
    main()
# Exercise 1
## Overview
This project contains a Python program for Exercise 1 of the DATA 4000 Python with AI assignment. The program simulates entering sales data for a retail business by asking the user for the number of units sold and the price per unit. It validates the input, reprompts the user when invalid values are entered, and then calculates the total revenue.
## Purpose
The purpose of this exercise is to practice:
- user input
- data type conversion
- functions
- loops
- exception handling with `ValueError`
- basic arithmetic operations
## Program Description
The program prompts the user to enter:
- the number of units sold as an integer
- the price per unit as a float
A helper function named `get_valid_number()` is used to validate input. If the user enters an invalid value, the program displays an error message and asks again until a valid number is entered. Once both values are valid, the program calculates total revenue using the formula:
`total revenue = units sold × price per unit`

# Exercise 2
## Overview
This project contains a Python program for Exercise 2 of the DATA 4000 Python with AI assignment. The program simulates an inventory management task by asking the user for the current inventory level and the minimum reorder threshold. It validates the input, reprompts the user when invalid values are entered, checks whether inventory is below the threshold, and calculates the inventory percentage relative to the threshold.
## Purpose
The purpose of this exercise is to practice:
- user input
- data type conversion
- functions
- loops
- exception handling with `ValueError`
- exception handling with `ZeroDivisionError`
- conditional statements
- basic arithmetic operations
## Program Description
The program prompts the user to enter:
- the current inventory level as an integer
- the minimum reorder threshold as an integer
A helper function named `get_valid_integer()` is used to validate input. If the user enters an invalid value, the program displays an error message and asks again until a valid integer is entered. After valid inputs are collected, the program checks whether the inventory level is below the reorder threshold and prints a reorder alert if needed.
The program also attempts to calculate the inventory percentage using the formula:
`inventory percentage = (inventory level / reorder threshold) × 100`
If the reorder threshold is zero, the program handles the error using `ZeroDivisionError` and prints a message instead of crashing.

# Exercise 3
## Overview
This project contains a Python program for Exercise 3 of the DATA 4000 Python with AI assignment. The program simulates a marketing team checking whether a customer is eligible for an age-restricted promotion by asking for the customer's age, validating the input, and determining eligibility based on a minimum required age.
## Purpose
The purpose of this exercise is to practice:
- user input
- data type conversion
- functions
- loops
- exception handling with `ValueError`
- exception handling with `NameError`
- conditional statements
## Program Description
The program prompts the user to enter the customer's age as an integer. A helper function named `get_customer_age()` is used to validate input. If the user enters a non-integer value, the program catches the error and asks again. If the user enters a value that is zero or negative, the program also asks again until a valid positive integer is entered.
After a valid age is entered, the program checks whether the customer is eligible for an age-restricted promotion. The program uses a minimum age of 18 to determine eligibility.
The program also demonstrates handling a `NameError` by referencing a variable before it is defined, then catching the error and assigning the correct value before continuing.

# Exercise 4
## Overview
This project contains a Python program for Exercise 4 of the DATA 4000 Python with AI assignment. The program simulates a finance tool that calculates a business's profit margin ratio by asking the user for profit and revenue values, validating the input, and displaying the result as a percentage.
## Purpose
The purpose of this exercise is to practice:
- user input
- data type conversion
- loops
- exception handling with `ValueError`
- exception handling with `ZeroDivisionError`
- try-except-else statements
- basic arithmetic operations
- defensive programming
## Program Description
The program prompts the user to enter:
- profit as a float
- revenue as a float
The program uses a `while True` loop to keep asking for input until valid values are entered. It uses a `try-except-else` structure to handle possible errors during input and calculation.
The profit margin ratio is calculated using the formula:
`profit margin ratio = (profit / revenue) × 100`
If the user enters an invalid float, the program silently reprompts using `pass` in the `ValueError` block. If the user enters zero for revenue, the program catches the `ZeroDivisionError` and displays a message instead of crashing. If no exceptions occur, the program prints the ratio as a percentage in the `else` block.

# Exercise 5
## Overview
This project contains a Python program for Exercise 5 of the DATA 4000 Python with AI assignment. The program simulates an HR salary adjustment tool by asking the user for an employee's current salary and an adjustment percentage, validating the input, and calculating the employee's new salary.
## Purpose
The purpose of this exercise is to practice:
- user input
- data type conversion
- functions
- loops
- exception handling with `ValueError`
- conditional statements
- basic arithmetic operations
- input validation
## Program Description
The program prompts the user to enter:
- the employee's current salary as a float
- the adjustment percentage as a float
A helper function is used to validate numeric input with `try-except`. The program also uses `if-else` checks to make sure the adjustment percentage is within a valid range. If the user enters a negative percentage or a percentage greater than 100, the program displays an error message and asks again until a valid value is entered.
The new salary is calculated using the formula:
`new salary = current salary + (current salary × adjustment percentage / 100)`

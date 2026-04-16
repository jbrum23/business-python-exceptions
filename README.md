# assingment-4

# Sales Data Input Validation
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

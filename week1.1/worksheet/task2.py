"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

amount = int(input("How much do you want to save each month? "))  # Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


annually_amount = amount * 12# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
print(f"you will save {annually_amount} in the end of the year")# print this out for the user with a suitable message.

interest = annually_amount * 0.008
total_of_amount = annually_amount + interest# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
print(f"you will save £{total_of_amount:.2f} in the end of the year")# print this out in the format £X.XX (to two decimal places).


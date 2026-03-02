# Ubaldo Alvarado
# 03/01/2026
# P1HW2_AlvaradoUbaldo.py
# This program calculates and displays travel expenses.

print("This program calculates and displays travel expenses")
budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
transportation = int(input("How much do you think you will spend on gas?: "))
accommodation = int(input("Approximatly, how much will you need for accomodations/hotel?: "))
food = int(input("Last, how much do you need for food?: "))

print("------Travel Expenses------")
print("Location:", destination)
print("Initial Budget:", budget)
print("Fuel:", transportation)
print("Accomodation:", accommodation)
print("Food:", food)
total_expenses = transportation + accommodation + food

print("Remaining Balance:", budget - total_expenses)
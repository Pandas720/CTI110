 # Ubaldo Alvarado
 # 03/11/2026
 # P1HW1_AlvaradoUbaldo.py
 # This program will perform basic math operations. The user will be prompted to enter the values for each operation, and the results will be displayed.

print("-----Calculating Exponents-----")
base = int(input("Enter an interger as the base value: "))
exponent = int(input("Enter an interger as the exponent: "))
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result} !!")

print("\n-----Addition and Subtraction-----")
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))
addition_result = num1 + num2
final_result = addition_result - num3
print(f"\n{num1} + {num2} - {num3} = {final_result}")
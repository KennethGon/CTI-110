# This program calculates and displays travel expenses 
# 2-16-2023
# CTI-110 P1HW2 - Travel Expense
# Kenneth Gonzalez

print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter budget: "))
print()
name = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()

print("-"*12, "Travel Expenses", 12*'-')
print("Location: ", name)
print("Initial Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)
print()
balance = budget - gas - food - hotel
#print("Remaining Balance: ", balance)
print("Remaining Balance: ", format(balance,',.0f'))







# Change displayed results 
# Date: 3-1-2023
# CTI-110 P2HW1 - Travel 
# Kenneth Gonzalez
#

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
print("Location:             ", name)
print("Initial Budget:       $",budget)
print("Fuel:                      $",gas)
print("Accomodation:     $",hotel)
print("Food:                    $",food)
print("-"*50)

balance = budget - gas - food - hotel
#print("Remaining Balance: ", balance)
print()
print("Remaining Balance: $", format(balance,',.1f'))







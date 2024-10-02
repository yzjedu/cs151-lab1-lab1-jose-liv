# Programmers: Jose and Liv
# Course: Cs151, [Zelalem Yalew]
# Due Date: 9/18/2024
# Lab Assignment: 1
# Problem Statement: This program calculates the total cost of gas for a road trip
# Data In: The program asks the user to input miles to travel, car's MPG, and the cost of gas.
# Data Out: The program outputs the total gas cost for the road trip.
# Credits: [Class Examples]

# Prompt the user for input values
miles_to_travel = int(input("Enter the number of miles you will travel: "))
car_mpg = int(input("Enter the miles per gallon (MPG) of your car: "))
gas_cost_per_gallon = float(input("Enter the cost of gas per gallon: "))

# Calculate the total number of gallons needed for the trip
gallons_needed = miles_to_travel / car_mpg

# Calculate the total cost of gas for the trip
total_gas_cost = gallons_needed * gas_cost_per_gallon

# Output the result to the user
print(f"The total cost of gas for your trip is: ${total_gas_cost:.2f}")

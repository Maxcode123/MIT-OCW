# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:53:10 2020

@author: nikif
"""

# prompt user for annual salary
annual_salary = float(input("Enter your annual salary: "))

# prompt user for portion of salary to be saved
portion_saved = float(input("Enter the percent of your salary to" \
                            " save, as a decimal: "))

# prompt user for cost of dream house
total_cost = float(input("Enter the cost of your dream home: "))

# percent of house price for down payment
portion_down_payment = 0.25

# initialize current savings
current_savings = 0

# initialize month counter
month_count = 0;

while (current_savings < portion_down_payment * total_cost):
    # add 1 to month counter
    month_count += 1
    # calculate savings from return from investment
    returns = current_savings * (4/100) / 12
    # calculate current savings
    current_savings += returns + portion_saved * annual_salary / 12    
print("Number of months: {}".format(month_count))



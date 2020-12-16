# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 16:42:33 2020

@author: nikif
"""

# semi annual raise
e = 0.07

# investment annual return
r = 0.04

# percent of total cost as down payment
percent_down_payment = 0.25

# house total cost
house_total_cost = 1e+6

# down payment amount
down_payment = percent_down_payment * house_total_cost

# prompt user for initial annual salary
initial_annual_salary = float(input("Enter initial annual salary: "))

# maximum allowable percentage of salary that will be saved
max_percentage = 0.6

# function bisect
def bisect(err, grad, P):
    """
    Parameters
    ----------
    err : float
        Difference between calculated savings and down payment.
    grad : float list
        List of gradients of percentages of monthly salary savings.
    P : float list
        List of percentages of monthly salary savings.

    Returns
    -------
    perc : float
        Percentage of monthly salary savings as calculated by the fuction.
    """
    if grad == []:
        perc = (P[-1] + max_percentage) / 2
        return perc
    if err > 100:
        if grad[-1] > 0:
            perc = (P[-1] + P[-2]) / 2
        else:
            if grad[-2] > 0:
                perc = (P[-1] + P[-3]) / 2
            else:
                perc = P[-1] + grad[-1]
    else:
        if grad[-1] > 0:
            perc = (P[-1] + max_percentage) / 2
        else:
            perc = (P[-1] + P[-2]) / 2
    return perc  

def savings_calc(perc, S):
    """
    Parameters
    ----------
    perc : float
        Percentage of salary to be saved.
    S : float
        Initial savings.

    Returns
    -------
    S : float
        Savings after 36 months.

    """
    # initialize annual_salary
    annual_salary = initial_annual_salary
    # loop for 36 months
    for i in range(36):
        # every six months raise salary
        if (i % 6 == 0) and (i != 0):
            annual_salary = annual_salary * (1 + e)
        # append investment returns and monthly salary savings to savings    
        S += (S * r / 12) + (annual_salary / 12 * perc)
    return S

# initialize variables
# error 
error = 101
# percentage gradient list
grad = []
# percentage list
p = [0.1]
# while loop counter
bisect_count = 0
# break variable
b_var = 0

while abs(error) > 100:
    # append percentage as calculated from bisect function
    p.append(bisect(error, grad, p))
    # append gradient
    grad.append(p[-1] - p[-2])
    # calculate savings for 36 months
    S = savings_calc(p[-1], 0)
    # calculate error
    error = S - down_payment
    # increase loop counter
    bisect_count += 1
    # if you're over 10 loops and the gradient doesn't change then, exit
    if (bisect_count > 20) and (abs(p[-1] - p[-2]) < 0.001):
        print("It is not possible to pay the down payment in three years")
        # assign exit value to break variable
        b_var = 1
        break

# if break variable is 0, everything OK, print message
if b_var == 0:
    print("Best savings rate: {:.4f}\nSteps in bisection search: {}".\
          format(p[-1], bisect_count))
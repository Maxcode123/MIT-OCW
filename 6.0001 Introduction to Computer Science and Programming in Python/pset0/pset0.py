# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 14:33:52 2020

@author: nikif
"""

# import numpy package
import numpy as np

# prompt user for number x
x = float(input("Enter number x: "))

# prompt user for number y
y = float(input("Enter number y: "))

# print x to the power of y
print("X**y = {}".format(x**y))

# print log base 2 of x
print("log(x) = {}".format(np.log2(x)))

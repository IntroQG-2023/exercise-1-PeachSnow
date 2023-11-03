"""Functions used in the Introduction to Quantitative Geology course"""

# Import any modules needed in your functions here
import math

# Define your new functions below
def mean(numbers):
    return sum(numbers) / len(numbers)

def stddev(numbers):
    mu = mean(numbers)
    variance = sum((x - mu) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

from math import sqrt
def stderr(data):
    n = len(data)
    if n <= 1:
        raise ValueError("Standard error requires at least two data points")
    std_dev = stddev(data) 
    return std_dev / sqrt(n)

import numpy as np
def gaussian(mean, stddev, x_values):
    x_values = np.array(x_values)  
    constant = 1 / (stddev * np.sqrt(2 * np.pi))
    exponent = np.exp(-((x_values - mean) ** 2) / (2 * stddev ** 2))
    return constant * exponent


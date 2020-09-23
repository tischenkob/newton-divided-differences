from math import *
from random import randrange

functions_strings = ["y = cos(-1.5x)", "y = x^2 + 2x + 6", "y = x - 4.321"]
functions = [
    lambda X: [cos(-1.5 * x) for x in X],
    lambda X: [pow(x, 2) + 2 * x + 6 for x in X],
    lambda X: [x - 4.321 for x in X],
]
nodes = [
    [0.001, 0.345, 1.556, 6.111],
    [0.1, 0.3, 0.44, 0.69, 1.64, 2.93, 3.455, 4.13, 5.12, 6.28],
    [4, 11, 16, 31, 40, 55, 60, 86, 103, 164],
]

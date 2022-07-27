from math import *

def isInteger(N):
    X = int(N)
    temp2 = N - X
    if (temp2 > 0):
        return False      
    return True

def roundx(n, decimals=0):
    multiplier = 10 ** decimals
    return floor(n*multiplier + 0.5) / multiplier
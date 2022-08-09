from math import *

#working
def isInteger(N):
    X = int(N)
    temp2 = N - X
    if (temp2 > 0):
        return False      
    return True

#working
def roundx(n, decimals=0, mode=0):
  if mode == 0:
    #round half up
    multiplier = 10 ** decimals
    return floor(n*multiplier + 0.5) / multiplier
  elif(mode == 1):
    #round half down
    multiplier = 10 ** decimals
    return floor(n*multiplier + 0.4) / multiplier
  elif(mode == 2):
    #round up
    return ceil(n)
  elif(mode == 3):
    #round down
    return floor(n)
  elif(mode == 4):
    #rounding half away from 0
    ans = roundx(abs(n), decimals=decimals, mode=0)
    if(n < 0 ):
      return ans * -1
    else:
      return ans 
  elif(mode == 5):
    #rounding half toward 0
    ans = roundx(abs(n), decimals=decimals, mode=1)
    if(n < 0 ):
      return ans * -1
    else:
      return ans 
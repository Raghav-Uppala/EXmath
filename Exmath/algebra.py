from math import *

def quadraticRoots(b,a,c):
  numerator1 = -b + sqrt(b**2 + -4*a*c)
  numerator2 = -b - sqrt(b**2 + -4*a*c)
  denominator = 2*a

  return numerator1/denominator,numerator2/denominator
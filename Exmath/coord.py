from math import *
from .math_func import *

#steps added, working
def distance2P2Dx(x1,y1,x2,y2, steps=False):
  if(steps != False and steps != True):
    return "error"
  dist = sqrt((x2-x1)**2 + (y2-y1))
  if(steps == True):
    steps_arr = []
    steps_arr.append("distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)")
    steps_arr.append(f"distance = sqrt(({x2} - {x1})^2 + ({y2} - {y1})^2)")
    steps_arr.append(f"distance = sqrt({x2 - x1}^2 + {y2 - y1}^2)")
    steps_arr.append(f"distance = sqrt({(x2 - x1)**2} + {(y2 - y1)**2})")
    steps_arr.append(f"distance = sqrt({(x2 - x1)**2 + (y2 - y1)**2})")
    steps_arr.append(f"distance = {dist} units")

    return dist, steps_arr

  else:
    return dist

#steps added, working
def gradient2P2Dx(x1,y1,x2,y2, steps=False):
  if(steps != False and steps != True):
    return "error"
  m = (y2-y1)/(x2-x1)

  if(steps == True):
    steps_arr = []
    steps_arr.append("gradient = (y2 - y1)/(x2 - x1)")
    steps_arr.append(f"gradient = ({y2} - {y1})/({x2} - {x1})")
    steps_arr.append(f"gradient = {y2 - y1}/{x2 - x1}")
    steps_arr.append(f"gradient = {m}")

    return m, steps_arr
  else:
    return m

#steps added, working
def gradientFAx(m, theta, steps=False, r=True, round=3):
  if(r == True):
    if(theta+atan(m) == pi/2 or theta+atan(m) == ((3*pi)/2)):
      return None,None
    else:
      gradient =  roundx(tan(theta+atan(m)),round)
    if(steps == True):
      steps_arr = []
      steps_arr.append("m2 = tan(A + atan(m1))")
      steps_arr.append(f"m2 = tan({theta} + {roundx(atan(m),round)})")
      steps_arr.append(f"m2 = tan({roundx(theta + atan(m),round)})")
      steps_arr.append(f"m2 = {gradient}")
      return gradient,steps_arr
    return gradient
  if(r == False):
    if(radians(theta)+atan(m) == pi/2 or radians(theta)+atan(m) == ((3*pi)/2)):
      return None,None
    else:
      gradient = roundx(tan(radians(theta+degrees(atan(m)))),round)
    if(steps == True):
      steps_arr = []
      steps_arr.append("m2 = tan(A + atan(m1))")
      steps_arr.append(f"m2 = tan({theta} + {roundx(degrees(atan(m)),round)})")
      steps_arr.append(f"m2 = tan({theta + roundx(degrees(atan(m)),round)})")
      steps_arr.append(f"m2 = {gradient}")
      return gradient,steps_arr
    return gradient

#steps added, working
def distance2P3Dx(x1,y1,z1,x2,y2,z2, steps=False):
  if(steps != False and steps != True):
    return "error"
  dist = sqrt(distance2P2Dx(x1,y1,x2,y2)**2+(z2-z1)**2)
  print(dist, dist**2)
  if (steps == True):
    steps_arr = []
    steps_arr.append("distance = sqrt((x2 - x1)^2 + (y2 - y1)^2+(z2 - z1)^2)")
    steps_arr.append(f"distance = sqrt(({x2} - {x1})^2 + ({y2} - {y1})^2+({z2} - {z1})^2)")
    steps_arr.append(f"distance = sqrt({x2 - x1}^2 + {y2 - y1}^2 + {z2 - z1}^2)")
    steps_arr.append(f"distance = sqrt({(x2 - x1)**2} + {(y2 - y1)**2} + {(z2 - z1)**2})")
    steps_arr.append(f"distance = sqrt({dist**2})")
    steps_arr.append(f"distance = {dist} units")

    return dist,steps_arr
  elif(steps == False):
    return dist

#steps added, working
def midpoint2Px(x1,y1,x2,y2, steps=False):
  midpoint = ((x1+x2)/2, (y1+y2)/2)
  if(steps == True):
    steps_arr = []
    steps_arr.append("midpoint = ((x1 + x2)/2, (y1 + y2)/2)")
    steps_arr.append(f"midpoint = (({x1} + {x2})/2, ({y1} + {y2})/2)")
    steps_arr.append(f"midpoint = (({x1+x2})/2, ({y1+y2})/2)")
    steps_arr.append(f"midpoint = {midpoint}")

    return midpoint, steps_arr
  elif(steps == False):
    return midpoint

#steps added, working
def perpendicularBisector2Px(x1,y1,x2,y2, steps=False):
  midpoint = midpoint2Px(x1,y1,x2,y2)
  m1 = gradient2P2Dx(x1,y1,x2,y2)
  m = gradientFAx(m1, 90, r=False)
  c = midpoint[1] - m*midpoint[0]

  ans = f"y = {m}x + {c}"

  if(steps == True):
    steps_arr = []
    steps_arr.append("gradient = -1/((y2 - y1)/(x2 - x1))")
    steps_arr.append(f"gradient = -1/(({y2} - {y1})/({x2} - {x1}))")
    steps_arr.append(f"gradient = -1/({y2 - y1}/{x2 - x1})")
    steps_arr.append(f"gradient = -1/{y2 - y1/x2 - x1}")
    steps_arr.append(f"gradient = {m}")
    
    steps_arr.append("y = mx + c")
    steps_arr.append(f"{midpoint[1]} = {m}{midpoint[0]} + c")
    steps_arr.append(f"c = {midpoint[1]} - {m}{midpoint[0]}")
    steps_arr.append(f"c = {midpoint[1]} - {m * midpoint[0]}")
    steps_arr.append(f"c = {c}")

    steps_arr.append("y = mx + c")
    steps_arr.append(ans)

    return ans,steps_arr
  elif(steps == False):
    return ans

#steps added, working
def lineFrom2Px(x1,y1,x2,y2, steps=False):
  m = gradient2P2Dx(x1, y1, x2, y2, steps=True)
  c = y1 - m[0]*x1
  ans = f"y = {m[0]}x + {c}"

  if(steps == True):
    steps_arr = []
    for x in m[1]:
      steps_arr.append(x)
    
    steps_arr.append("y = mx + c")
    steps_arr.append(f"c = {y1} - {m[0]} * {x1}")
    steps_arr.append(f"c = {y1} - {m[0] * x1}")
    steps_arr.append(f"c = {c}")

    steps_arr.append("y = mx + c")
    steps_arr.append(ans)
    
    return ans, steps_arr
  elif(steps == False):
    return ans

#steps not added, working
def collinearTest3P2Dx(x1,y1,x2,y2,x3,y3, steps=False):
  m12 = gradient2P2Dx(x1,y1,x2,y2, steps=steps)
  m23 = gradient2P2Dx(x2,y2,x3,y3, steps=steps)

  if(steps == True):
    steps_arr = []
    for x in m12[1]:
      step = x[:8] + " 1" + x[8:]
      steps_arr.append(step)
    for x in m23[1]:
      step = x[:8] + " 2" + x[8:]
      steps_arr.append(step)
    if(float(m12[0]) == float(m23[0])):
      col =  True
      steps_arr.append("Because gradient 1 = gradient 2, the points are collinear")
    else:
      col =  False
      steps_arr.append("Because gradient 1 != gradient 2, the points are not collinear")
    return col, steps_arr
  elif(steps == False):
    return col
from math import *
import numpy as np
import matplotlib.pyplot as plt

def graphx(r=2, A=1, B=1, C=0, D=0):
  x = np.arange(0,r*np.pi,0.1)
  y = A * np.sin(B*(x+C)) + D
  plt.plot(x,y)

  px = [0,r * np.pi]
  py = [0,0]
  plt.plot(px,py)

  plt.show()
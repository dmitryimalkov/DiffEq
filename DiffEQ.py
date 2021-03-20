"""
Диф. уравнение 1-го порядка
y'=-y(t)*t, y(-2)=1
Нужно инсталлировать все модули:
pip install numpy
pip install scipy
pip install matplotlib
"""

import numpy as np
from scipy. integrate import odeint
import matplotlib.pyplot as plt

 # create function
def dydt(y, t):
	return -y*t

t = np.linspace( -2, 2, 51) # vector of time
y0 = 1 # start value
y = odeint (dydt, y0, t) # solve eq.
y = np.array(y).flatten()
plt.plot( t, y,'-sr', linewidth=3) # graphic
plt.show() # display
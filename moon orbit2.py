# PROBLEM 1
#
# Modify the orbit function below to model
# one revolution of the moon around the earth,
# assuming that the orbit is circular.
#
# Use the math.cos(angle) and math.sin(angle) 
# functions in order to accomplish this.

import math
import numpy
import matplotlib.pyplot
#from udacityplots import *

moon_distance = 384e6 # m

def orbit():
    num_steps = 100
    x = numpy.zeros([num_steps + 1, 2])
    for step in range(num_steps+1):
        angle = 2. * math.pi * step / num_steps
        x[step][0] = math.cos(angle) * moon_distance
        x[step][1] = math.sin(angle) * moon_distance
    return x

x = orbit()

#@show_plot
def plot_me():
    matplotlib.pyplot.axis('equal')
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()
    
plot_me()

# PROBLEM 2
#
# Modify the trajectory function below to 
# plot the trajectory of several particles. 
# Each trajectory starts at the point (0,0) 
# given initial speed in the direction 
# specified by the angle. Use the Forward 
# Euler Method to accomplish this.

import math
import matplotlib.pyplot
import numpy
#from udacityplots import *

h = 0.1 # s
g = 9.81 # m / s2
acceleration = numpy.array([0., -g])
initial_speed = 20. # m / s

#@show_plot
def trajectory():
    angles = numpy.linspace(20., 70., 6)
    print angles

    num_steps = 30
    x = numpy.zeros([num_steps + 1, 2])
    v = numpy.zeros([num_steps + 1, 2])

    for angle in angles:
        print angle
        h_vel = math.cos(angle/360*2*math.pi)*initial_speed
        v[0,1] = math.sin(angle/360*2*math.pi)*initial_speed
        for step in range(num_steps):
#            t[step + 1] = h * (step + 1)
            x[step + 1,1] = x[step,1] + h * v[step,1]
            v[step + 1,1] = v[step,1] - h * g
            x[step + 1,0] = x[step,0] + h * h_vel
        print x
        matplotlib.pyplot.plot(x[:, 0], x[:, 1])
        matplotlib.pyplot.axis('equal')
        axes = matplotlib.pyplot.gca()
        axes.set_xlabel('Horizontal position in m')
        axes.set_ylabel('Vertical position in m')
    matplotlib.pyplot.show()
#    return x, v

trajectory()
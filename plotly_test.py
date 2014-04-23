import plotly
py = plotly.plotly("dkens", "qcskp0copu")

from numpy import *
 
# generate some random sets of data
y0 = random.randn(100)/5. + 0.5 
x0 = random.randn(100)/5. + 0.5 
 
y1 = random.standard_cauchy(20)
x1 = random.standard_cauchy(20)

x = concatenate([x0,x1])
y = concatenate([y0,y1])

scatter0 = {'x': x0, 'y': y0, 'name': 'normal', 'type': 'scatter', 'mode': 'markers', 'marker': {'size':4,'opacity':0.5}}
scatter1 = {'x': x1, 'y': y1, 'name': 'cauchy', 'type': 'scatter', 'mode': 'markers', 'marker': {'size':4,'opacity':0.5,'symbol':'cross'}}
hist2d = {'x': x, 'y': y, 'type': 'histogram2d'}

py.plot([scatter0, scatter1, hist2d])
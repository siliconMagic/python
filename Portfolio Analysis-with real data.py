# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.data import DataReader
from datetime import datetime

# <codecell>

# %matplotlib inline

# <rawcell>

# Run the next three cells for real data

# <codecell>

start = datetime(2004,2,1)
end = datetime.today()

# stock list
L = ['DDD', 'DIS', 'COST', 'SBUX']

#set up DataFrames
daily_price  = pd.DataFrame(index=pd.bdate_range(start, end)) # business days
daily_return = pd.DataFrame(index=pd.bdate_range(start, end))

# <codecell>

# get daily equity "Adj Close" from start to end
# would like to build a database of SP500 stocks instead

daily_price = DataReader(L, 'yahoo', start, end)['Adj Close']

daily_return = np.log(1+daily_price.pct_change())  # for a continuous return number
# cumulative_return = daily_return.cumsum()        useful for a normalized return chart

# <codecell>

# create expected return vector, stdev vector and covariance, correlation matrices

R = daily_return.mean() # expected return vector
AAR = (1+R)**252-1      # average annual return vector
SD = daily_return.std()  # expected standard deviation vector
C = np.matrix(daily_return.cov())  # covariance matrix
Corr =  daily_return.corr() # and a correlation matrix for info

# <rawcell>

# Comment out R, SD and C in the cell below to run with real data from above

# <codecell>

W = [1/3, 1/3, 1/3, 0]
R = [.06, .02, .04]
C = np.matrix([[8, -2, 4], [-2, 2, -2], [4, -2, 8]])/1000
SD = [np.sqrt(C[i,j]) for i in range(len(R)) for j in range(len(R)) if i == j]
r = .05    # an initial target return
rf = 0.01  # risk free rate

# <codecell>

def make_Muvec(R):        # R is a list [] of returns as real numbers
    Muvec = np.array(R)
    return Muvec
    
def make_Onevec(R):
    Onevec = np.ones(len(R))
    return Onevec

def make_Xvec(R):         # W is a list [] of weights as real numbers 
    Xvec = np.ones(len(R))/len(R)
    return Xvec

# <codecell>

def make_LMtarget(r, R):      # r is a target return as a real number
    LMtarget = np.append(np.zeros(len(R)), [r,1])
    return np.matrix(LMtarget)

# <codecell>

def Initialize(R, r):
    M = make_Muvec(R)
    O = make_Onevec(R)
    X = make_Xvec(R)
    LMt = make_LMtarget(r,R)
    return M, O, X, LMt

# <codecell>

Muvec, Onevec, Xvec, LMtarget = Initialize(R,r)

# <codecell>

Equal_return = np.sum(Muvec * Xvec)
Equal_var = np.matrix(Xvec) * C * np.matrix(Xvec).T
Equal_vol = np.sqrt(Equal_var)
print("Equal weighted return: {:.2%} with a {:.2%} volatility".format(Equal_return, Equal_vol.item()))

# <codecell>

def make_LMmat(C, R, Muvec, Onevec): # C is the covariance matrix as an NxN matrix of real numbers
    D = np.append(2*C, [Muvec], axis=0)
    E = np.append(D, [Onevec], axis=0)
    F = np.insert(E, len(R), np.append(Muvec, [0,0])*-1, axis=1)
    G = np.insert(F, len(R)+1, np.append(Onevec, [0,0])*-1, axis=1)               
    return G

# <codecell>

LMmat = make_LMmat(C, R, Muvec, Onevec)

# <codecell>

def MinVar_target_return(C, LMmat, LMtarget):
    Xvec_target = LMmat.I * LMtarget.T
    Xvec_target = Xvec_target[:-2]
    target_var = Xvec_target.T * C * Xvec_target
    target_SD = np.sqrt(target_var)         # SD is standard deviation - measures volatility
    return Xvec_target, target_SD

# <codecell>

Target_weights, target_SD = MinVar_target_return(C, LMmat, LMtarget)
print("For a return of {:.2%} the minimum volatility is: {:.2%}".format(r, target_SD.item()))

# <codecell>

def MinVar_port(C, Muvec, Onevec):
    Muvec = np.matrix(Muvec).T
    Onevec = np.matrix(Onevec).T
    Xminvec = 1/np.sum(C.I * Onevec) * C.I * Onevec
    Xmin_return = 1/np.sum(C.I * Onevec) * Muvec.T * C.I * Onevec
    Xmin_SD = np.sqrt(Xminvec.T * C * Xminvec)
    return Xminvec, Xmin_return, Xmin_SD

# <codecell>

Xminvec, Xmin_return, Xmin_SD = MinVar_port(C, Muvec, Onevec)
for i, weight in enumerate(Xminvec):
    print(i, weight)
print("Min Variance return: {:.2%} with a {:.2%} volatility".format(Xmin_return.item(), Xmin_SD.item()))

# <codecell>

def Sharpe_port(C, Muvec, rf):
    Muvec = np.matrix(Muvec).T
    Muhat = Muvec - rf
    XShvec = 1/np.sum(C.I * Muhat) * C.I * Muhat
    XSh_return = 1/np.sum(C.I * Muhat) * Muvec.T * C.I * Muhat
    XSh_SD = np.sqrt(1/np.sum(C.I * Muhat)**2 * Muhat.T * C.I * C * C.I * Muhat)
    Sharpe_ratio = (XSh_return - rf)/XSh_SD
    return XShvec, XSh_return, XSh_SD, Sharpe_ratio

# <codecell>

XShvec, XSh_return, XSh_SD, Sharpe_ratio = Sharpe_port(C, Muvec, rf)
for i, weight in enumerate(XShvec):
    print(i, weight)
print("Sharpe Optimal return: {:.2%} with volatility: {:.2%}".format(XSh_return.item(), XSh_SD.item()))
print("Sharpe ratio: {:.2f}".format(Sharpe_ratio.item()))

# <codecell>

def Find_Frontier(C, Muvec, rf):
    frontier = []
    frontier_weights = []
    r_points = np.arange(min(Muvec)/1.2, max(Muvec)*1.2, (max(Muvec)-min(Muvec))/100)
    for r in r_points:
        LMtarget = make_LMtarget(r,R)
        Target_weights, target_SD = MinVar_target_return(C, LMmat, LMtarget)
        frontier.append([target_SD.item(), r])
        frontier_weights.append((r, Target_weights))
    return frontier, frontier_weights

# <codecell>

frontier, frontier_weights = Find_Frontier(C,Muvec,rf)

# <codecell>

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Portfolio Analysis')
ax.set_ylabel('Return')
ax.set_xlabel('Volatility')

x,y = zip(*frontier)
line, = ax.plot(x, y, color='b', lw=1)

ax.scatter(SD, Muvec, color='c')
ax.scatter(Equal_vol, Equal_return, color='k')

ax.scatter(0, rf, color='orange')
ax.scatter((max(Muvec)-rf)/Sharpe_ratio, max(Muvec), color='orange')
ax.scatter(max(SD), rf+max(SD)*Sharpe_ratio, color='orange')

ax.plot([0,max(SD)], [rf, rf+max(SD)*Sharpe_ratio], color='y', lw=1)

ax.scatter(XSh_SD, XSh_return, color='g')
ax.scatter(Xmin_SD, Xmin_return, color='r')

plt.grid(True)
plt.show()

# <codecell>

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Portfolio Analysis')
ax.set_ylabel('weight')
ax.set_xlabel('Return')

r, W = zip(*frontier_weights)
y1=[]
y2=[]
y3=[]
y4=[]
for point in W:
    y1.append(point[0].item())
    y2.append(point[1].item())
    y3.append(point[2].item())
#    y4.append(point[3].item())

plt.plot(r,y1, color='b')
plt.plot(r,y2, color='c')
plt.plot(r,y3, color='r')
#plt.plot(r,y4, color='m')

plt.plot([Xmin_return.item(), Xmin_return.item()], [0, 1], color='orange', lw=2)
plt.plot([XSh_return.item(), XSh_return.item()], [0, 1], color='g', lw=2)

plt.grid(True)

plt.show()



# <codecell>



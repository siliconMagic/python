import pandas as pd
import numpy as np
from scipy.optimize import minimize
from matplotlib.pyplot import plot, scatter, show
from pandas.io.data import DataReader
from datetime import datetime


start = datetime(2011,11,1)
end = datetime.today()
L = ['SPY', 'SBUX', 'DISCK', 'DIS', 'COST', 'GLD'] # stock list

#set up DataFrames
daily_stock_price = pd.DataFrame(index=pd.date_range(start, end)) 
daily_stock_return = pd.DataFrame(index=pd.date_range(start, end))

for ticker in L:
    stock = DataReader(ticker,'yahoo',start,end)   # pandas module to get stock prices
    daily_stock_price[ticker] = stock['Adj Close'] # just want Adj Close prices (includes div)
    
daily_stock_price = daily_stock_price.dropna()     #strip out the non-trading days
daily_stock_return = np.log(1+daily_stock_price.pct_change()) # for a continuous return number

plot(daily_stock_price)
plot(daily_stock_return)

#create avg return, stdev vectors and covariance matrix
R = daily_stock_return.mean() # expected return vector
R = (1+R)**250-1              # annualized
S = daily_stock_return.std()  # expected standard deviation vector
S = S*np.sqrt(250)            # annualized
C = daily_stock_return.cov()  # covariance matrix
C = C*250                     # annualized

print('data for the period ',start, end)
print('yearly returns:')
print(R)
print('standard deviations')
print(S)
print('covariance matrix')
print(C)

def port_return(W):
    return np.dot(R, W)
    
def port_var(W):
    return np.dot(W, np.dot(C, W))
    
# Given risk-free rate, assets returns and covariances, this function calculates
# mean-variance frontier and returns its [x,y] points in two arrays
def find_frontier(R, C, rf):
        def fitness(W, R, C, r):
                # For given level of return r, find weights that minimize portfolio variance.
                mean, var = port_return(W), port_var(W)
                # Big penalty for not meeting stated portfolio return effectively serves as optimization constraint
                penalty = 50*abs(mean-r)
                return var + penalty
        frontier_mean, frontier_var, frontier_weights = [], [], []
        for r in np.linspace(min(R), max(R), num=20):   # iterate through a range of returns on Y axis
                W = np.ones([len(L)])/len(L)            # start optimization with equal weights
                b_ = [(0.,1.) for i in range(len(L))]
                c_ = ({'type':'eq', 'fun': lambda W: sum(W)-1. })
                optimized = minimize(fitness, W, (R, C, r), method='SLSQP', constraints=c_, bounds=b_)   
                if not optimized.success: 
                        raise BaseException(optimized.message)
                # add point to the min-var frontier [x,y] = [optimized.x, r]
                frontier_mean.append(r)                                                 # return
                frontier_var.append(np.sqrt(port_var(optimized.x)))   # min-variance based on optimized weights
                frontier_weights.append(optimized.x)
        return np.array(frontier_mean), np.array(frontier_var), frontier_weights

def optimum_weights(C, rf):
    def Sharpe(W, C, rf):
        mean, var = port_return(W), port_var(W) 
        util = (mean - rf) / np.sqrt(var) # calculates the Sharpe Ratio
        return 1/util                     # maximize utility, minimize the function
    W = np.ones([len(L)])/len(L)
    b_ = [(0., 1.) for i in range(len(L))]     # weights between 0 and 100%, no shorts
    c_ = ({'type':'eq', 'fun': lambda W: sum(W)-1. }) # weights must add to 100%
    optimized = minimize(Sharpe, W, (C, rf), method='SLSQP', constraints=c_, bounds=b_) # the magic scipy function!
    if not optimized.success:
        raise BaseException(optimized.message)
    return optimized.x
    
rf = 0

O_W = optimum_weights(C, rf)
F_M, F_S, F_W = find_frontier(R, C, rf)

for i, stock in enumerate(O_W):
    print('{}     {:.2%}'.format(L[i],stock))
print('portfolio return: {:.2%}'.format(port_return(O_W)))

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
# import numpy as np
# from scipy.optimize import minimize
from matplotlib.pyplot import show
from pandas.io.data import DataReader
from datetime import datetime, timedelta

# <codecell>

# %matplotlib inline

# <codecell>

end = datetime.today()
start = end - timedelta(days=365)

# stock list
ticker = ['AAPL', 'AMZN', 'ATVI', 'BBBY', 'BRK.B', 'COST', 'DDD', 'DIS', 'DISCK', 'F', 'GLD', 'SBUX', 'SPY']
share = [635, 850, 12313, 1104, 840, 2115, 922, 2007, 1840, 5000, 1124, 2542, 165]

#set up DataFrames
daily_stock_price  = pd.DataFrame(index=pd.bdate_range(start, end)) # business days
daily_stock_share = pd.DataFrame(index=pd.bdate_range(start, end), columns=ticker)
daily_stock_value = pd.DataFrame(index=pd.bdate_range(start, end), columns=ticker)
daily_portfolio_value = pd.DataFrame(index=pd.bdate_range(start, end))

# <codecell>

daily_stock_price = DataReader(ticker, 'yahoo', start, end)['Adj Close']

# <codecell>

for i, s in enumerate(ticker):
    daily_stock_share[s] = share[i]
daily_stock_value = daily_stock_price * daily_stock_share
daily_portfolio_value = daily_stock_value.sum(axis=1)

# <codecell>

print(daily_stock_price.head())

# <codecell>

print(daily_stock_price.tail())

# <codecell>

print(daily_stock_share.head())

# <codecell>

daily_stock_value.dropna().plot()
show()

# <codecell>

daily_portfolio_value = daily_portfolio_value.dropna()

# <codecell>

daily_portfolio_value.plot()
show()

# <codecell>

year_return = daily_portfolio_value[-1:] - daily_portfolio_value[0]

# <codecell>

percent_return = year_return / daily_portfolio_value[0]

# <codecell>

print("Start: ${:,.2f} on {:%Y-%m-%d}".format(daily_portfolio_value[0], daily_portfolio_value.index[0]))
print("  End: ${:,.2f} on {:%Y-%m-%d}".format(daily_portfolio_value[-1], daily_portfolio_value.index[-1]))
print("  Min: ${:,.2f} on {:%Y-%m-%d}".format(daily_portfolio_value.min(), daily_portfolio_value.idxmin()))
print("  Max: ${:,.2f} on {:%Y-%m-%d}".format(daily_portfolio_value.max(), daily_portfolio_value.idxmax()))
print("Total return for the year is ${:,.2f} for a return of {:.2%}".format(year_return[0], percent_return[0]))

# <codecell>



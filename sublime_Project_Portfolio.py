
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
# from pylab import *
import pandas as pd
from pandas.io.data import DataReader
from datetime import date, timedelta
# import vincent
# vincent.core.initialize_notebook()


# In[32]:

# %matplotlib inline


# In[18]:

end = date.today()
start = end - pd.DateOffset(years=10)
periods = [1,2,3,5,10] # in years
periods = [x*12 for x in periods] # in months

# stock list
L = ['AAPL', 'AMZN', 'ATVI', 'BBBY', 'BRK.B','COST', 'DDD', 'DIS', 
     'DISCK', 'EPD', 'ETP', 'KMP', 'MMP', 'PAA', 'SBUX', 'VDE', 'VNQ', 'VCIT']

# transaction list
T = []

#set up DataFrames
# daily_close = pd.DataFrame(index=pd.date_range(start, end))
daily_share = pd.DataFrame(index=pd.bdate_range(start, end), columns=L)
daily_value = pd.DataFrame(index=pd.bdate_range(start, end), columns=L)
#monthly_return = pd.DataFrame(index=pd.date_range(start, end))
irr_table = pd.DataFrame(index=periods, columns=L)


# In[19]:

# get daily equity "Adj Close" from start to end
# would like to build a database of SP500 stocks instead

daily_close = DataReader(L, 'yahoo', start, end)['Adj Close']


# In[20]:

print(daily_close.tail(10))


# In[21]:

def add_trans(trans_date, action, shares, ticker, cash_flow):
    if action == 'buy':
        if daily_share[ticker][trans_date] is np.nan: daily_share[ticker][trans_date] = 0 # for first buy 
        daily_share[ticker][trans_date:] = daily_share[ticker][trans_date] + shares
    elif action == 'sell':
        daily_share[ticker][trans_date:] = daily_share[ticker][trans_date] - shares
    elif action == 'split':
        daily_share[ticker][trans_date:] = daily_share[ticker][trans_date] + shares
    else:
        print('action not recognized as "buy", "sell" or "split"')


# In[22]:

add_trans(date(2006, 2, 24), 'buy', 195, 'AAPL',0)
add_trans(date(2006, 7, 6), 'buy', 700, 'AAPL',0)
add_trans(date(2007, 6, 8), 'buy', 160, 'AAPL',0)
add_trans(date(2008, 2, 6), 'buy', 150, 'AAPL',0)
add_trans(date(2008, 9, 12), 'buy', 260, 'AAPL',0)
add_trans(date(2010, 10, 18), 'sell', 1020, 'AAPL',0)
add_trans(date(2012, 5, 21), 'buy', 190, 'AAPL',0)


# In[34]:

plt.plot(daily_share['AAPL'])
plt.figure()


# In[27]:

daily_value = daily_close * daily_share
plt.plot(daily_value['AAPL'])
plt.figure()


# In[28]:

monthly_close = daily_close.resample('M')
monthly_return = np.log(monthly_close / monthly_close.shift(1))
avg_yearly_return = (monthly_return.mean()+1)**12-1
plt.scatter(monthly_return.mean(), monthly_return.std())
plt.figure()
print(monthly_return.corr())


# In[10]:

def xirr(transactions):
    years = [(ta[0] - transactions[0][0]).days / 365.0 for ta in transactions]
    residual = 1
    step = 0.05
    guess = 0.05
    epsilon = 0.00001
    limit = 10000
    while abs(residual) > epsilon and limit > 0:
        limit -= 1
        residual = 0.0
        for i, ta in enumerate(transactions):
            residual += ta[1] / pow(guess, years[i])
        if abs(residual) > epsilon:
            if residual > 0:
                guess += step
            else:
                guess -= step
                step /= 2.0
    return guess-1


# In[11]:

months = 60
begin = monthly_close.AMZN[-1-months]
end = monthly_close.AMZN[-1]
irr = ((end-begin)/begin + 1)**(12/months) - 1
print("{:%}".format(irr))


# In[12]:

tas2 = [(monthly_close.index[-1-months], -monthly_close.AMZN[-1-months]),
        (monthly_close.index[-1], monthly_close.AMZN[-1])]
print("{:%}".format(xirr(tas2)))


# In[29]:

def build_IRR (periods, monthly_close):
    for stock in monthly_close.iteritems():
        for period in periods:
            begin = stock[1][-1-period]
            end = stock[1][-1]
            irr = ((end-begin)/begin + 1)**(12/period) - 1
            irr_table[stock[0]][period] = irr
    return
        
build_IRR(periods, monthly_close)
print(irr_table)


# In[30]:

# writer = pd.ExcelWriter('output.xlsx')
# daily_close.to_excel(writer, 'daily close')
# monthly_close.to_excel(writer, 'monthly close')
# monthly_return.to_excel(writer, 'monthly return')
# irr_table.to_excel(writer, 'IRR table')
# writer.save()


# In[33]:

# line = vincent.Line(monthly_close)
# line.axis_titles(x='Date', y='Price')
# line.legend(title='Daily Prices')
# line.display()


plt.plot(np.log(monthly_close))
plt.show()




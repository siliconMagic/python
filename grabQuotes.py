'''The first input of DataReader is the name of the dataset (e.g. the stock ticker for YF)
and the second is the location of the dataset ("yahoo" for YF). The msft object is a DataFrame
object whose rows are days of the year and columns are the prices for each day, labelled Open,
High, Low, Close, Volume and Adj Close, respectively. '''


from pandas.io.data import DataReader
from datetime import datetime

aapl = DataReader("AAPL", "yahoo")
aapl = DataReader("AAPL", "yahoo", datetime(2009,1,1))
print aapl["Adj Close"][-150:]

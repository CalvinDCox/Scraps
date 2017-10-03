#This file just pulls info from my favorite ticker

import pandas as pd
import pandas_datareader as web  #Module imports data from web (author says may change based on version)
import datetime
import matplotlib.pyplot as plt

#Prices over the past Month, starting in september
start = datetime.datetime(2016,9,1) #Pretty sure it goes year day month
end = datetime.datetime.today()

# Get Coca-Cola stock data 'KO'
#Author says get the series first, then the source. So series KO source in this case is yahoo (could be google) and then the start and end times
cola = web.DataReader("KO", "yahoo", start, end)

cola.head()

cola["Adj Close"].plot(grid=False) #Plot the adjusted closing price

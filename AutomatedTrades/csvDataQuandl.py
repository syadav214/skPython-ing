import quandl
import pandas as pd

#aapl = quandl.get('WIKI/AAPL',start_date="2016-10-01",end_date="2017-01-01")
#aapl.to_csv('file_name.csv', sep=' ')

aapl_data = pd.read_csv('file_name.csv')
print(aapl_data.head())
print(aapl_data.head(10))
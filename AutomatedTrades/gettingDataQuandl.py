import quandl
#www.quandl.com/tools/python

aapl = quandl.get('WIKI/AAPL',start_date="2016-10-01",end_date="2017-01-01")
#print(type(aapl))

#To get numpy object
#aapl_numpy = quandl.get('WIKI/AAPL',start_date="2012-10-01",end_date="2017-01-01", returns="numpy")
#print(type(aapl_numpy))

print(aapl.head()) #first 5 rows
print(aapl.tail()) #last 5 rows
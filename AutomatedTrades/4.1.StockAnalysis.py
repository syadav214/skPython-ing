import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#amzn = quandl.get("WIKI/AMZN", start_date="2017-01-01", end_date="2018-01-01")
#amzn.to_csv('amzn.csv', sep=',')

amzn = pd.read_csv('amzn.csv')
#print(amzn.head())

amzn_daily_close = amzn[['Adj. Close']]
amzn_daily_pct_c = amzn_daily_close.pct_change()
amzn_daily_pct_c.fillna(0, inplace=True)
#print(amzn_daily_pct_c.head())

amzn_daily_log_returns = np.log(amzn_daily_close.pct_change()+1)
#print(amzn_daily_log_returns.head())

#monthly = amzn.resample('BM').apply(lambda x: x[-1])
#amzn_monthly_pct_c = monthly.pct_change()
#print(amzn_monthly_pct_c)

quarter = amzn.resample("4M").mean()
print(quarter.pct_change())
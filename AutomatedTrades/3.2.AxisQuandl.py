import pandas as pd
import matplotlib.pyplot as plt

aapl_data_index = pd.read_csv('file_name.csv',index_col='Date',parse_dates=True)
aapl_data_index = aapl_data_index.sort_index()
aapl_data_index.index = pd.to_datetime(aapl_data_index.index)

aapl_data_index['Adj. Close'].plot()
plt.show()
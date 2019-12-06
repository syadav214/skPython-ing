import pandas as pd
import matplotlib.pyplot as plt

aapl_data = pd.read_csv('file_name.csv')
aapl_data['Close'].plot()
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('data_challenge_stock_prices.csv')
r_i = []
r_mean = [0]*100
r = [0]*(len(df.iloc[:,1])-2)
for i in range(100):
    print(1)
    for j in range(len(df.iloc[:,1])-2):
        r[j] = (df.iloc[j+1,i]-df.iloc[j,i])/df.iloc[j,i]
    r_i.append(r)
    r_mean[i] = np.mean(r)


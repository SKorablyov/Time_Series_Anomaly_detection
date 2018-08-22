# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:08:43 2018

@author: Librarian
"""
import matplotlib.pyplot as plt
import pandas as pd
# import Data_Extraction as de
from luminol.anomaly_detector import AnomalyDetector
import Data_Processing as dp
# import luminol


# file_names = de.Data_Extract('train_AD.csv', 'BTCUSD')


TIME_INTERVAL = 5000

file_names = ['BUY_BTCUSD.csv', 'SELL_BTCUSD.csv']
file_names = dp.Data_Processing(file_names, 'BTCUSD', TIME_INTERVAL)

#file_names = ['PTI_BUY_BTCUSDPER30000.csv','PTI_SELL_BTCUSDPER30000.csv']

df_sell = pd.read_csv(file_names[1], encoding="ISO-8859-1")
df_buy = pd.read_csv(file_names[0], encoding="ISO-8859-1")

#box_sell=[]
#box_sell=MPA.analysis_price('SELL_BTCUSD.csv',TIME_INTERVAL)


#box_buy=[]
#box_buy=MPA.analysis_price('BUY_BTCUSD.csv',TIME_INTERVAL)



counter = 0
container = []
box_volume = []
volume = 0
box_difference = []
lts = {}

for i in df_buy['VALUE']:
    container.append(counter)
    difference = df_buy['PRICE'][counter] - df_sell['PRICE'][counter]
    volume = volume-df_buy['VOLUME'][counter] + df_sell['VOLUME'][counter]
    box_difference.append(difference)
    box_volume.append(volume)
    lts[counter] = difference
    counter += 1
plt.plot(container, box_difference)

detector = AnomalyDetector(lts)
anomalies = detector.get_anomalies()

k = 0
while k < len(anomalies):
    time_period = anomalies[k].get_time_window()
    container_anomalies = []
    box_difference_anomalies = []
    i = time_period[0]
    while i <= time_period[1]:
        i += 1
        container_anomalies.append(i)
        difference = df_buy['PRICE'][i] - df_sell['PRICE'][i]
        box_difference_anomalies.append(difference)
    k+=1
    plt.plot(container_anomalies, box_difference_anomalies)

plt.show()
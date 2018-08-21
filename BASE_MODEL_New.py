# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:08:43 2018

@author: Librarian
"""
import pandas as pd
import matplotlib.pyplot as plt
#import tensorflow as tf

#import Data_Extraction as DE
#import MEAN_PRICE_ANALYSIS as MPA
import Data_Processing as DP
#import Analysis_Buy as BUY
#import Analysis_Sell as SELL

#FILE_NAMES=DE.Data_Extract('train_AD.csv','BTCUSD')
TIME_INTERVAL=600000

File_Names=DP.Data_Processing('train_AD.csv','BTCUSD',TIME_INTERVAL)

DF_SELL=pd.read_csv(File_Names[1], encoding = "ISO-8859-1")
DF_BUY=pd.read_csv(File_Names[0], encoding = "ISO-8859-1")

#BOX_SELL=[]
#BOX_SELL=MPA.analysis_price('SELL_BTCUSD.csv',TIME_INTERVAL)


#BOX_BUY=[]
#BOX_BUY=MPA.analysis_price('BUY_BTCUSD.csv',TIME_INTERVAL)

BOX_SELL=[]
BOX_SELL=DF_SELL['PRICE']

BOX_BUY=[]
BOX_BUY=DF_BUY['PRICE']

COUNTER=0
CONTAINER=[]

BOX_DIFFERENCE=[]

for i in BOX_BUY :
    
    #print(COUNTER)
    CONTAINER.append(COUNTER)
    
    DIFFERENCE=BOX_SELL[COUNTER]-BOX_BUY[COUNTER]
    BOX_DIFFERENCE.append(DIFFERENCE)
    
    COUNTER+=1
    
plt.plot(CONTAINER,BOX_DIFFERENCE)
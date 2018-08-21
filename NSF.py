# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 22:31:05 2018

@author: Librarian
"""

import pandas as pd 
#import matplotlib.pyplot as plt

def analysis_balance(FILE_NAME,TIME_INTERVAL) :

 df=pd.read_csv(FILE_NAME, encoding = "ISO-8859-1")

 df['index_col'] = df.index

 k=0

 ZERO_TIME=df['TIMESTAMP'][0]

 #TIME_INTERVAL=480000

 END_TIME=ZERO_TIME+TIME_INTERVAL

 COUNTER=0
 EXTRA_COUNTER=0
 SUMM_VALUE=0
 SUMM_PRICE=0
    
 BOX_MEAN_VALUE=[]
 BOX_MEAN_PRICE=[]
 #BOX_MEAN_DIFFERENCE=[]
 CONTAINER=[]

 for k in df['index_col'] :
    
        if   df['TIMESTAMP'][k] >= END_TIME :
            END_TIME=END_TIME+TIME_INTERVAL
            COUNTER=COUNTER+1
            SUMM_VALUE=SUMM_VALUE+df['PRICE'][k]*df['TRADE_SIZE'][k]
            SUMM_PRICE=SUMM_PRICE+df['PRICE'][k]
            MEAN_VALUE=SUMM_VALUE/COUNTER
            MEAN_PRICE=SUMM_PRICE/COUNTER
            CONTAINER.append(EXTRA_COUNTER)
            EXTRA_COUNTER=EXTRA_COUNTER+1
            BOX_MEAN_VALUE.append(MEAN_VALUE)
            BOX_MEAN_PRICE.append(MEAN_PRICE)
            COUNTER=0
            SUMM_VALUE=0
            SUMM_PRICE=0
        else :
                COUNTER=COUNTER+1
                SUMM_VALUE=SUMM_VALUE+df['PRICE'][k]*df['TRADE_SIZE'][k]
                SUMM_PRICE=SUMM_PRICE+df['PRICE'][k]
        
 ZERO_TIME=df['TIMESTAMP'][0]

 END_TIME=ZERO_TIME+TIME_INTERVAL

 COUNTER=0
 EXTRA_COUNTER=0
 VALUE=0
 K=0

 while  df['TIMESTAMP'][K] < END_TIME : 
            COUNTER=COUNTER+1
            VALUE=VALUE+df['TRADE_SIZE'][k]
            K=COUNTER
            
 END_TIME=END_TIME+TIME_INTERVAL
 MEAN_PRICE=SUMM_PRICE/K      
 MEAN_VALUE_0=VALUE/COUNTER
 BOX_MEAN_VALUE.append(MEAN_VALUE_0)
 
 COUNTER=0
 VALUE=0

 for K in df['index_col'] :
        if   df['TIMESTAMP'][K] >= END_TIME :
            END_TIME=END_TIME+TIME_INTERVAL
            COUNTER=COUNTER+1
            VALUE=VALUE+df['TRADE_SIZE'][K]
        
            MEAN_VALUE_0=VALUE/COUNTER
            BOX_MEAN_VALUE.append(MEAN_VALUE_0)
           
          
        
            COUNTER=0
            VALUE=0
            
            
        else :
            COUNTER=COUNTER+1
            VALUE=VALUE+df['TRADE_SIZE'][K]
            


 return  BOX_MEAN_VALUE
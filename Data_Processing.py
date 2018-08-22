# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:23:24 2018

@author: V.Korablov
"""

import pandas as pd 

def Data_Processing (FILE_NAMES,MONEY,TIME_INTERVAL) :
    
 df_X_B=pd.read_csv(FILE_NAMES[1], encoding = "ISO-8859-1")
 df_X_A=pd.read_csv(FILE_NAMES[0], encoding = "ISO-8859-1")

 #df_X_A = df_X_A.sort_values('TIMESTAMP')
 #df_X_B = df_X_B.sort_values('TIMESTAMP')

 #df_X_B.to_csv('sort_test.csv')


 
 """
 rows_list_A=[]
 rows_list_B=[]
 TIME_BOX_A=[]
 TIME_BOX_B=[]

 counter=0;
#for row in input_rows:
 for counter in df['index_col'] :
    frame=df.iloc[counter]
    TIMESTAMP=frame['TIMESTAMP']
    EX_CODE=frame['EX_CODE']
    PAIR=frame['PAIR']
    AB=frame['AB']
    PRICE=frame['PRICE']
    TRADE_SIZE=frame['TRADE_SIZE']
    print(counter)
    dictionary={'TIMESTAMP' : TIMESTAMP,'EX_CODE' : EX_CODE,'PAIR' : PAIR,'AB' : AB ,'PRICE' : PRICE ,'TRADE_SIZE' : TRADE_SIZE}
    
    if PAIR==MONEY :
        if AB=='A': 
            rows_list_A.append(dictionary)
            TIME_BOX_A.append(TIMESTAMP)
        else : 
            rows_list_B.append(dictionary) 
            TIME_BOX_B.append(TIMESTAMP)
    

 df_X_A = pd.DataFrame(rows_list_A)     
 df_X_B = pd.DataFrame(rows_list_B) 
 print('progress - 50%')
 """
 BUY_LIST=[]
 x=0
 PREVIOUS_BUY_PRICE=0
 ALL_BUY_PRICE=0
 ALL_BUY_VALUE=0
 VOLUME_BUY=0

 df=pd.read_csv('train_AD.csv', encoding = "ISO-8859-1")
 df.columns =['TIMESTAMP','EX_CODE','PAIR','AB','PRICE','TRADE_SIZE']
 
 TIME_START=df['TIMESTAMP'][0]
 TIME_END_REAL_A=max(df_X_A['TIMESTAMP'])
 #TIME_END_REAL=max([max(df_X_A['TIMESTAMP']),max(df_X_B['TIMESTAMP'])])
 TIME_END=TIME_START+TIME_INTERVAL
 while TIME_START < TIME_END_REAL_A:
     if TIME_END > TIME_END_REAL_A : TIME_END=TIME_END_REAL_A
     counter_BUY=0
     while df_X_A['TIMESTAMP'][x]<TIME_END :
         counter_BUY=counter_BUY+1
         frame=df_X_A.iloc[x]
         ALL_BUY_PRICE=ALL_BUY_PRICE+frame['PRICE']
         VOLUME_BUY=VOLUME_BUY+frame['TRADE_SIZE']
         ALL_BUY_VALUE=ALL_BUY_VALUE+frame['PRICE']*frame['TRADE_SIZE']
         x=x+1
     if df_X_A['TIMESTAMP'][x]==TIME_END:
         counter_BUY=counter_BUY+1
         frame=df_X_A.iloc[x]
         ALL_BUY_PRICE=ALL_BUY_PRICE+frame['PRICE']
         ALL_BUY_VALUE=ALL_BUY_VALUE+frame['TRADE_SIZE']

     if counter_BUY==0 : 
         MEAN_PRICE=PREVIOUS_BUY_PRICE
         ALL_BUY_VALUE=0
         VOLUME_BUY=0
     else :
         MEAN_PRICE=ALL_BUY_PRICE/counter_BUY
     dictionary={'TIME':TIME_START ,'VALUE' :ALL_BUY_VALUE,'PRICE':MEAN_PRICE,'VOLUME':VOLUME_BUY,'OPTI':counter_BUY }   
     BUY_LIST.append(dictionary)
     PREVIOUS_BUY_PRICE=MEAN_PRICE
     TIME_START=TIME_END
     TIME_END=TIME_END+TIME_INTERVAL
     ALL_BUY_PRICE=0
     ALL_BUY_VALUE=0
     VOLUME_BUY=0
 
 SELL_LIST=[]
 
 x = 0
 
 PREVIOUS_SELL_PRICE=0
 ALL_SELL_PRICE=0
 ALL_SELL_VALUE=0 
 VOLUME_SELL=0
 
 TIME_START=df['TIMESTAMP'][0]
 TIME_END_REAL_B=max(df_X_B['TIMESTAMP'])
 #TIME_END_REAL=max([max(df_X_A['TIMESTAMP']),max(df_X_B['TIMESTAMP'])])
 TIME_END=TIME_START+TIME_INTERVAL
 
 while TIME_START < TIME_END_REAL_B:
     counter_SELL=0
     if TIME_END > TIME_END_REAL_B : 
         TIME_END=TIME_END_REAL_B
     while df_X_B['TIMESTAMP'][x]<TIME_END :
         counter_SELL=counter_SELL+1
         frame=df_X_B.iloc[x]
         ALL_SELL_PRICE=ALL_SELL_PRICE+frame['PRICE']
         ALL_SELL_VALUE=ALL_SELL_VALUE+frame['TRADE_SIZE']
         VOLUME_SELL+=frame['TRADE_SIZE']
         x=x+1
     if df_X_B['TIMESTAMP'][x]==TIME_END:
         counter_SELL=counter_SELL+1
         frame=df_X_B.iloc[x]
         ALL_SELL_PRICE=ALL_SELL_PRICE+frame['PRICE']
         ALL_SELL_VALUE=ALL_SELL_VALUE+frame['TRADE_SIZE']*frame['PRICE']
         VOLUME_SELL+=frame['TRADE_SIZE']
    
     if counter_SELL==0 : 
         MEAN_PRICE=PREVIOUS_SELL_PRICE
         ALL_SELL_VALUE=0
         VOLUME_SELL=0
     else:
         MEAN_PRICE=ALL_SELL_PRICE/counter_SELL
     dictionary={'TIME':TIME_START ,'VALUE' :ALL_SELL_VALUE,'PRICE':MEAN_PRICE,'VOLUME':VOLUME_SELL,'OPTI' : counter_SELL}
     SELL_LIST.append(dictionary)
     PREVIOUS_SELL_PRICE=MEAN_PRICE
     TIME_START=TIME_END
     TIME_END=TIME_END+TIME_INTERVAL
     
     ALL_SELL_PRICE=0
     ALL_SELL_VALUE=0 
     VOLUME_SELL=0
     
 while TIME_END_REAL_B>TIME_END_REAL_A+TIME_INTERVAL-1 :
     MEAN_PRICE=PREVIOUS_BUY_PRICE
     ALL_BUY_VALUE=0
     VOLUME_BUY=0
     dictionary={'TIME':TIME_END_REAL_A ,'VALUE' :ALL_BUY_VALUE,'PRICE':MEAN_PRICE,'VOLUME':VOLUME_BUY,'OPTI':0 }   
     BUY_LIST.append(dictionary)
     TIME_END_REAL_A=TIME_END_REAL_A+TIME_INTERVAL
  
 while TIME_END_REAL_A>TIME_END_REAL_B+TIME_INTERVAL-1 :
     MEAN_PRICE=PREVIOUS_SELL_PRICE
     ALL_SELL_VALUE=0
     VOLUME_SELL=0
     dictionary={'TIME':TIME_END_REAL_B ,'VALUE' :ALL_SELL_VALUE,'PRICE':MEAN_PRICE,'VOLUME':VOLUME_SELL,'OPTI':0 }   
     SELL_LIST.append(dictionary)
     TIME_END_REAL_B=TIME_END_REAL_B+TIME_INTERVAL
 #BUY_FILE='BUY_' + MONEY + '.csv'
 #SELL_FILE='SELL_' + MONEY + '.csv'
 
 BUY_FILE_PTI='PTI_BUY_' + MONEY + 'PER'+str(TIME_INTERVAL)+'.csv'
 SELL_FILE_PTI='PTI_SELL_' + MONEY + 'PER'+str(TIME_INTERVAL)+ '.csv'
 
 FILE_NAMES=[BUY_FILE_PTI,SELL_FILE_PTI]
 
 #df_X_A.to_csv(BUY_FILE)
 #df_X_B.to_csv(SELL_FILE)
 
 SELL_DATA_PTI=pd.DataFrame(SELL_LIST)
 BUY_DATA_PTI=pd.DataFrame(BUY_LIST)
 
 SELL_DATA_PTI.to_csv(SELL_FILE_PTI)
 BUY_DATA_PTI.to_csv(BUY_FILE_PTI)
 
 
 
 return FILE_NAMES
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 11:23:24 2018

@author: V.Korablov
"""

import pandas as pd 


def data_processing(file_names, money, time_interval):
    
 df_buy = pd.read_csv(file_names[1], encoding ="ISO-8859-1")
 df_sell = pd.read_csv(file_names[0], encoding ="ISO-8859-1")

 df_sell = df_sell.sort_values('TIMESTAMP')
 df_buy = df_buy.sort_values('TIMESTAMP')

 buy_list = []
 x = 0
 previous_buy_price = 0
 all_buy_price = 0
 all_buy_value = 0
 volume_buy = 0

 df = pd.read_csv('train_AD.csv', encoding = "ISO-8859-1")
 df.columns = ['TIMESTAMP','EX_CODE','PAIR','AB','PRICE','TRADE_SIZE']
 
 time_start = df['TIMESTAMP'][0]
 time_end_real_sell = max(df_sell['TIMESTAMP'])
 end_time = time_start + time_interval

 while time_start < time_end_real_sell:

     if end_time > time_end_real_sell :
         end_time=time_end_real_sell

     counter_buy = 0

     while df_sell['TIMESTAMP'][x]<end_time :
         counter_buy = counter_buy+1
         frame = df_sell.iloc[x]
         all_buy_price = all_buy_price+frame['PRICE']
         volume_buy = volume_buy+frame['TRADE_SIZE']
         all_buy_value = all_buy_value+frame['PRICE']*frame['TRADE_SIZE']
         x += 1

     if df_sell['TIMESTAMP'][x] == end_time:
         counter_buy += 1
         frame = df_sell.iloc[x]
         all_buy_price = all_buy_price+frame['PRICE']
         all_buy_value = all_buy_value+frame['TRADE_SIZE']

     if counter_buy == 0:
         mean_price = previous_buy_price
         all_buy_value = 0
         volume_buy = 0

     else:
         mean_price = all_buy_price/counter_buy
     dictionary = {'TIME':time_start, 'VALUE': all_buy_value, 'PRICE': mean_price,
                 'VOLUME': volume_buy, 'OPTI': counter_buy }
     buy_list.append(dictionary)
     previous_buy_price = mean_price
     time_start = end_time
     end_time = end_time + time_interval
     all_buy_price = 0
     all_buy_value = 0
     volume_buy = 0
 
 sell_list = []
 
 x = 0
 
 previous_sell_price = 0
 all_sell_price = 0
 all_sell_value = 0
 volume_sell = 0
 
 time_start = df['TIMESTAMP'][0]
 time_end_sell = max(df_buy['TIMESTAMP'])
 end_time = time_start + time_interval
 
 while time_start < time_end_sell:

     counter_sell = 0

     if end_time > time_end_sell:
         end_time = time_end_sell

     while df_buy['TIMESTAMP'][x] < end_time:
         counter_sell += 1
         frame = df_buy.iloc[x]
         all_sell_price = all_sell_price+frame['PRICE']
         all_sell_value = all_sell_value+frame['TRADE_SIZE']
         volume_sell += frame['TRADE_SIZE']
         x+=1

     if df_buy['TIMESTAMP'][x] == end_time:
         counter_sell += 1
         frame = df_buy.iloc[x]
         all_sell_price = all_sell_price+frame['PRICE']
         all_sell_value = all_sell_value+frame['TRADE_SIZE']*frame['PRICE']
         volume_sell += frame['TRADE_SIZE']

     if counter_sell == 0:
         mean_price = previous_sell_price
         all_sell_value = 0
         volume_sell = 0
     else:
         mean_price = all_sell_price/counter_sell

     dictionary = {'TIME':time_start ,'VALUE' :all_sell_value,'PRICE':mean_price,
                 'VOLUME':volume_sell,'OPTI' : counter_sell}
     sell_list.append(dictionary)
     previous_sell_price = mean_price
     time_start = end_time
     end_time = end_time + time_interval
     
     all_sell_price = 0
     all_sell_value = 0
     volume_sell = 0
     
 while time_end_sell > time_end_real_sell + time_interval - 1:
     mean_price = previous_buy_price
     all_buy_value = 0
     volume_buy = 0
     dictionary = {'TIME':time_end_real_sell ,'VALUE' :all_buy_value,
                   'PRICE':mean_price,'VOLUME':volume_buy,'OPTI':0 }
     buy_list.append(dictionary)
     time_end_real_sell = time_end_real_sell + time_interval
  
 while time_end_real_sell >time_end_sell + time_interval - 1:
     mean_price = previous_sell_price
     all_sell_value = 0
     volume_sell = 0
     dictionary = {'TIME':time_end_sell ,'VALUE' :all_sell_value,'PRICE':mean_price,'VOLUME':volume_sell,'OPTI':0 }
     sell_list.append(dictionary)
     time_end_sell = time_end_sell + time_interval

 buy_file_pti = 'PTI_BUY_' + money + '_PER_' + str(time_interval/1000) + 's.csv'
 sell_file_pti = 'PTI_SELL_' + money + '_PER_' + str(time_interval/1000) + 's.csv'
 
 file_names = [buy_file_pti, sell_file_pti]

 sell_data_pti = pd.DataFrame(sell_list)
 buy_data_pti = pd.DataFrame(buy_list)
 
 sell_data_pti.to_csv(sell_file_pti)
 buy_data_pti.to_csv(buy_file_pti)

 return file_names

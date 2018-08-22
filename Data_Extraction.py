import pandas as pd 


def data_extract(file_name, money):
 df = pd.read_csv(file_name, encoding="ISO-8859-1")
 df.columns =['TIMESTAMP', 'EX_CODE', 'PAIR', 'AB', 'PRICE', 'TRADE_SIZE']

 df['index_col'] = df.index

 rows_list_a = []
 rows_list_b = []

# for row in input_rows:

 for counter in df['index_col']:
    frame = df.iloc[counter]
    timestamp = frame['TIMESTAMP']
    ex_code = frame['EX_CODE']
    pair = frame['PAIR']
    ab = frame['AB']
    price = frame['PRICE']
    trade_size = frame['TRADE_SIZE']
    print(counter)
    dictionary = {'TIMESTAMP': timestamp, 'EX_CODE': ex_code, 'PAIR': pair, 'AB': ab, 'PRICE': price,
                  'TRADE_SIZE': trade_size}
    
    if pair == money:
        if ab == 'A':
            rows_list_a.append(dictionary)
        else:
            rows_list_b.append(dictionary)

 df_x_a = pd.DataFrame(rows_list_a)
 df_x_b = pd.DataFrame(rows_list_b)

 buy_file = 'BUY_' + money + '.csv'
 sell_file = 'SELL_' + money + '.csv'

 file_names = [buy_file,sell_file]
 
 df_x_a.to_csv(buy_file)
 df_x_b.to_csv(sell_file)

 return file_names

import pandas as pd 

def Data_Extract (FILE_NAME,MONEY) :
 
 df=pd.read_csv(FILE_NAME, encoding = "ISO-8859-1")
 df.columns =['TIMESTAMP','EX_CODE','PAIR','AB','PRICE','TRADE_SIZE']
 df['index_col'] = df.index

 rows_list_A=[]
 rows_list_B=[]
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
        if AB=='A': rows_list_A.append(dictionary)
        else : rows_list_B.append(dictionary) 
    

 df_X_A = pd.DataFrame(rows_list_A)     
 df_X_B = pd.DataFrame(rows_list_B) 

 BUY_FILE='BUY_' + MONEY + '.csv'
 SELL_FILE='SELL_' + MONEY + '.csv'
 
 FILE_NAMES=[BUY_FILE,SELL_FILE]
 
 df_X_A.to_csv(BUY_FILE)
 df_X_B.to_csv(SELL_FILE)
 
 return FILE_NAMES
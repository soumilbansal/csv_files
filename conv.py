import pandas as pd
from jugaad_data.nse import NSELive
from jugaad_data.nse import stock_df
import pandas as pd
from datetime import date
import datetime

df=pd.read_excel('n50.xlsx')
se=df['Symbol']
for i in range(59,100):
    mysym=se[i]
    print(mysym)
    from_dat = datetime.datetime.now() - datetime.timedelta(days=365)
    from_dat = date(year=from_dat.year, month=from_dat.month, day=from_dat.day)
    to_dat = date.today()
    dff = stock_df(symbol=mysym, from_date=from_dat,to_date=to_dat)
    dff = dff[["DATE","VWAP","VOLUME"]]
    dff.to_csv(mysym+'.csv',index= False)
    print('yaya')
# from_dat = datetime.datetime.now() - datetime.timedelta(days=365)
# from_dat = date(year=from_dat.year, month=from_dat.month, day=from_dat.day)
# dff = stock_df(symbol='ASIANPAINT', from_date=from_dat,to_date=date.today())
# dff = dff[["DATE","VWAP","VOLUME"]]
# dff.to_csv('ASIANPAINT.csv',index= False)
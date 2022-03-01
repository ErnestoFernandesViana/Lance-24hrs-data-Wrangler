#main scrip for wrangling the dataframe
import pandas as pd
from datetime import datetime
import functions as f

for x in range(1,7):
    f.build_df(x)

df1, df2, df3, df4, df5, df6 = [f.wrangling(i) for i in range(1, 7)]

df_new = pd.concat([df1,df2,df3,df4,df5,df6], ignore_index=True)
df_new.to_csv('true_lance.csv')

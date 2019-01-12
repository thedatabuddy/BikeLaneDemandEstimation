import pandas as pd
import json
from pandas.io.json import json_normalize

with open('north_carolina_bicycle_crash_data_json.json') as f:
    d = json.load(f)

#file=pd.read_json("north_carolina_bicycle_crash_data_json.json")

#print(df['fields'][1])
#for i in df.recordid:
#  print(df.i.fields)

#print(df.columns)
geop=json_normalize(d)
geop.set_index('recordid',inplace=True, drop=True)
writer=pd.ExcelWriter('output1.xlsx')
geop.to_excel(writer,'Sheet1')
writer.save()
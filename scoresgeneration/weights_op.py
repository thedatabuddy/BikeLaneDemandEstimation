import pandas as pd
import numpy as np
import pandasql as pdsql
import os
pd.set_option('display.max_columns', 10)

pdquery=lambda q:pdsql.sqldf(q,globals())

data2=pd.read_excel(r'E:\UMKCStudies\Thesis\roadsplit\output_geocodioupdated.xlsx')
data=pdquery("select * from data2 where geocodio_City='Charlotte'")
newdata=pd.DataFrame()

features={}
filenames=[]
directory=r'E:\UMKCStudies\Thesis\features_unique\features'
for filename in os.listdir(directory):
    filenames.append(filename[:-5])
    features[filename[:-5]]=pd.read_excel(directory+'\\'+filename)

for filename in filenames:
    newdata[filename]=data[filename]
newdata['recordid']=data['recordid']
newdata['geocodio_AddressNumber']=data['geocodio_AddressNumber']
newdata['geocodio_Street']=data['geocodio_Street']



for filename in filenames:
    df=pd.DataFrame()
    df=features[filename]
    for i in range(newdata.shape[0]):
        for j in range(df.shape[0]):
            if newdata.loc[i][filename]==df.loc[j]['label']:
                newdata.loc[i,filename]=df.loc[j]['value']

newdata['point_score']=0

for filename in filenames:
    newdata['point_score']=newdata['point_score']+newdata[filename]
print(newdata.head())
writer=pd.ExcelWriter('valuesfile.xlsx')
newdata.to_excel(writer)
writer.save()
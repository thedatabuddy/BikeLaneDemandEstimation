import pandas as pd
import numpy as np
import pandasql as pdsql
import os
from tabulate import tabulate
import time

start=time.time()

pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')

pdquery=lambda q:pdsql.sqldf(q,globals())

data2=pd.read_excel(r'E:\UMKCStudies\Thesis\roadsplit\output_geocodioupdated.xlsx')
data=pdquery("select * from data2 where geocodio_City='Charlotte'")
newdata=pd.DataFrame()

features={}
attributes={}
filenames=[]
for filename in os.listdir(r'E:\UMKCStudies\Thesis\features_unique\features'):
    filenames.append(filename[:-5])
    features[filename[:-5]]=pd.read_excel(r'E:\UMKCStudies\Thesis\features_unique\features'+'\\'+filename)

for filename in os.listdir(r'E:\UMKCStudies\Thesis\score_optimization\woe_calculated'):
    attributes[filename.split('.')[0]] = pd.read_csv(r'E:\UMKCStudies\Thesis\score_optimization\woe_calculated' + '\\' + filename)


for filename in filenames:
    newdata[filename]=data[filename]
newdata['recordid']=data['recordid']
newdata['geocodio_AddressNumber']=data['geocodio_AddressNumber']
newdata['geocodio_Street']=data['geocodio_Street']


for filename in filenames:
    df1=pd.DataFrame()
    df1=features[filename]
    df2=pd.DataFrame()
    df2=attributes[filename]
    for i,newdata_row in newdata.iterrows():
        for j,df1_row in df1.iterrows():
            if newdata_row[filename]==df1_row['label']:
                for k, df2_row in df2.iterrows():
                    if newdata_row[filename]==df2_row[0]:
                        newdata.loc[i,filename]=df1.loc[j]['value']*df2.loc[k]['WoEScore']

for filename in filenames:
    df1=pd.DataFrame()
    df1=features[filename]
    df2=pd.DataFrame()
    df2=attributes[filename]
    for i,newdata_row in newdata.iterrows():
        for j,df1_row in df1.iterrows():
            if newdata_row[filename]==df1_row['label']:
                newdata.loc[i,filename]=df1.loc[j]['value']

# writer=pd.ExcelWriter('valuesfile.xlsx')
# newdata.to_excel(writer)
# writer.save()
newdata.to_csv('valuesfile_2.csv')
print(time.time()-start)
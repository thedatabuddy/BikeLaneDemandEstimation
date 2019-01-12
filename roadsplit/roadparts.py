import pandas as pd
import numpy as np

data=pd.read_excel(r'E:\UMKCStudies\Thesis\roadsplit\minmaxoutput.xlsx',header=0)
data['minstreet']=np.NaN
data['maxstreet']=np.NaN
data['streetstart']=np.NaN
data['streetend']=np.NaN
newdata=pd.DataFrame(columns=['streetname','startstreet','endstreet'])


for i in range(data.shape[0]):
    data.loc[i,'minstreet']=data.iloc[i]['min(geocodio_AddressNumber)']//100
    data.loc[i,'maxstreet'] = data.iloc[i]['max(geocodio_AddressNumber)']//100

for i in range(data.shape[0]):
    data.loc[i, 'streetstart'] = (data.iloc[i]['minstreet'] - (data.iloc[i]['minstreet'] % 10))*100
    data.loc[i, 'streetend']\
        = (data.iloc[i]['maxstreet'] - (data.iloc[i]['maxstreet'] % 10)+10)*100
data=data.replace(0,100)

for i in range(data.shape[0]):
    try:
        l = list(range(int(data.iloc[i]['streetstart']), int(data.iloc[i]['streetend'])+500, 500))
        for j in range(len(l)):
            newdata=newdata.append(pd.DataFrame([[data.iloc[i]['geocodio_Street'],l[j],l[j+1]]],columns=['streetname','startstreet','endstreet']),ignore_index=True)

    except:
        pass

#print(newdata.head())

newdata.to_csv('minmaxstreets.csv',sep=';')
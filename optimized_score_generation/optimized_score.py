import pandas as pd
import os
from tabulate import tabulate

pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')


features=[]
for file in os.listdir(r'E:\UMKCStudies\Thesis\features_unique\features'):
    if file.endswith('.xlsx'):
        features.append(file.split('.')[0])

dataset=pd.read_excel(r'E:\UMKCStudies\Thesis\jsontoxlsx\dataset_updated.xlsx')
segment=pd.read_csv(r'E:\UMKCStudies\Thesis\roadsplit\minmaxstreets.csv')
pointscore=pd.read_csv(r'E:\UMKCStudies\Thesis\scoresgeneration\valuesfile.csv')

segment['road_ids']=[[] for _ in range(len(segment))]
segment['address_nos']=[[] for _ in range(len(segment))]

for feature in features:
    segment[feature]=0
segment['totalscore']=0

for i in range(segment.shape[0]):
    for j in range(pointscore.shape[0]):
        if segment.loc[i]['streetname']==pointscore.loc[j]['geocodio_Street']:
            if segment.loc[i]['startstreet']<=pointscore.loc[j]['geocodio_AddressNumber']<segment.loc[i]['endstreet']:
                for feature in features:
                    segment.at[i, feature] = segment.loc[i][feature] + pointscore.loc[j][feature]
                    segment.at[i, 'totalscore'] = segment.loc[i]['totalscore'] + pointscore.loc[j][feature]
                segment.at[i, 'road_ids'] = segment.loc[i]['road_ids']+[pointscore.loc[j]['recordid']]
                segment.at[i, 'address_nos'] = segment.loc[i]['address_nos']+[pointscore.loc[j]['geocodio_AddressNumber']]


print(pdtabulate(segment.head()))
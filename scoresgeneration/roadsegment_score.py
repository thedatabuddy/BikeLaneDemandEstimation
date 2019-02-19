import pandas as pd
import os
from tabulate import tabulate

pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')

segment=pd.read_csv(r'E:\UMKCStudies\Thesis\roadsplit\minmaxstreets.csv')
pointscore=pd.read_csv(r'E:\UMKCStudies\Thesis\scoresgeneration\valuesfile_2.csv')
yelp_pointscore=pd.read_csv(r'E:\UMKCStudies\Thesis\yelp_score\filtered_chonly.csv')

segment['segment_score']=0.0
segment['yelp_score']=0.0
segment['road_ids']=[[] for _ in range(len(segment))]
segment['address_nos']=[[] for _ in range(len(segment))]
segment['yelp_ids']=[[] for _ in range(len(segment))]
segment['yelp_address_nos']=[[] for _ in range(len(segment))]
segment['accident_count']=0
segment['business_count']=0

features=[]
for file in os.listdir(r'E:\UMKCStudies\Thesis\features_unique\features'):
    if file.endswith('.xlsx'):
        features.append(file.split('.')[0])
for feature in features:
    segment[feature]=0.0

for i in range(segment.shape[0]):
    for j in range(pointscore.shape[0]):
        if segment.loc[i]['streetname']==pointscore.loc[j]['geocodio_Street']:
            if segment.loc[i]['startstreet']<=pointscore.loc[j]['geocodio_AddressNumber']<segment.loc[i]['endstreet']:
                for feature in features:
                    segment.at[i,feature]=segment.loc[i][feature]+pointscore.loc[j][feature]
                segment.at[i, 'road_ids'] = segment.loc[i]['road_ids']+[pointscore.loc[j]['recordid']]
                segment.at[i, 'address_nos'] = segment.loc[i]['address_nos']+[pointscore.loc[j]['geocodio_AddressNumber']]

for i in range(segment.shape[0]):
    for j in range(yelp_pointscore.shape[0]):
        if segment.loc[i]['streetname'] == yelp_pointscore.loc[j]['gc_Street']:
            if segment.loc[i]['startstreet'] <= yelp_pointscore.loc[j]['gc_Number'] < segment.loc[i]['endstreet']:
                segment.at[i, 'yelp_score'] = segment.loc[i]['yelp_score'] + yelp_pointscore.loc[j]['stars']
                segment.at[i, 'yelp_ids'] = segment.loc[i]['yelp_ids']+[yelp_pointscore.loc[j]['business_id']]
                segment.at[i, 'yelp_address_nos'] = segment.loc[i]['yelp_address_nos']+[yelp_pointscore.loc[j]['gc_Number']]

for i in range(segment.shape[0]):
    segment.at[i,'accident_count'] = len(segment.loc[i]['road_ids'])
    segment.at[i,'business_count'] = len(segment.loc[i]['yelp_ids'])
for feature in features:
    segment['segment_score']+=segment[feature]
segment['segment_score']+=segment['yelp_score']

# writer=pd.ExcelWriter('calc_segmentscore.xlsx')
# segment.to_excel(writer)
# writer.save()
# segment.to_csv('calc_segmentscore.csv')

segment.to_csv('calc_segmentscore_optimized.csv')
print(pdtabulate(segment))
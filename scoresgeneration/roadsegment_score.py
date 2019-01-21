import pandas as pd

segment=pd.read_csv(r'E:\UMKCStudies\Thesis\roadsplit\minmaxstreets.csv')
pointscore=pd.read_csv(r'E:\UMKCStudies\Thesis\scoresgeneration\valuesfile.csv')
yelp_pointscore=pd.read_csv(r'E:\UMKCStudies\Thesis\yelp_score\filtered_chonly.csv')

segment['segment_score']=0
segment['road_ids']=[[] for _ in range(len(segment))]
segment['address_nos']=[[] for _ in range(len(segment))]
segment['yelp_ids']=[[] for _ in range(len(segment))]
segment['yelp_address_nos']=[[] for _ in range(len(segment))]

for i in range(segment.shape[0]):
    for j in range(pointscore.shape[0]):
        if segment.loc[i]['streetname']==pointscore.loc[j]['geocodio_Street']:
            if segment.loc[i]['startstreet']<=pointscore.loc[j]['geocodio_AddressNumber']<segment.loc[i]['endstreet']:
                segment.at[i,'segment_score']=segment.loc[i]['segment_score']+pointscore.loc[j]['point_score']
                segment.at[i, 'road_ids'] = segment.loc[i]['road_ids']+[pointscore.loc[j]['recordid']]
                segment.at[i, 'address_nos'] = segment.loc[i]['address_nos']+[pointscore.loc[j]['geocodio_AddressNumber']]

for i in range(segment.shape[0]):
    for j in range(yelp_pointscore.shape[0]):
        if segment.loc[i]['streetname'] == yelp_pointscore.loc[j]['gc_Street']:
            if segment.loc[i]['startstreet'] <= yelp_pointscore.loc[j]['gc_Number'] < segment.loc[i]['endstreet']:
                segment.at[i, 'segment_score'] = segment.loc[i]['segment_score'] + yelp_pointscore.loc[j]['stars']
                segment.at[i, 'yelp_ids'] = segment.loc[i]['yelp_ids']+[yelp_pointscore.loc[j]['business_id']]
                segment.at[i, 'yelp_address_nos'] = segment.loc[i]['yelp_address_nos']+[yelp_pointscore.loc[j]['gc_Number']]


# writer=pd.ExcelWriter('calc_segmentscore.xlsx')
# segment.to_excel(writer)
# writer.save()
segment.to_csv('calc_segmentscore.csv')
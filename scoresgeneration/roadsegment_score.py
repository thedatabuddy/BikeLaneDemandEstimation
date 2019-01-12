import pandas as pd

segment=pd.read_csv(r'E:\UMKCStudies\Thesis\roadsplit\minmaxstreets.csv',engine='python')
pointscore=pd.read_csv(r'E:\UMKCStudies\Thesis\scoresgeneration\valuesfile.xlsx',engine='python')

segment['segment_score']=0
segment['road_ids']=[[] for _ in range(len(segment))]
segment['address_nos']=[[] for _ in range(len(segment))]

for i in range(segment.shape[0]):
    for j in range(pointscore.shape[0]):
        if segment.loc[i]['geocodio_Street']==pointscore.loc[j]['geocodio_Street']:
            if segment.loc[i]['startstreet']<=pointscore.loc[j]['geocodio_AddressNumber']<segment.loc[i]['endstreet']:
                segment.loc[i,'segment_score']=segment.loc[i]['segment_score']+pointscore.loc[j]['point_score']
                segment.loc[i, 'road_ids'] = segment.loc[i]['road_ids'].append(pointscore.loc[j]['recordid'])
                segment.loc[i, 'address_nos'] = segment.loc[i]['address_nos'].append(pointscore.loc[j]['geocodio_AddressNumber'])

writer=pd.ExcelWriter('calc_segmentscore.xlsx')
segment.to_excel(writer)
writer.save()
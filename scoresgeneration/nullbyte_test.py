# data = open(r'E:\UMKCStudies\Thesis\scoresgeneration\valuesfile.csv', 'rb').read()
# print(data.find(b'\x00'))
# print(data.count(b'\x00'))

import pandas as pd
pd.set_option('display.max_columns', 500)
segment=pd.read_csv(r'E:\UMKCStudies\Thesis\roadsplit\minmaxstreets.csv')
segment['road_ids']=[['hello'] for _ in range(len(segment))]



segment.at[1,'road_ids']=segment.loc[1]['road_ids']+(['hello'])

print(segment.head())

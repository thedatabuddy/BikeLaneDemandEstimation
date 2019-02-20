import pandas as pd
from tabulate import tabulate
import os
import ast
import time

start=time.time()

pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')

def BagofWords(a):
    preprocessed_documents = []
    for i in a:
        preprocessed_documents.append(i.split('*'))

    frequency_list = []

    from collections import Counter

    for i in preprocessed_documents:
        frequency_counts = Counter(i)
        frequency_list.append(frequency_counts)
    return(pd.DataFrame(frequency_list).fillna(0).astype(int))


features=[]
for file in os.listdir(r'E:\UMKCStudies\Thesis\features_unique\features'):
    if file.endswith('.xlsx'):
        features.append(file.split('.')[0])

segments=pd.read_csv(r'E:\UMKCStudies\Thesis\scoresgeneration\normalized_scores_optimized.csv')
dataset=pd.read_excel(r'E:\UMKCStudies\Thesis\features_unique\dataset_updated.xlsx')

listed_variables=['road_ids','address_nos','yelp_ids','yelp_address_nos']

for variable in listed_variables:
    segments[variable] = segments[variable].apply(ast.literal_eval)

segments['allattributes']=""
for i,segment_row in segments.iterrows():
    for j, dataset_row in dataset.iterrows():
        for k in segment_row['road_ids']:
            if k==dataset_row['recordid']:
                for feature in features:
                    segments.loc[i,'allattributes']=segments.loc[i]['allattributes']+dataset_row[feature]+'*'

bag=BagofWords(segments['allattributes'])
print(pdtabulate(segments))
print(pdtabulate(bag))
bag.to_csv('bagofwords_output.csv')
segments.to_csv('segments_withallattributes.csv')
print(time.time()-start)
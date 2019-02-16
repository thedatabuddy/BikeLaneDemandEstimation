import pandas as pd
import numpy as np
import os
from tabulate import tabulate

pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')

def WoE(non_event_count,non_event_total_count,event_count,event_total_count):
    return((np.log((non_event_count/non_event_total_count)/(event_count/event_total_count))*100))

features=[]
for file in os.listdir(r'E:\UMKCStudies\Thesis\features_unique\features'):
    if file.endswith('.xlsx'):
        features.append(file.split('.')[0])

non_event_count=7060
event_count=407

for feature in features:
    df=pd.read_csv(r'E:\UMKCStudies\Thesis\score_optimization\feature_counts_merged\\'+feature+'.csv',index_col=0)
    df['WoEScore']=WoE(df['wolane'],non_event_count,df['wlane'],event_count)
    df.to_csv(r'E:\UMKCStudies\Thesis\score_optimization\woe_calculated\\'+feature + '.csv')


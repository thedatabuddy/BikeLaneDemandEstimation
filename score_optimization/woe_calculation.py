import pandas as pd
import numpy as np
import os
from tabulate import tabulate
import plotly.plotly as py
import plotly.graph_objs as go
import plotly


pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')

def WoE(non_event_count,non_event_total_count,event_count,event_total_count):
    return((np.log((non_event_count/non_event_total_count)/(event_count/event_total_count))*100)*(non_event_count+event_count))

features=[]
for file in os.listdir(r'E:\UMKCStudies\Thesis\features_unique\features'):
    if file.endswith('.xlsx'):
        features.append(file.split('.')[0])

non_event_count=7060
event_count=407

for feature in features:
    df=pd.read_csv(r'E:\UMKCStudies\Thesis\score_optimization\feature_counts_merged\\'+feature+'.csv',index_col=0)
    df['WoEScore']=WoE(df['wolane'],non_event_count,df['wlane'],event_count)
    df=df.sort_values('WoEScore')
    df=df.clip(lower=0)
    df['WoEScore']=1-(df['WoEScore']-df['WoEScore'].min())/(df['WoEScore'].max()-df['WoEScore'].min())
    print(pdtabulate(df))
    data = [go.Bar(x=df.reset_index()['index'],y=df['WoEScore'])]
    plotly.offline.plot(data, filename='graph_'+feature+'.html')
    df.to_csv(r'E:\UMKCStudies\Thesis\score_optimization\woe_calculated\\'+feature + '.csv')
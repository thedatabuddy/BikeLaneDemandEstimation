import pandas as pd
from tabulate import tabulate

pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')

input=pd.read_csv(r'E:\UMKCStudies\Thesis\ml_algorithm_2\segments_withallattributes.csv')

input=input.drop(columns=['Unnamed: 0','Unnamed: 0.1','Unnamed: 0.1.1','Unnamed: 0.1.1.1'])

input.loc[(input['norm_score']>=0) & (input['norm_score']<2.5),'label']="Not Required"
input.loc[(input['norm_score']>=2.5) & (input['norm_score']<5),'label']="Not Necessary"
input.loc[(input['norm_score']>=5) & (input['norm_score']<7.5),'label']="Needed"
input.loc[input['norm_score']>=7.5,'label']="Definitely Needed"

input.to_csv('input_with_classes.csv')
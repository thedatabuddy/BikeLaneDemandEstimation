import os
import pandas as pd
from tabulate import tabulate

pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')

features=[]
for file in os.listdir(r'E:\UMKCStudies\Thesis\features_unique\features'):
    if file.endswith('.xlsx'):
        features.append(file.split('.')[0])

dataset=pd.read_excel(r'E:\UMKCStudies\Thesis\features_unique\dataset_updated.xlsx',index_col=0)

wlane=dataset.loc[dataset['bikepos']=='Bike Lane / Paved Shoulder']
wolane=dataset.loc[dataset['bikepos']!='Bike Lane / Paved Shoulder']

for feature in features:
    df1=pd.DataFrame(wlane[feature].value_counts())
    df1.columns = ['wlane']
    df2=pd.DataFrame(wolane[feature].value_counts())
    df2.columns = ['wolane']
    full_df=pd.DataFrame(wolane[feature].value_counts())
    final_df=df1.join(df2,lsuffix='wlane', rsuffix='wolane',how='outer')
    final_df=final_df.replace(0,pd.np.nan).dropna(axis=0, how='any')
    print(pdtabulate(final_df))
    final_df.to_csv(r'E:\UMKCStudies\Thesis\score_optimization\feature_counts_merged\\'+feature + '.csv')

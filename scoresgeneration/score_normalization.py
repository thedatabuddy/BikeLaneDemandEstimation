import pandas as pd
from tabulate import tabulate

pdtabulate=lambda df:tabulate(df,headers='keys',tablefmt='psql')

inpfile=pd.read_csv(r'E:\UMKCStudies\Thesis\scoresgeneration\calc_segmentscore.csv')

max_business_count=2
max_accident_count=2
max_score_per_accident_feature=5
max_rating_per_business=5

inpfile['norm_score']=(inpfile['segment_score']/((max_business_count*max_rating_per_business)+(max_accident_count*max_score_per_accident_feature*9)))*10

for i in range(inpfile.shape[0]):
    if inpfile.loc[i]['norm_score']>10:
        inpfile.at[i, 'norm_score']=10.0

inpfile.to_csv('normalized_scores.csv')
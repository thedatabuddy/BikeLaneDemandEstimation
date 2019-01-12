import pandas as pd
import numpy as np
import pandasql as pdsql

pd.set_option('display.max_columns',50)

data=pd.read_excel(r'E:\UMKCStudies\Thesis\features_postgres\dataset_updated.xlsx')

attr='ambulancer bikedir bikeinjury bikepos crashgrp crashloc crashtype development drvrinjury'.split()

for i in attr:
    d=pd.DataFrame(data[i].unique())
    d[1]=np.NaN
    d.columns=['label','value']
    d.to_excel('features\\'+i+'.xlsx',index=False)
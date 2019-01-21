import pandas as pd
import pandasql as pdsql
from tabulate import tabulate

tabdf=lambda df:tabulate(df,headers="keys",tablefmt="psql")
pquery=lambda q : pdsql.sqldf(q,globals())

df=pd.read_csv(r'E:\UMKCStudies\Thesis\geocodio_yelpop\chonlyyelp_geocodio.csv')

dfslice=pquery("select business_id,stars,gc_number,gc_street,review_count from df where review_count > 100")
# dfslice=df.loc[df["review_count"]>100,["business_id","stars","gc_number","gc_street","review_count"]]
dfslice.to_csv('filtered_chonly.csv')
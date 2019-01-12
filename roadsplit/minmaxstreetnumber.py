import pandas as pd
import pandasql as pdsql
import uuid
import numpy as np

data=pd.read_excel(r'E:\UMKCStudies\Thesis\roadsplit\output_geocodioupdated.xlsx')

pysql = lambda q: pdsql.sqldf(q, globals())
data["geocodio_AddressNumber"]=pd.to_numeric(data["geocodio_AddressNumber"])

query=pysql("select min(geocodio_AddressNumber),max(geocodio_AddressNumber),geocodio_Street from data where geocodio_city='Charlotte' group by geocodio_Street")
# size=query.shape[0]
# query['streetid']=np.NaN
# for i in range(size):
#     query.loc[i,'streetid']=str(uuid.uuid4())
query.to_excel('minmaxoutput.xlsx')
import pandas as pd
from haversine import haversine

f = open("silimarstreetdistance.csv", "a")
inp=pd.read_excel('output_geocodiofull.xlsx',index_col=[0])

chonly=inp.loc[inp['geocodio.City']=='Charlotte']
df_similar=pd.DataFrame({'id1':[],'id2':[],'distance':[]})

for i,rowi in chonly.iterrows():
    for j,rowj in chonly.iterrows():
        if rowi['geocodio.Street']==rowj['geocodio.Street']:
            distance = haversine([rowi['geocodio.Latitude'], rowi['geocodio.Longitude']], [rowj['geocodio.Latitude'], rowj['geocodio.Longitude']],miles=True)
            #print(i,j,distance)
            f.write(i+';'+j+';'+str(distance)+'\n')



#inp.loc[[i], "lat"]
#print(chonly['geocodio.City'].head())
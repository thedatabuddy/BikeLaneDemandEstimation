import pandas as pd
from haversine import haversine

inp=pd.read_excel('nearestdistance_in.xlsx',index_col=[0])
x=0

for i in inp.index:
     for j in inp.index:
         distance=haversine([inp.loc[[i],"lat"],inp.loc[[i],"lon"]],[inp.loc[[j],"lat"],inp.loc[[j],"lon"]], miles=True)
         if distance<=10:
             inp.loc[[i],"nearestoccurences"]+=1
             print(inp.loc[[i]])
             print(inp.loc[[j]])
             x+=1
             print(x)

writer=pd.ExcelWriter('nearestdistance_out.xlsx')
inp.to_excel(writer,"Sheet1")
writer.save()
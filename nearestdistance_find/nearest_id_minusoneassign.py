import pandas as pd

flatexp=pd.read_excel('output.xlsx',index_col=[0])
slice=pd.DataFrame(flatexp['fields.geo_shape.coordinates'])
slice1=slice.rename(columns={"fields.geo_shape.coordinates":"coordinates"})

for i in slice1.index:
    val = slice1["coordinates"].loc[i].strip("[").strip("]").split(', ')
    fval=[float(j) for j in val]
    slice1.loc[[i],"lat"]=fval[0]
    slice1.loc[[i],"lon"] = fval[1]

slice1["nearestoccurences"]=-1

writer=pd.ExcelWriter('nearestdistance_in.xlsx')
slice1.to_excel(writer,"Sheet1")
writer.save()
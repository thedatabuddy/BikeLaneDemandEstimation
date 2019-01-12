import pandas as pd

inp=pd.read_json("yelp_academic_dataset_business.json", lines=True)

chlist=['Char','Charlotte','CHARLOTTE','Charlotte NC','charlotte']

chonly=inp[inp.city.isin(chlist)]

writer=pd.ExcelWriter('yelp_chonly.xlsx')
chonly.to_excel(writer,"Sheet1")
writer.save()
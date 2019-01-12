import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_excel(r'E:\UMKCStudies\Thesis\yelp_filtered\yelp_chonly.xlsx',index_col=3)

plt.hist(list(data.loc[:,'review_count']),range=(0,1800),bins=20)
plt.title('Rating count distribution Histogram')
plt.xlabel('rating_count')
plt.ylabel('no. of ratings')
plt.xticks(list(range(0, 1800, 90)))
plt.grid(True)
plt.show()
#print(list(data.loc[:,'review_count']))
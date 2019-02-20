import pandas as pd

an=['A','A', 'B', 'C', 'D', 'A*A', 'C*C*']
a=pd.DataFrame(an)
a[0]=a[0].str.rstrip('*')
def BagofWords(a):
    preprocessed_documents = []
    for i in a:
        preprocessed_documents.append(i.split('*'))

    frequency_list = []

    from collections import Counter

    for i in preprocessed_documents:
        frequency_counts = Counter(i)
        frequency_list.append(frequency_counts)
    return(pd.DataFrame(frequency_list).fillna(0).astype(int))
print(a)
print(BagofWords(a[0]))
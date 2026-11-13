import pandas as pd
import numpy as np

data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']}

df=pd.DataFrame(data1)
print(df)


# print(df.groupby('Name').groups)
# #to print the first entries of the group
# gk=df.groupby('Name').first()
# print(gk)

#grouping data with multiple keys

# df.groupby(['Name', 'Qualification'])
# print(df.groupby(['Name', 'Qualification']).groups)

#grouping data by sorting keys

# print(df.groupby('Name')['Age'].sum())

#single keys
# grp= df.groupby('Name')
# for name, group in grp:
#     print(name)
#     print(group)
#     print()

#multiple keys

# grp=df.groupby(['Name', 'Qualification'])
# for  name, group in grp:
#     print(name)
#     print(group)
#     print()

#selecting a group

# grp=df.groupby('Name')
# print(grp.get_group('Jai'))

#multiple columns

# grp=df.groupby(['Name','Qualification'])
# print(grp.get_group(('Jai','Msc')))


grp1=df.groupby(['Name', 'Qualification'])
print(grp1['Age'].aggregate(np.sum))

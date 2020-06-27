# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data = pd.read_csv(path)
#print(data['Rating'].isnull())
#print(data['Rating'].value_counts())
plt.hist(data['Rating'].dropna())
print(data.shape)
data= data[data['Rating']<=5]
print(data.shape)
plt.hist(data['Rating'].dropna())
#Code ends here


# --------------
import numpy as np
# code starts here
total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())*100
missing_data = pd.concat([total_null,percent_null],keys = ['Total','Percent'],
axis = 1)
print(missing_data)
data.dropna(inplace = True)
total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())*100
missing_data_1 = pd.concat([total_null_1,percent_null_1],keys = ['Total','Percent'],
axis = 1)
print(missing_data_1)
# code ends here


# --------------

#Code starts here
g = sns.catplot(x='Category',y='Rating',data = data, kind = 'box', height = 10)
#g.set_titles('Rating vs Category (BoxPlot)')
#g.set_
#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print(data['Installs'].value_counts())
#print(data.info())
data['Installs'] = data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].str.replace('+','')
data['Installs'] = pd.to_numeric(data['Installs'])
le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
sns.regplot(x = 'Installs',y = 'Rating',data=data)
plt.title('Rating vs Install [RegPlot]')
#Code ends here



# --------------
#Code starts here
#data['Price'].value_counts()
data['Price'] = data['Price'].str.replace('$','').astype(dtype = np.float64)
#print(data['Price'].value_counts())
sns.regplot(x = 'Price',y = 'Rating',data = data)
plt.title('Rating vs Price [RegPlot]')
#Code ends here


# --------------

#Code starts here
#print(data['Genres'].unique())
Genres_1= data['Genres'].str.split(';',expand = True)
data['Genres'] = Genres_1[0]
gr_mean = data[['Genres','Rating']].groupby(['Genres'],as_index = False).agg('mean')
gr_mean = gr_mean.sort_values(by = 'Rating')
print(gr_mean.iloc[[0,-1]])
print(gr_mean.describe())
#Code ends here


# --------------

#Code starts here
#print(data['Last Updated'])
data['Last Updated'] = pd.to_datetime(data['Last Updated'])
max_date = data['Last Updated'].max()
print(max_date)
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days 
#print(data['Last Updated Days'])
sns.regplot(x='Last Updated Days', y='Rating', data = data)
plt.title('Rating vs Last Updated Days [RegPlot]')
#Code ends here



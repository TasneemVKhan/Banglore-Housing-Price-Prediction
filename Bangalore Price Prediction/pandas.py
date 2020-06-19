# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 13:29:39 2020

@author: ADIL KHAN
"""

''' Data Frames '''
#  Data Frame 
#     - Spl Case of list which has each component of equal length 
#     - Each component forms column and content forms row 



import pandas as pd
      



# Reading a data file

df = pd.read_csv("RegularSeasonCompactResults.csv")


# Summary of data
d = df.describe()   

# No of rows
len(df)         

# Column names
df.columns      

# Specifies data types
df.dtypes       

#to check top 5 rows of data set
df.head()

#to check last 5 rows of data set
df.tail()



#to check maximum values
df.max()

#to check maximum value of Specific column
df['Wscore'].max()


#to find mean of specific column data
df['Lscore'].mean()


'''Acessing Values'''


df.iloc[:3]  

df.iloc[1:3]  1  2  

df.iloc[3]

''' Sorting '''


 c= df.sort_values('Lscore')


''' Filtering Rows Conditionally '''

df[df['Wscore'] > 150]

df[(df['Wscore'] > 150) & (df['Lscore'] < 100)]


''' Grouping '''

df.groupby('Wteam')['Wscore'].mean()


# Converting to list
b = df.columns.tolist()  



''' Extracting Rows and Columns '''


df[['Wscore', 'Lscore']].head()

df.loc[:, ['Wscore', 'Lscore']]


''' Data Cleaning '''

import numpy as np

df1 = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1],
                  [np.nan, np.nan, 4, 5]],
                  columns=list('ABCD'))

df1.isnull().sum()


#Drop the columns where all elements are nan:

df1.dropna(axis=1, how='all')

#Drop the columns where any of the elements is nan
df1.dropna(axis=0, how='any')

#Drop the rows where all of the elements are nan
df1.dropna(axis=0, how='all')

#Keep only the rows with at least 2 non-na values:
df1.dropna(thresh=1)



''' Fill the data '''

#Replace all NaN elements with 0s.
df1.fillna(8)

#We can also propagate non-null values forward or backward.

df1.fillna(method='bfill')

df2=df1.fillna(df1.mean())
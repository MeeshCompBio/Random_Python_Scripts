'''General examples of using pandas'''

import pandas as pd
import numpy as np
# Make a basic pandas series
Series = pd.Series([1,3,5,np.nan,6,8])

# Make a basic pandas dataframe
people = ['Chad', 'Mahfuz', 'Meesh', 'Henri', 'Xiaotong']
df = pd.DataFrame(np.random.randn(5,4), index=people, columns=list('ABCD'))

#####
# Useful built in functions
#####
# type of data in each column
df.dtypes

#return row names
df.index

# return column names
df.columns

# return only the values in the dataframe
df.values

# Top ten lines of dataframe
df.head()

# Basic statistics on the data
df.describe()

#####
# Slicing and indexing
#####

# First two rows
df[:2]

# column a and b 
df[['A','B']]

# numerical indexing
# First three rows of columns A through C 
df.iloc[0:3,0:2]

# Label based indexing
# First three rows of columns A through C 
df.loc["Chad":"Meesh",'A':'C']

# Return the third row as a list
df[2:3]
df[2:3]
df[2:3].values.tolist()
df[2:3].values.flatten().tolist()



#####
# Manipulating dataframes
#####

# Adding a column on the end
E = pd.Series(np.random.randn(5))
df['E'] = E.values

Skeletor = pd.DataFrame(np.random.randn(1,5), index=['Skeletor'], columns=df.columns)

df = df.append(Skeletor)

#Swapping column values
df[['B', 'A']] = df[['A', 'B']]


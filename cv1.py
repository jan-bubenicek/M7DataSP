# I just want to say at the begining, that I have a lot experience with R,
# but this is my first atempt to do something in Python.

#%% import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%% data
# train.csv needs to be in working directory.
data = pd.read_csv("train.csv")
# First of all we need to read description on Kaggle and open loaded DataFrame.
# We can see data about 1460 houses. There are 79 explanatory variables (house
# setting). In the last column there is outcome - selling price of the house.
# Data looks complete. 
data
na_sum = data.isnull().sum()
# Here we can see, in which columns is NULL value. Mostly it seems, that's not
# mistake. I would be a bit suspicious about column Electrical, where is just
# one NULL row.

#%%
desc = data.describe()
desc.plot.box()
plt.show()
# Here we can see, that there are two columns which maximum exceeds a lot. 
# It may not mean anything, but its worth exploring
plt.boxplot(data['SalePrice'])
plt.show()
plt.boxplot(data['LotArea'])
plt.show()
# We can see, that there are just 4 properties, which lot area exceed 10000.

#%%
data_except = data.drop(['SalePrice', 'LotArea'], axis = 1)
data_except.plot.box()
# Here are again some attributes that are more variable than others. 
# It would be important to scale them all, because we have some which goes to
# the big numbers and on the other hand we have some that are just 0/1 variables.

#%%
# Now we can take a look on some interestring 2 dimensional plots
sns.relplot(x='LotArea',y='SalePrice',data=data)
sns.relplot(x='YearBuilt',y='SalePrice',data=data)
sns.relplot(x='YearRemodAdd',y='SalePrice',data=data)

#%%
cor_matrix = data.corr()
# Corelation matrix in that amount of variables looks bit messy, but if we 
# use colored version, we can see some strong corelations, for example:
# SalePrice X OverallQual
# SalePrice X GrLivArea
# GarageCars X SalePrice

# Just because of that easy exploratory analysis we see, that there are a lot
# of corelations, which shouldn't be surprise when there are 80 variables.
# It seems that data are complete, where is 'NaN' value, it tells us something
# about the house.
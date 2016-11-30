# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:00:00 2016

@author: ADalton
"""
# 1.	Create a list named my_list in python with the following data points - 
# 45.4 44.2 36.8 35.1 39.0 60.0 47.4 41.1 45.8 35.6
my_list = [45.4,44.2,36.8,35.1,39.0,60.0,47.4,41.1,45.8,35.6]
my_list
# 1a.	Print the 5th element in the list
# Since array is 0 based, item 4 is the 5th element
my_list[4]
# 1b.	Append 55.2 to my_list
my_list.append(55.2)
# 1c.	Remove the 6th element in the list
my_list.pop(5)
# 1d.	Iterate over the list to print data points greater than 45
[x for x in my_list if x > 45]

# 2.	Introduction to numpy – 
# 2a.	Import the numpy library using the following command – import numpy
import numpy
# 2b.	Declare numpy array with the same data points as in my_list using numpy.array()
npArray = numpy.array([45.4,44.2,36.8,35.1,39.0,60.0,47.4,41.1,45.8,35.6])
# 2c.	Compute the mean and standard deviation using numpy.mean() and numpy.std() of the above array
numpy.mean(npArray)
numpy.std(npArray)
# 2d.	Use logical referencing to get only those values that are less than 45
[x for x in npArray if x < 45]
# 2e.	Compute the max and min of the array using numpy.max() and numpy.min()
numpy.max(npArray)
numpy.min(npArray)

# 3.	Introduction to pandas – 
# 3a.	Import the pandas library – import pandas
import pandas
# 3b.	Read the IRIS dataset into iris using pandas.read_csv().
iris = pandas.read_csv('c:\datasets\iris.csv')  
# 3c.	Using iris.head(), display the head of the dataset
iris.head()
# 3d.	Use DataFrame.drop() to drop the id column
iris = iris.drop('Id', axis=1)
# 3e.	Subset dataframe to create a new data frame that includes only the measurements for the setosa species
newIris = iris.loc[iris['Species'] == 'Iris-setosa']
# 3f.	Use DataFrame.describe() to get the summary statistics
iris.describe()
# 3g.	Use DataFrame.groupby() to create grouped data frames by Species and compute summary statistics using DataFrame.describe()
iris.groupby('Species').describe()
# 3h.	Use DataFrame.boxplot() to plot boxplots by Species
iris.groupby('Species').boxplot()
# 3i.	Plot a scatter matrix plot using the seaborn library. Use the following to load and plot 
import seaborn as sns
sns.pairplot(iris,hue='Species')
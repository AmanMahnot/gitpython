# -*- coding: utf-8 -*-
"""
Created on Thu May 24 10:48:09 2018

@author: user
"""

#Import Python Libraries

import pandas as pd

#Read csv file
df= pd.read_csv("Salaries.csv")

#List first 5 records
df.head()

#Try to read the first 10, 20, 50 records;
#Can you guess how to view the last few records;

df.tail()

#Check types for all the columns
df.dtypes
df.columns #list the column names
df.axes #list the row labelsand column names
df.ndim   #number of dimensions
df.size #number of elements
df.shape #return a tuplerepresenting the dimensionality
df.values #numpyrepresentation of the data

df.describe() #generate descriptive statistics (for numeric columns only)

df.max() #return max/minvalues for all numeric columns
df.min()

df.mean()
df.median()
df.std()

df.sample(10) #returns a random sample of thedata frame

#What are the mean values of the first 50 records in the dataset?
df.head(50).mean()

"""
Selecting a column in a Data Frame
Method 1: Subset the data frame using column name:
df['sex']
Method 2: Use the column name as an attribute:
df.sex
Note:there is an attribute rankfor pandas data frames, 
so to select a column with a name "rank" we should use method 1.
"""

df['rank']
df.phd

#calculate the basic statstics on the salary column
df['salary'].mean()
df['salary'].describe()

#Find how many values in the salarycolumn (use countmethod);
df['salary'].count()

#calculate the avg salary
print df['salary'].mean()

"""
Data Frames groupbymethod
26
Using "group by" method we can:
•Split the data into groups based on some criteria
•Calculate statistics (or apply a function) to each group
•Similar to dplyr() function in R

"""
#Group data using rank
df_rank= df.groupby(['rank'])

#Calculate mean value for each numeric column per each group
df_rank.mean()

#Calculate mean salary for each professor rank:
df.groupby('rank')[['salary']].mean()

"""
Important
Note:If single brackets are used to specify the column (e.g. salary), 
then the output is Pandas Series object. 
When double brackets are used the output is a Data Frame
"""
df.groupby('rank')[["salary"]].mean()

"""
groupbyperformance notes:
-no grouping/splitting occurs until it's needed. 
Creating the groupby object only verifies that you have passed 
a valid mapping
-by default the group keys are sorted during the 
groupby operation. You may want to pass sort=False 
for potential speedup:
"""
#Calculate mean salary for each professor rank:
df.groupby(['rank'],sort=False)[['salary']].mean()

"""
Data Frame: filtering
29
To subset the data we can apply Boolean indexing. 
This indexing is commonly known as a filter. 
For example if we want to subset the rows in which the salary
 value is greater than $120K:
"""
#Calculate mean salary for each professor rank:
df_sub= df[df['salary'] > 120000 ]

#Select only those rows that contain female professors:
df_f= df[df['sex'] == 'Female' ]

"""
Data Frames: Slicing

When selecting one column, it is possible to use single set of 
brackets, but the resulting object will be a Series (not a DataFrame)


When we need to select more than one column and/or make the 
output to be a DataFrame, we should use double brackets

"""

#Select column salary:
df['salary']
df["salary"]

#Select column salary:
df[['rank','salary']]

"""
Data Frames: method loc
33
If we need to select a range of rows, using their labels 
we can use method loc
"""
df_sub.loc[10:20,['rank','sex','salary']]

"""
Data Frames: method iloc

If we need to select a range of rows and/or columns, 
using their positions we can use method iloc
"""
df_sub.iloc[10:20,[0, 3, 4, 5]]
df.iloc[0] # First row of a data frame

df.iloc[-1] # Last row

df.iloc[:, 0] # First column

df.iloc[:, -1] # Last column

df.iloc[0:7] #First 7 rows

df.iloc[:, 0:2] #First 2 columns

df.iloc[1:3, 0:2] #Second through third rows and first 2 columns

df.iloc[[0,5], [1,3]] #1stand 6throws and 2ndand 4thcolumns

"""
DataFrame sorting
"""

# Create a new data frame from the original sorted by the column Salary
df_sorted= df.sort_values( by='service')
df_sorted.head()

#We can sort the data using 2 or more columns:
df_sorted= df.sort_values( by=['service','salary'], ascending = [True,True])
df_sorted.head(10)

df_sorted= df.sort_values( by=['service','salary'], ascending = [True,False])
df_sorted.head(10)


"""
Missing Values

Missing values are marked as NaN
"""

# Read a dataset with missing values
salary = pd.read_csv("Salaries.csv")

# Select the rows that have at least one missing value
salary[salary.isnull().any(axis=1)].head()

#select the rows with all values NaN
salary[salary.isnull()].head()

#There are a number of methods to deal with missing values in the data frame:
salary.dropna()

"""
dropna(how='all') >> Drop observations where all cells is NA
dropna(axis=1, how='all') >> Drop column if all the values aremissing
dropna(thresh = 5) >> Drop rows that contain less than 5 non-missing values
fillna(0) >> Replace missing values with zeros
isnull() >> returns True if the value is missing
notnull() >> Returns True for non-missing values

More notes:
    Missing Values

•When summing the data, missing values will be treated as zero
•If all values are missing, the sum will be equal to NaN
•cumsum() and cumprod() methods ignore missing values but 
preserve them in the resulting arrays
•Missing values in GroupBymethod are excluded (just like in R)
•Many descriptive statistics methods have skipnaoption to control 
if missing data should be excluded . This value is set to True by 
default (unlike R)

"""

salary = pd.read_csv("Salaries.csv")

# fill the record having missing values, with mean of that column
salary['salary'] = salary['salary'].fillna(salary['salary'].mean())

# fill all the records having missing values, with mean of that column
salary = salary.fillna(salary.mean())

#agg() method are useful when multiple statistics are computed per column:
salary[['service','salary']].agg(['min','mean','max'])
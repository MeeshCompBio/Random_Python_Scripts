# CSCI 3003 Lecture
# Introduction to python packages

## What is a Python package, module or library?
* Modules are file containing Python definitions and statements
* A package is a directory of Python modules
* Unlike other languages, libraries are a very loose term in Python. They typically refer to a core set of modules.

### How to install and use a module/package
* You can put all of your python definitions in a different file to call on later
    * You would typically do this so you don't have to copy and paste the same code across files/scripts

### Your first Python Module
* Take this simple function for instance
```python
# Simple function to say Hello n number of times
def Hello(n):
    while n > 0:
        print("Hi")
        n -= 1
```
If we save it as a python file called SayHello.py, we will be able to call on it later using other scripts or within an IDE.

Open up your favorite python IDE lets test out our new function (Make sure you are in the same directory as your python function file)
```bash
# Open up ipython or your favorite python IDE
 ipython
```
Now within Python
```python
# import the module
In [4]: import SayHello
# call the function within the module
In [5]: SayHello.Hello(3)
Hi
Hi
Hi
```
The resulting output will a "Hi" on each line with repect to the nuber used in the function
## Installing python packages
There are multiple ways to install a python package, but the most popular method is to use pip
```bash
# To install a ptyhon package from the command line
pip install numpy

```
Keep in mind that this method does install packages across all versions of python. To specify a specific version you can use the python module command.
```bash
python3.6 -m pip install numpy
```
This will ensure that numpy is installed a s a package for python3.6. Here are some popular pip commands to help you with package management.
```bash
# Install a package
pip install <package_name>
# Upgrade a package
pip install --upgrade <package_name>
# Remove a package
pip uninstall <package_name>
# Show current version of all installed packages
pip freeze
```

## Numpy
Numpy stands for numerical python. It is very fast and efficient at numerical calculations and supports large multidemtional arrays and matrices. It is faster and more memoery efficient than basic Python, but can only store one data type in an array.
### Basic numpy examples
```python
# make sure to import numpy
import numpy as np

# Traditional python array
base_Array = [0, 1, 2, 3]
# creating our first numpy array
np_Array = np.array([0, 1, 2, 3])
```
Numpy arrays also have built in functions that are faster. Say that we want to calculate the mean of the array
```python
# This would be the normal python way
sum(base_Array)/len(base_Array)
# 625 ns to run command

# This is the numpy built in function
Array.mean()
# 12.6 µs to run command, way faster
```

Two-dimensional array and indexing
```python
# Create a 2D array
TwoD = np.array([[0, 1, 2], [3, 4, 5]])
In [18]: TwoD.ndim
Out[18]: 2
In [19]: TwoD.shape
Out[19]: (2, 3)
```
Index operations on the array
```python
#Grab everything up to the first row
In [20]: TwoD[:1]
Out[20]: array([[0, 1, 2]])
# Grab everything after the first row
In [21]: TwoD[1:]
Out[21]: array([[3, 4, 5]])
# Select a specific column
In [22]: TwoD[:,[1]]
Out[22]:
array([[1],
       [4]])
```
Generating data for arrays
```python
# produce a sequence of numbers from 0 up to 5 at spacing 0.2
In [2]: np.arange(0, 5, 0.2)
Out[2]:
array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4,
       2.6, 2.8, 3. , 3.2, 3.4, 3.6, 3.8, 4. , 4.2, 4.4, 4.6, 4.8])

# produce a sequence of numbers from 0 to 100 at spacing 0.1
np.arange(0,100,0.1)

# make an empty matrix
In [5]: np.zeros([5,5])
Out[5]:
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])

# return standard normal distribution for 10 x 10 array
In [6]: np.random.randn(5,5)
Out[6]:
array([[ 1.00435574,  0.0061684 ,  0.95088423, -2.34454893, -1.15037774],
       [ 1.20254388,  0.25431958,  0.08901913,  0.08221421,  1.17821403],
       [-1.42777859, -0.33667732,  0.85823388,  0.60718726, -0.32063143],
       [ 1.01338441, -0.30382252, -0.2234927 ,  0.93903844,  0.69062427],
       [ 0.28339266, -0.9301785 , -1.23130615, -0.6422832 , -0.57835214]])
```
Operations on arrays
```python
# Two dimentional array
TwoD = np.array([[0, 1, 2], [3, 4, 5]])

# Perform operations on the entire array
plusone = TwoD + 1
In [9]: plusone
Out[9]:
array([[1, 2, 3],
       [4, 5, 6]])

# Square the matrix
squared = TwoD**2
In [11]: squared
Out[11]:
array([[ 0,  1,  4],
       [ 9, 16, 25]])

# Modify part of the array
TwoD[:1] = TwoD[:1]+10
In [13]: TwoD
Out[13]:
array([[10, 11, 12],
       [ 3,  4,  5]])
```

## Pandas
Python pandas is a data analysis library that is suited for a variety of data types. Unlike numpy it can handle a variety of data types, it is an important part of the statistical ecosystem, and is used extensively in commercial applications.
```python
import pandas as pd
import numpy as np

# Make a basic pandas series
Series = pd.Series([1,3,5,np.nan,6,8])
In [17]: Series
Out[17]:
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64

# Make a basic pandas dataframe
people = ['Chad', 'Mahfuz', 'Meesh', 'Henri', 'Xiaotong']
df = pd.DataFrame(np.random.randn(5,4), index=people, columns=list('ABCD'))
In [20]: df
Out[20]:
                 A         B         C         D
Chad     -1.719822 -0.295213  0.164352 -0.374377
Mahfuz   -0.258308 -0.258635  2.123565 -0.056291
Meesh    -0.512175  0.546413 -0.759366 -1.228470
Henri    -1.256220 -1.400962 -0.650755  1.121592
Xiaotong  0.294646  0.728671  1.515158 -0.895310
```
Useful built-in functions
```python
# type of data in each column
In [21]: df.dtypes
Out[21]:
A    float64
B    float64
C    float64
D    float64
dtype: object

#return row names
In [22]: df.index
Out[22]: Index(['Chad', 'Mahfuz', 'Meesh', 'Henri', 'Xiaotong'], dtype='object')

# return column names
In [23]: df.columns
Out[23]: Index(['A', 'B', 'C', 'D'], dtype='object')

# return only the values in the dataframe
In [24]: df.values
Out[24]:
array([[-1.7198224 , -0.29521261,  0.16435153, -0.37437715],
       [-0.25830798, -0.25863496,  2.12356467, -0.05629145],
       [-0.51217547,  0.54641257, -0.75936572, -1.22847028],
       [-1.25621989, -1.40096194, -0.65075532,  1.12159178],
       [ 0.29464627,  0.72867147,  1.51515816, -0.89531042]])

# Top ten lines of dataframe
df.head()

# Basic statistics on the data
In [27]: df.describe()
Out[27]:
              A         B         C         D
count  5.000000  5.000000  5.000000  5.000000
mean  -0.690376 -0.135945  0.478591 -0.286572
std    0.801350  0.844669  1.292973  0.908488
min   -1.719822 -1.400962 -0.759366 -1.228470
25%   -1.256220 -0.295213 -0.650755 -0.895310
50%   -0.512175 -0.258635  0.164352 -0.374377
75%   -0.258308  0.546413  1.515158 -0.056291
max    0.294646  0.728671  2.123565  1.121592
```
Slicing and indexing
```python
# First two rows
In [28]: df[:2]
Out[28]:
               A         B         C         D
Chad   -1.719822 -0.295213  0.164352 -0.374377
Mahfuz -0.258308 -0.258635  2.123565 -0.056291

# column a and b 
In [29]: df[['A','B']]
Out[29]:
                 A         B
Chad     -1.719822 -0.295213
Mahfuz   -0.258308 -0.258635
Meesh    -0.512175  0.546413
Henri    -1.256220 -1.400962
Xiaotong  0.294646  0.728671

# numerical indexing
# First three rows of columns A through C 
In [30]: df.iloc[0:3,0:2]
Out[30]:
               A         B
Chad   -1.719822 -0.295213
Mahfuz -0.258308 -0.258635
Meesh  -0.512175  0.546413

# Label based indexing
# First three rows of columns A through C 
In [31]: df.loc["Chad":"Meesh",'A':'C']
Out[31]:
               A         B         C
Chad   -1.719822 -0.295213  0.164352
Mahfuz -0.258308 -0.258635  2.123565
Meesh  -0.512175  0.546413 -0.759366
```

Progression of turning in pandas dataframe to python list
```python
In [32]: df[2:3]
Out[32]:
              A         B         C        D
Meesh -0.512175  0.546413 -0.759366 -1.22847

# pulling out values
In [33]: df[2:3].values
Out[33]: array([[-0.51217547,  0.54641257, -0.75936572, -1.22847028]])

# Return a list of lists
In [34]: df[2:3].values.tolist()
Out[34]:
[[-0.512175469092307,
  0.5464125657957694,
  -0.7593657158866708,
  -1.2284702755127868]]
df[2:3].values.flatten().tolist()

# Flatten out to a single list
In [35]: df[2:3].values.flatten().tolist()
Out[35]:
[-0.512175469092307,
 0.5464125657957694,
 -0.7593657158866708,
 -1.2284702755127868]
```
Manipulating dataframes
```python
# Adding a column on the end of the data frame
E = pd.Series(np.random.randn(5))
df['E'] = E.values
In [38]: df
Out[38]:
                 A         B         C         D         E
Chad     -1.719822 -0.295213  0.164352 -0.374377  0.043171
Mahfuz   -0.258308 -0.258635  2.123565 -0.056291 -0.280208
Meesh    -0.512175  0.546413 -0.759366 -1.228470  0.672247
Henri    -1.256220 -1.400962 -0.650755  1.121592  1.559458
Xiaotong  0.294646  0.728671  1.515158 -0.895310 -0.456347

# Add a row
Skeletor = pd.DataFrame(np.random.randn(1,5), index=['Skeletor'], columns=df.columns)
df = df.append(Skeletor)
In [41]: df
Out[41]:
                 A         B         C         D         E
Chad     -1.719822 -0.295213  0.164352 -0.374377  0.043171
Mahfuz   -0.258308 -0.258635  2.123565 -0.056291 -0.280208
Meesh    -0.512175  0.546413 -0.759366 -1.228470  0.672247
Henri    -1.256220 -1.400962 -0.650755  1.121592  1.559458
Xiaotong  0.294646  0.728671  1.515158 -0.895310 -0.456347
Skeletor  0.720206 -0.932789  1.264533 -0.398572  1.824843

#Swapping column values
df[['B', 'A']] = df[['A', 'B']]
In [43]: df
Out[43]:
                 A         B         C         D         E
Chad     -0.295213 -1.719822  0.164352 -0.374377  0.043171
Mahfuz   -0.258635 -0.258308  2.123565 -0.056291 -0.280208
Meesh     0.546413 -0.512175 -0.759366 -1.228470  0.672247
Henri    -1.400962 -1.256220 -0.650755  1.121592  1.559458
Xiaotong  0.728671  0.294646  1.515158 -0.895310 -0.456347
Skeletor -0.932789  0.720206  1.264533 -0.398572  1.824843
```

## Scipy
Scipy is a scientific and numerical tools for python. The majority of its code is written in C or Fortran. It contains a larger variety of numerical algorithms wrapped up into modules
```python
import numpy as np
#You can't just import scipy, you need to specify a module
from scipy import stats

# Generate a numpy array
a = np.array([ 0.7972,  0.0767,  0.4383,  0.7866,  0.8091,
               0.1954, 0.6307, 0.6599,  0.1065,  0.0508])

#check the mean of a to see what z-score of 0 would be
In [46]: a.mean()
Out[46]: 0.45511999999999986

# convert to z-scores
In [47]: stats.zscore(a)
Out[47]:
array([ 1.12724554, -1.2469956 , -0.05542642,  1.09231569,  1.16645923,
       -0.8558472 ,  0.57858329,  0.67480514, -1.14879659, -1.33234306])
```

## Matplotlib
Matplitlib is a library for making plots in python (over 200k lines of code). Its philosophy centers around the idea that anyone should be able to create simple plots with very few lines of code.
```python
import matplotlib.pyplot as plt
import numpy as np

# simple figure
#Set up x,y values
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
#label the y axis
plt.ylabel('some numbers')
# show the plot
plt.show()

# Add some decoration
# ro stands for red circles
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
# set the axis you want to see
plt.axis([0, 6, 0, 20])
plt.show()

# plot three items as a time
# generate data from to to 5 with 0.2 values increments
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# Histogram
x = np.random.randn(100000)
# data, number of bins, color
fig = plt.hist(x, 200,  facecolor="g")
plt.show()

# Barplot 
# Plot a barplot showing nucleotide frequencies
bases = ["A","G","C","T"]
# y_pos needs to be a numpy array
y_pos = np.arange(len(bases))
freqs = np.array([0.1, 0.4, 0.25, 0.25])
plt.bar(bases,freqs,align="center")
plt.show()
```

# Introduction to python packages (for CSCI 3003 Lecture)

##What is a Python package, module or library?
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

Index operations on the array
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
test = np.arange(0, 5, 0.2)

# produce a sequence of numbers from 0 to 100 at spacing 0.1
a = np.arange(0,100,0.1)

# make an empty matrix
Zeros = np.zeros([100,100]) 

# return standard normal distribution for 10 x 10 array
x = np.random.randn(10,10)

# operations on arrays

# Two dimentional array
TwoD = np.array([[0, 1, 2], [3, 4, 5]])

# Perform operations on the entire array
plusone = TwoD + 1

# Square the matrix
squared = TwoD**2

# Modify part of the array
TwoD[:1] = TwoD[:1]+10
```
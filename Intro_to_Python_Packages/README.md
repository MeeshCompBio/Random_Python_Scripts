# Introduction to python packages

## How to install and use a module/package
* You can put all of your python definitions in a defferent files to call on later
    * You would typically do this so you don't have to copy and paste the same code across files

### Your first Python Module
* Take this simple function for instance
```python
# Simple function to say Hello n number of times
def Hello(n):
    while n > 0:
        print("Hi")
        n -= 1
```
If we save it as a python file called SayHello.py, we will be able to call on it later using other scripts or a Python IDE

Open up your favorite python IDE lets test out our new function (Make sure you are in the same directory as your python function file)
```bash ipython```
```python
# import the module
import SayHello
# call the function within the module
SayHello.Hello(3)
```
The resulting output will a "Hi" on each line with repect to the nuber used in the function
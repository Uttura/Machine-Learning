import numpy as np
print(np.__version__)

## Creating an arrag using numpy

arr = np.array([1,2,3,4,5]) #using list for creating the numpy array
arr_T = np.array((1,2,3,4,5))#using tuple for creating the numpy array
#0 dimension array or 0-D array
arr_0 = np.array(42)
## uni-Dimensional array or 1-D array
arr = np.array([1,2,3,4,5])
## 2-dimensional array, represent second order tensor
arr = np.array([[1,2,3,4,5],[2,3,4,5,6]])
## 3-dimensional array , represent third order tensor
arr = np.array([[[1,2,3,4],[5,6,7,8]],[[2,3,4,5],[2,3,5,6]]])
print(arr)
# Checking the dimesnions of the array using the attribute ndim
print(arr.ndim)
# parameters ndmin can be used to set the dimensions of the given array
arr = np.array([1,2,3,4],ndmin=4)
print(arr)
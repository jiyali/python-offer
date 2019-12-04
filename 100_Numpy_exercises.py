# 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np


# 2. Print the numpy version and the configuration (★☆☆)
print(np.__version__)
np.show_config()


# 3. Create a null vector of size 10 (★☆☆)
print(np.zeros(10))


# 4.  How to find the memory size of any array (★☆☆)
Z = np.zeros((10, 10))
print(Z)
print("%d bytes" % (Z.size * Z.itemsize))


# 5.  How to get the documentation of the numpy add function from the command line? (★☆☆)
print(np.info(np.add))


# 6.  Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
Z = np.zeros(10)
Z[4] = 1
print(Z)


# 7.  Create a vector with values ranging from 10 to 49 (★☆☆)
print(np.arange(10, 50))


# 8.  Reverse a vector (first element becomes last) (★☆☆)
Z = np.arange(50)
print(Z[::-1])


# 9.  Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
print(np.arange(9).reshape(3, 3))


# 10. Find indices of non-zero elements from \[1,2,0,0,4,0\] (★☆☆)
print(np.nonzero([1, 2, 0, 0, 4, 0]))


# 11. Create a 3x3 identity matrix (★☆☆) 单位矩阵
print(np.eye(3))


# 12. Create a 3x3x3 array with random values (★☆☆)
print(np.random.random((3, 3, 3)))


# 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
Z = np.random.random((10, 10, 10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)


# 14. Create a random vector of size 30 and find the mean value (★☆☆)
Z = np.random.random(30)
Zmean = Z.mean()
print(Zmean)


# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
Z = np.ones((10, 10))
Z[1:-1, 1:-1] = 0
print(Z)


# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)
Z = np.random.random((5, 5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)


# 17. What is the result of the following expression? (★☆☆)
print(0 * np.nan)  # nan
print(np.nan == np.nan)  # False
print(np.inf > np.nan)  # False
print(np.nan - np.nan)  # nan
print(np.nan in set([np.nan]))  # False
print(0.3 == 3 * 0.1)  # False


# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
"""
[[0 0 0 0 0]
 [1 0 0 0 0]
 [0 2 0 0 0]
 [0 0 3 0 0]
 [0 0 0 4 0]]
"""
print(np.diag(1+np.arange(4), k=-1))


# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
Z = np.zeros((8, 8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)


# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
print(np.unravel_index(99, (6, 7, 8)))


# 21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
Z = np.tile([[0, 1], [1, 0]], (4, 4))
print(Z)


# 22. Normalize a 5x5 random matrix (★☆☆)
Z = np.random.random((5, 5))
Z = (Z - np.mean(Z)) / (np.std(Z))
print(Z)


# 23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
color = np.dtype([("r", np.ubyte, 1), ("g", np.ubyte, 1), ("b", np.ubyte, 1), ("a", np.ubyte, 1)])
print(color)


# 24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
Z = np.dot(np.ones((5, 3)), np.ones((3, 2)))
print(Z)
Z1 = np.ones((5, 3)) @ np.ones((3, 2))
print(Z1)


# 25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)


# 26. What is the output of the following script? (★☆☆)
print(sum(range(5), -1))  # 计算总和后再加-1
from numpy import *
print(sum(range(5), -1))  # axis=0是按列求和,axis=1 是按行求和


# 27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
Z = np.ones(10)
print(Z**Z)
print(Z < - Z)
print(1j*Z)
print(Z/1/1)


# 28. What are the result of the following expressions?
print(np.array(0) / np.array(0))  # nan
print(np.array(0) // np.array(0))  # 0
print(np.array([np.nan]).astype(int).astype(float))  # [-2.14748365e+09]


# 29. How to round away from zero a float array ? (★☆☆) 四舍五入
Z = np.random.uniform(-10, +10, 10)
print(Z)
print(around(Z))


# 30. How to find common values between two arrays? (★☆☆)



#### 31. How to ignore all numpy warnings (not recommended)? (★☆☆)



#### 32. Is the following expressions true? (★☆☆)


#### 33. How to get the dates of yesterday, today and tomorrow? (★☆☆)



#### 34. How to get all the dates corresponding to the month of July 2016? (★★☆)



#### 35. How to compute ((A+B)\*(-A/2)) in place (without copy)? (★★☆)



#### 36. Extract the integer part of a random array using 5 different methods (★★☆)



#### 37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)



#### 38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)



#### 39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)



#### 40. Create a random vector of size 10 and sort it (★★☆)



#### 41. How to sum a small array faster than np.sum? (★★☆)



#### 42. Consider two random array A and B, check if they are equal (★★☆)



#### 43. Make an array immutable (read-only) (★★☆)



#### 44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)



#### 45. Create a random vector of size 10 and replace the maximum value by 0 (★★☆)



#### 46. Create a structured array with `x` and `y` coordinates covering the \[0,1\]x\[0,1\] area (★★☆)



####  47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))



#### 48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)



#### 49. How to print all the values of an array? (★★☆)



#### 50. How to find the closest value (to a given scalar) in a vector? (★★☆)
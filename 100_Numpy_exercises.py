# 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

# 2. Print the numpy version and the configuration (★☆☆)
print(np.__version__)
np.show_config()

# 3. Create a null vector of size 10 (★☆☆)
print(np.zeros(10))

# 4.  How to find the memory size of any array (★☆☆)
Z = np.zeros((10, 10))
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
print(np.diag(1+np.arange(4), k=-1))

# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
Z = np.zeros((8, 8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)

# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
print(np.unravel_index(99, (6, 7, 8)))

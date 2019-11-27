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

# 11. Create a 3x3 identity matrix (★☆☆)


# 12. Create a 3x3x3 array with random values (★☆☆)


# 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)


# 14. Create a random vector of size 30 and find the mean value (★☆☆)


# 15. Create a 2d array with 1 on the border and 0 inside (★☆☆)


# 16. How to add a border (filled with 0's) around an existing array? (★☆☆)


# 17. What is the result of the following expression? (★☆☆)


# 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)


# 19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)


# 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?

# implements the examples on the Matrix Math page in the Samantha wiki
# https://github.com/voyc/samantha/wiki/Matrix-Math

import numpy as np

# do not use these python types
np.array([1,2])  # does not support matrix math
np.ndarray([1,2])  # works, but matrix() is better

# data types
x = 3;  # scalar
v = np.matrix([1,2,3,4])  # vector
A = np.matrix([[1,2],[3,4]])  # matrix

# element-wise multiplication of two same-size matrices
A = np.matrix([[1,2],[3,4]])
B = np.matrix([[5,7],[6,4]])
np.multiply(A, B)

# element-wise addition of vector and matrix
C = np.matrix([1,2])
C + B

# element-wise multiplication of scalar and matrix
2 * B

# matrix multiplication
D = np.matrix([[2,1],[4,2]])
B * D

# another matrix multiplication
E = np.matrix([[5,7],[6,4],[3,2]])
F = np.matrix([[2,1,3,2],[4,2,1,5]])
E * F

# matrix transpose
G = np.matrix([[1,2,3],[4,5,6]])
np.transpose(G)

# identity matrix
np.identity(3)   # create a 3x3 identity matrix

# matrix inversion
C = np.matrix([[3,4,8],[2,16,4],[4,2,9]])  # create a square matrix
C
CV = np.linalg.inv(C)   # invert it
CV
C * CV    # multiply the matrix times its inverse, giving the Identity matrix

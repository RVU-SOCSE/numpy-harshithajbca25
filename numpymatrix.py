import numpy as np

# Create two matrices
A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10, 11, 12]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# 1. Matrix Addition
addition = A + B
print("\nMatrix Addition (A + B):")
print(addition)

# 2. Matrix Multiplication
# For multiplication, number of columns in A must equal rows in B
# So we reshape B for valid multiplication
B_reshaped = np.array([[7, 8],
                       [9, 10],
                       [11, 12]])

multiplication = np.dot(A, B_reshaped)
print("\nMatrix Multiplication (A x B):")
print(multiplication)

# 3. Transpose of a matrix
transpose_A = A.T
print("\nTranspose of Matrix A:")
print(transpose_A)

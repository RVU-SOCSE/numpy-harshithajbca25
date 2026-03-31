import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:")
print(arr)

# Reshape the array (2 rows, 3 columns)
reshaped_arr = arr.reshape(2, 3)
print("\nReshaped Array (2x3):")
print(reshaped_arr)

# Indexing examples
print("\nAccessing elements using indexing:")
print("Element at position [0][1]:", reshaped_arr[0][1])  # row 0, column 1
print("First row:", reshaped_arr[0])
print("Second column:", reshaped_arr[:, 1])

# Calculate the sum of elements
total_sum = np.sum(arr)
print("\nSum of all elements:", total_sum)

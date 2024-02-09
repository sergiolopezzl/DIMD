import numpy as np

def calculate_vector_projection(A, B):
    # Calculate the dot product of A and B
    dot_product = np.dot(A, B)

    # Calculate the magnitude of B
    magnitude_B = np.linalg.norm(B)

    # Calculate the square of the magnitude of B
    magnitude_B_squared = magnitude_B ** 2

    # Calculate the projection using the projection formula
    projection = (dot_product / magnitude_B_squared) * B

    return projection

# Example usage
A = np.array([3, 4])
B = np.array([5, 12])
projection = calculate_vector_projection(A, B)
print(projection)

A = np.array([10, 20, 30])
B = np.array([4, 9, 16])
projection = calculate_vector_projection(A, B)
print(projection)
import math

def rotate_vector_2d(x, y, alpha):
    # Calculate the rotation matrix
    rotation_matrix = [
        [math.cos(alpha), -math.sin(alpha)],
        [math.sin(alpha), math.cos(alpha)]
    ]

    # Multiply the rotation matrix by the original vector
    rotated_vector = [
        sum(r * c for r, c in zip(rotation_matrix[i], (x, y)))
        for i in range(2)
    ]

    return rotated_vector

# Example usage
x, y = 3, 4
alpha = math.radians(45)
rotated_vector = rotate_vector_2d(x, y, alpha)
print(rotated_vector)

x, y = 1, 0
alpha = math.radians(90)
rotated_vector = rotate_vector_2d(x, y, alpha)
print(rotated_vector)

x, y = 0, 1
alpha = math.radians(180)
rotated_vector = rotate_vector_2d(x, y, alpha)
print(rotated_vector)
# Define matrices A and B
A = [[1, 2], [3, 4]]
B = [[5], [6]]

# Function to compute outer product
def outer_product_matrices(A, B):
    m = len(A)
    p = len(A[0])
    q = len(B)
    n = len(B[0])
    result = [[0] * (n * p) for _ in range(m * q)]

    for i in range(m):
        for j in range(p):
            for k in range(q):
                for l in range(n):
                    result[i*q + k][j*n + l] = A[i][j] * B[k][l]

    return result

# Compute outer product
outer_product_result_matrices = outer_product_matrices(A, B)

# Display result
print("Outer Product of Matrices (From Scratch):")
for row in outer_product_result_matrices:
    print(row)
import numpy as np

A = np.array([
    [2, 0],
    [0, 3]
])

# Eigenvalues & Eigenvectors
eig_values, eig_vectors = np.linalg.eig(A)

print("Eigenvalues:", eig_values)
print("Eigenvectors:\n", eig_vectors)




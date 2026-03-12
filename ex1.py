import numpy as np
import timeit

sample_A = np.random.randint(1, 10, (2,2))
sample_B = np.random.randint(1, 10, (2,2))

# Item A)
def mat_prod(A: np.matrix, B: np.matrix) -> np.matrix:
    m, k = A.shape
    n = B.shape[1]
    C = np.zeros((m, n))
    
    for i in range(m):
        for j in range(n):
            for p in range(k):
                C[i, j] += A[i, p]*B[p, j]           

    return C

# Shapes for test
A_sps = ((2,10),(15,10),(6,10),(500, 10), (500, 500), (400, 500))
B_sps = ((10,5),(10,2),(10,6),(10, 300), (500, 500), (500, 500))

# Function for measure the time of item B, C and D
def time_measure(function):
    print(function.__name__, ": \n")
    for shape_a, shape_b in zip(A_sps, B_sps):
        A = np.random.randint(0,1000, shape_a)
        B = np.random.randint(0,1000, shape_b)

        # heating
        function(A, B)

        tempo = timeit.timeit(lambda: function(A, B), number=3)
        print(tempo)
    print()

# Item B)
# time_measure(mat_prod)

# Item C)
def mat_prod_dot(A, B):
    m = A.shape[0]
    n = B.shape[1]
    C = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
                C[i, j] += np.dot(A[i], B[:,j])

    return C

time_measure(mat_prod_dot)

# Item D)
time_measure(np.matmul)

import numpy as np
import timeit
from time import perf_counter, perf_counter_ns

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
A_shps = ((1,1), (2,10),(15,10),(6,20),(500, 113), (500, 500), (400, 500), (1000, 1000))
B_shps = ((1,1), (10,5),(10,2),(20,6),(113, 300), (500, 500), (500, 500), (1000, 1000))
times = (10000, 9000, 8000, 7000, 10, 10, 10, 2)

data = {"A":[], "B":[], "times": times}

for shape_a, shape_b in zip(A_shps, B_shps):
        A = np.random.randint(0,1000, shape_a)
        B = np.random.randint(0,1000, shape_b)

        data["A"].append(A)
        data["B"].append(B)

# Function for measure the time of item B, C and D
def time_matrix_product_measure(function):
    print(function.__name__, ": \n")
    
    for A, B, times in zip(data["A"], data["B"], data["times"]):

        # heating
        function(A, B)

        #time
        time = []

        for _ in range(times):
            inicio = perf_counter_ns()
            function(A, B)
            fim = perf_counter_ns()

            # calculamos o tempo agregado para depois fazer uma media
            time.append(fim - inicio)

        print("dp:", np.std(time), "m:", sum(time)/times)
        
    print()

# Item B)
#time_matrix_product_measure(mat_prod)

# Item C)
def mat_prod_dot(A, B):
    m = A.shape[0]
    n = B.shape[1]
    C = np.zeros((m, n))

    for i in range(m):
        for j in range(n):
                C[i, j] += np.dot(A[i], B[:,j])

    return C

# time_matrix_product_measure(mat_prod_dot)

# Item D)
# time_matrix_product_measure(np.matmul)

C = np.array([2,4,6,8])
A = np.array([1,2,3,4])
B = np.array([3,7,9,0])


def solve_tridiag(A:np.ndarray, b:np.ndarray) -> np.ndarray:
    """resolve um sistema tridiagonal

    Parameters
    ----------
    A : np.ndarray
        Uma matriz quadrada invertivel
    b : np.ndarray
        resultado que queremos chegar

    Returns
    -------
    np.ndarray
        solução do sistema
    """
    A_c = [A[0]]


    for i in range(1, len(A), 1):
         a_i = A[i] - (C[i]/A_c[i-1])*B[i-1]
         A_c.append(a_i)

    print(A_c)



solve_tridiag(A, B)
         



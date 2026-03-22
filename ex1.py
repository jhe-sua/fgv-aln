import numpy as np
from time import perf_counter, perf_counter_ns
import matplotlib.pyplot as plt

sample_A = np.random.randint(1, 10, (2,2))
sample_B = np.random.randint(1, 10, (2,2))

# Questão 1
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

# funcao para medir o tempo do item B, C, D
def time_matrix_product_measure(function):
    print(function.__name__, ": \n")
    
    for A, B, times in zip(data["A"], data["B"], data["times"]):

        # esquentamento
        function(A, B)

        # tempo
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


# Questã0 2

# Item A)
def solve_tridiag(A:np.ndarray, b:np.ndarray) -> np.ndarray:
    """resolve um sistema tridiagonal que não produz 0's na eliminacao

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

    u = A.diagonal(1)
    d = A.diagonal()
    l = A.diagonal(-1)

    size = len(d)
    d_c = [d[0]]
    b_c = [b[0]]

    # Eliminação abaixo
    for i in range(size-1):
        di_c = d[i+1] - (l[i]/d_c[i])*u[i]
        d_c.append(di_c)
        
        bi_c = b[i+1] - (l[i]/d_c[i])*b_c[i]
        b_c.append(bi_c)

    # Substituicao
    x = np.zeros(size)

    # Primeira
    x[size -1] = (b_c[size -1])/d_c[size -1]

    # Restantes
    for i in range(size - 2, -1, -1):
        x[i] = (b_c[i] - u[i]*x[i+1])/d_c[i]

    return x

# Item B)
# Para verificar se a funcao esta correta soluciono com np e calculo o erro

def gerar_tridiagonal(n):

    # diagonais inferior e superior
    l = np.random.randint(1, 3, size=n-1)
    u = np.random.uniform(1, 3, size=n-1)
    
    # diagonal principal
    d = np.abs(l) + np.abs(u)

    # ajusta tamanho
    d = np.append(d, np.abs(l[-1]) + 1)

    # garante que não sejam gerados 0's na eliminacao
    d = d + 1
    
    A = np.diag(d) + np.diag(u, k=1) + np.diag(l, k=-1)
    return A

def gerar_b(n):
    b = np.random.uniform(1, 3, size=n)
    return b

# gerar matrizes e b's de tamanho 2, 3, 4, ..., 100
matrizes = []
bs = []

for n in range(2, 501):
    A = gerar_tridiagonal(n)
    b = gerar_b(n)

    matrizes.append(A)
    bs.append(b)

# Calcular erro
# for cada_matriz, cada_b in zip(matrizes, bs):
#     err = np.linalg.solve(cada_matriz, cada_b) - solve_tridiag(cada_matriz, cada_b)
#     err = err * err
#     numeric_err = np.sum(err)
#     print(numeric_err)

# Item C)
"""
Complexidade O(n) pois qualquer linha de codigo se repete no maximo x vezes
"""

# Item D)

#Funcao para medir tempo
def measure_time(function):
    def wrap(*args, **kwargs):
        #esquentamento
        function(*args, **kwargs)
        function(*args, **kwargs)
        function(*args, **kwargs)
        function(*args, **kwargs)


        inicio = perf_counter()
        function(*args, **kwargs)
        fim = perf_counter()

        return fim - inicio
    return wrap

shapes = [n for n in range(2, 501)]
tempos_eu = [measure_time(solve_tridiag)(A,b) for A, b in zip(matrizes, bs)]
tempos_np = [measure_time(np.linalg.solve)(A,b) for A, b in zip(matrizes, bs)]

fig, ax = plt.subplots()

ax.plot(shapes, tempos_eu, label="Tempo solve_tridiag")
ax.plot(shapes, tempos_np, label="Tempo numpy")
ax.legend()
ax.grid()

plt.savefig("teste1.png")








         



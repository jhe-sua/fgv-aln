import numpy as np
import pandas as pd
from time import perf_counter

################################ Questão 1 - A ################################

def mat_prod(A: np.matrix, B: np.matrix) -> np.matrix:
    m, n = A.shape
    _, p = B.shape
    C = np.zeros((m, p))
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i, j] = A[i, k]*B[k, j]           

    return C

################################ Questão 1 - B ################################
# temos 3 classes de teste e em cada categoria de teste 2 tipos de teste
# então ao total realizaremos 6 testes e mediremos seus tempos

def medir_tempo(func, *args, repeat=10):
    tempos = []
    for _ in range(repeat):
        inicio = perf_counter()
        func(*args)
        fim = perf_counter()
        tempos.append(fim - inicio)
    return np.mean(tempos)


def test_prod(m,k,n, func):
    np.random.seed(42)
    A = np.random.randn(m, k)
    B = np.random.randn(k, n)

    # Esquentamento
    mat_prod(A, B)
    mat_prod(A, B)

    tempo = medir_tempo(func, A, B)
    return tempo

tests_cases ={
    "m < n, pequena (15, 10, 30)":(15, 10, 30),    
    "m > n, pequena (30, 10, 15)":(30, 10, 15),    
    "m = n, pequena (30, 30, 30)":(30, 30, 30), 
    "m < n, grande (300, 200, 500)":(300, 200, 500), 
    "m > n, grande (500, 200, 300)":(500, 200, 300),
    "m = n, grande (500, 500, 500)":(500, 500, 500),
}

def run_cases(func):
    tempos = []
    for _, (m,k,n) in tests_cases.items():
        tempo = test_prod(m, k, n, func)
        tempos.append(tempo)
    return tempos

tempos_mat_prod = run_cases(mat_prod)
################################ Questão 1 - C ################################

def mat_prod_dot(A, B):
    m, _ = A.shape
    _, p = B.shape
    C = np.zeros((m, p))

    for i in range(m):
        for j in range(p):
                C[i, j] = np.dot(A[i], B[:,j])

    return C

tempos_mat_prod_dot = run_cases(mat_prod_dot)
# A complexidade algoritmica diminuiu logo diminui o tempo de execução dos
# testes anteriores

################################ Questão 1 - D ################################

tempos_matmul = run_cases(np.matmul)

t_mat_prod = np.array(tempos_mat_prod)
t_mat_prod_dot = np.array(tempos_mat_prod_dot)
t_matmul = np.array(tempos_matmul)

compare = np.c_[
    np.ones_like(t_mat_prod),
    t_mat_prod/t_mat_prod_dot,
    t_mat_prod/t_matmul
]

exact = np.c_[
    t_mat_prod,
    t_mat_prod_dot,
    t_matmul
] 

comp = pd.DataFrame(
    compare,
    tests_cases,
    columns=["mat_prod", "mat_prod_dot", "matmul"]
)

ex = pd.DataFrame(
    exact,
    tests_cases,
    columns=["mat_prod", "mat_prod_dot", "matmul"]
)

print("Quanto as outras funcoes são melhores?")
comp.to_csv("comp_py.csv")
print(comp)

print("Valores exatos de tempo")
ex.to_csv("exatos_py.csv")
print(ex)
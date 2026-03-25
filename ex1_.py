import numpy as np

################################ Questão 1 - A ################################

def mat_prod(A: np.matrix, B: np.matrix) -> np.matrix:
    m, n = A.shape
    _, p = B.shape
    C = np.zeros((m, p))
    
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i, j] += A[i, k]*B[k, j]           

    return C

################################ Questão 1 - B ################################

# TODO: Criar casos de teste 
#       - Neste item os casos de teste são comparados entre si
#       - Usar apropiadamente as funcoes de medicao de tempo para evitar erros
#       de medida, algumas das praticas são:
#           - Executar 1, 2 ou um numero pequeno de vezes para compilar
#           - O tempo de execução muda de computador para computador então é
#           interessante fazer uma razão para dizer quanto mais rapido é um ca-
#           so em relação a outro
#           - Quanto o codigo é simples, é interessante executar varias vezes
#           para evitar flutuações de processos em segundo plano e então fazer
#           uma media dos tempos.

################################ Questão 1 - C ################################

def mat_prod_dot(A, B):
    m, _ = A.shape
    _, p = B.shape
    C = np.zeros((m, p))

    for i in range(m):
        for j in range(p):
                C[i, j] = np.dot(A[i], B[:,j])

    return C

# TODO: Executar novamente os casos de teste anteriores mas agora com
#       mat_prod_dot

################################ Questão 1 - D ################################

# TODO: Executamos novamente os casos de teste anteriores com np.matmul
#       - Como queremos comparar cada funcao aos casos de teste anteriores é
#       interessante fazer todas as razoes em relacao a funcao mat_prod
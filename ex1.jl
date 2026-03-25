using LinearAlgebra
using Random
using BenchmarkTools
using DataFrames

################################ Questão 1 - A ################################

function mat_prod(A, B)
    m, n = size(A)
    _, p = size(B)
    C = zeros(m, p)

    for i in 1:m
        for j in 1:p
            for k in 1:n
                C[i,j] = A[i, k]*B[k,j]
            end
        end
    end

    return C
end

################################ Questão 1 - B ################################
# temos 3 classes de teste e em cada categoria de teste 2 tipos de teste
# então ao total realizaremos 6 testes e mediremos seus tempos
function medir_tempo(func, A, B; samples=10, evals=1)
    bench = @benchmark $func($A, $B) samples=samples evals=evals
    return median(bench).time / 1e9   # em segundos
end

function test_prod(m, k, n, func)
    Random.seed!(42)
    A = randn(m, k)
    B = randn(k, n)

    # aquecimento
    func(A, B)
    func(A, B)

    return medir_tempo(func, A, B)
end

test_cases = Dict(
    "m < n, pequena (15, 10, 30)" => (15, 10, 30),
    "m > n, pequena (30, 10, 15)" => (30, 10, 15),
    "m = n, pequena (30, 30, 30)" => (30, 30, 30),
    #"m < n, grande (300, 200, 500)":(300, 200, 500), 
    #"m > n, grande (500, 200, 300)":(500, 200, 300),
    #"m = n, grande (500, 500, 500)":(500, 500, 500),
)

function run_cases(func)
    tempos = Float64[]
    for (_, (m, k, n)) in test_cases
        push!(tempos, test_prod(m, k, n, func))
    end
    return tempos
end

tempos_mat_prod = run_cases(mat_prod)

################################ Questão 1 - C ################################

function mat_prod_dot(A,B)
    m, _ = size(A)
    _, p = size(B)
    C = zeros(m,p)

    for i in 1:m
        for j in 1:p 
            C[i, j] = dot(A[i,:], B[:,j])
        end
    end

    return C
end

tempos_mat_prod_dot = run_cases(mat_prod_dot)

################################ Questão 1 - D ################################

tempos_matmul = run_cases(np.matmul)

nomes = collect(keys(test_cases))

comp = DataFrame(
    caso = nomes,
    baseline = ones(length(t_mat_prod)),
    mat_prod_dot = t_mat_prod ./ t_mat_prod_dot,
    matmul = t_mat_prod ./ t_matmul
)

ex = DataFrame(
    caso = nomes,
    mat_prod = t_mat_prod,
    mat_prod_dot = t_mat_prod_dot,
    matmul = t_matmatmul
)

println("Quanto as outras funções são melhores?")
println(comp)

println("\nValores exatos de tempo")
println(ex)
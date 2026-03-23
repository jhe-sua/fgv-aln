using BenchmarkTools

# Questão 1
# Item A)
function mat_prod(A::Matrix, B::Matrix)
    m, k = size(A)
    n = size(B, 2)
    C = zeros(m, n)

    for i in 1:m
        for j in 1:n
            for p in 1:k
                C[i,j] += A[i, p]*B[p,j]
            end
        end
    end

    return C
end

A_shps = ((1,1), (2,10),(15,10),(6,20),(500, 113), (500, 500), (400, 500), (1000, 1000))
B_shps = ((1,1), (10,5),(10,2),(20,6),(113, 300), (500, 500), (500, 500), (1000, 1000))
times = (10000, 9000, 8000, 7000, 10, 10, 10, 2)

data = []

for i in eachindex(A_shps)
    # os ... significam desempacotamento
    A = rand(A_shps[i]...)
    B = rand(B_shps[i]...)

    push!(data, (A=A, B=B, time=times[i]))
end

# funcao para medir o tempo do item B, C, D
function time_matrix_product_measure(funcao, data)
    println(nameof(funcao))

    results = []

    for item in data
        A = item.A
        B = item.B

        # aquecimento
        funcao(A, B)

        # benchmark
        trial = @benchmark $funcao($A, $B)

        push!(results, (
            mean = mean(trial).time,
            std = std(trial).time
        ))
    end

    return results
end

time_matrix_product_measure(mat_prod)
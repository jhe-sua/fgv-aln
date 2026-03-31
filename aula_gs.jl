using LinearAlgebra

function gs(A)
    m, n = size(A)
    rank = min(m, n)

    Q = zeros(m,rank)
    R = zeros(rank,n)
    u = zeros(m)
    for j in 1:rank
        u .= A[:, j]
        for i in 1:(j-1)
            qi = @view Q[:, i]
            R[i, j] = qi' * u 
        # end
        # for i in 1:(j-1)
        #     qi = @view Q[:, i]
            u .-= R[i, j] .* qi
        end
        r_jj = norm(u)
        R[j, j] = r_jj
        Q[:,j] .= u ./ r_jj
    end

    for j in (rank + 1):n
        u = A[:, j]
        for i in 1:rank
            R[i, j] = Q[:, i]' * u 
        end
    end
    
    return Q, R
end

function main()  
    A = [1 2 1 4; 3 4 2 3; 5 4 2 5; 6 4 1 1; 7 2 3 1]
    Q, R = gs(A)
    @show Q * R

    nothing
end

function test(m, n, b)
    r = min(m, n)

    A = randn(m, n)
    U, s, Vstar = svd(A)
    @show s
    s = b.^(1:r)
    # A = U * diagm(r,r,s) * Vstar
    A = U * diagm(r,r,s) * U'

    println("Gram-Schmodt Bernardo")
    @time Q, R = gs(A)
    @show norm(Q*R - A)
    @show norm(Q' * Q - I)

    println("QR LAPACK")
    @time Q, R = qr(A)
    @show norm(Q*R - A)
    @show norm(Q' * Q - I)

    nothing
end

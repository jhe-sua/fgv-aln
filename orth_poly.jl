using LinearAlgebra
using Plots

# recebemos como entrada um polinomio com esta cara
# p(x) = c_0*x^0 + c_1*x^1 + c_2*x^2 + ... + c_n*x^n

# 0. deixamos, onde possivel, x em evidencia e olhamos para o segundo fator
# 1. p(x) = c_0*x^0 + x*(c_1 + c_2*x^1 + ... + c_n*x^(n-1))
# 2. continuamos esse processo ate chegar em:
# 3. p(x) = c_0*x^0 + x*(c_1 + x*(c_2 + x*(...(c_(n-2) + x*(c_(n-1) + c_n*x)...)))

function polyval(x, coeffs)
    result = zero(x)
    for c in reverse(coeffs)
        result = x * result + c 
    end
    return result
end

function main()
    base = [
        [1.0],
        [0.0, 1.0],        
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 1.0],        
    ]
    xs = -1:0.01:1
    m = length(xs)
    A = [polyval(x, coeffs) for x in xs, coeffs in base]
    return xs, A ./ sqrt(m/2)
end

function main_1()
    base = [
        [1.0],
        [0.0, 1.0],        
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 1.0],        
    ]
    xs = -5:0.01:5
    m = length(xs)
    A = [polyval(x, coeffs)*exp(-x^2 / 2) for x in xs, coeffs in base]
    return xs, A ./ sqrt(m/10)
end

function P_1()
    base = [
        [1.0],
        [0.0, 1.0],        
        [0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 1.0],        
    ]
    xs = -5:0.01:5
    A = [polyval(x, coeffs) for x in xs, coeffs in base]

    return A
end
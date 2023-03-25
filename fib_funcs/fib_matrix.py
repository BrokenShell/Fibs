def matrix_mult(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_pow(M, n):
    if n == 1:
        return M
    elif n % 2 == 0:
        temp = matrix_pow(M, n//2)
        return matrix_mult(temp, temp)
    else:
        return matrix_mult(M, matrix_pow(M, n-1))

def fib_matrix_exponentiation(n):
    if n <= 1:
        return n

    F = [[1, 1], [1, 0]]
    Fn = matrix_pow(F, n-1)
    return Fn[0][0]

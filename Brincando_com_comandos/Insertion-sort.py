A = [31, 41, 59, 26, 41, 22, 19]
for chave, valor in enumerate(A):
    i = chave
    j = chave - 1
    while i > 0 and A[i] < A[j]:
        A[i] = A[j]
        A[j] = valor
        i -= 1
        j -= 1
print(A)
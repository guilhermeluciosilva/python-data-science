A = [31, 41, 59, 26, 41, 58]
for v in range(A):
    chave = A[v]
    i = v -1
    while i > 0 and A[i] > chave:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = chave
print(A) 
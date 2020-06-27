A = [1, 2, 2, 4, 1, 2, 5, 6, 2, 5, 6, 7, 2, 5, 6, 7, 3, 6, 7, 2, 4, 5, 6, 2, 5, 6, 3, 2, 5, 6, 2, 5, 3, 2, 23, 4, 2, 4]
v = int(input("Valor: "))
pos = []
for chave, conteudo in enumerate(A):
    if v == A[chave]:
        pos.append(chave)
if len(pos) != 0:
    print(f"{v} = A{pos}")
else:
    print(False)
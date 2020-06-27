A = [31, 41, 59, 26, 41, 22]
for chave, valor in enumerate(A):
    for numero in range(len(A)):
        if numero < valor:
            A.insert(chave, numero)
            break
        else:
            A.append(numero)

print(A)
# -*- coding: utf-8 -*-

#rotacionar pode ser considerado com a operação de substituir a fatia da lista até a posição -K e colocá-la no começo
#o ciclo se repete toda vez que K for igual a len(A), assim, o resto da divisão é utilizado

def solutions(A, K):
    if len(A) == 0 or K == 0:
        return A
    else:
        K = K % len(A) #resto da divisão
        return A[-K:] + A[:-K]


#### TESTE
# A = [3, 8, 9, 7, 6]

# K = int(input("Quantas vezes irá rotacionar?"))

# if len(A) == 0 or K == 0:
#     print(A)

# else:
#     K = K % len(A)
#     print(A[-K:] + A[:-K])

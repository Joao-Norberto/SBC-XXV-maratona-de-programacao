def fatorial(N):
    fact = 1
    for i in range(1, int(N) + 1):
        fact = fact*i

    return fact


N, K = input().split()
N = int(N)
K = int(K)
weight = []


value = input().split()
for j in value:
    weight.append(int(j))

A, B = input().split()
A = int(A)
B = int(B)

max_index = len(weight) - 1

# ----------------->revisar cálculo<--------------------
numeroDeEscolhas = int(fatorial(N) / (fatorial(K) * fatorial((N-K))))

for i in range(0, max_index+1):
    if i == max_index:
        for j in range(0, len(weight)-1):
            numeroAtual = weight[i]
            proximoNumero = weight[0+j]
            if (numeroAtual + proximoNumero) > B or (numeroAtual + proximoNumero) < A:
                numeroDeEscolhas = numeroDeEscolhas - 1
    else:
        for j in range(0, max_index+1):
            numeroAtual = weight[i]
            proximoNumero = weight[max_index-j]
            if numeroAtual == proximoNumero:
                numeroDeEscolhas = numeroDeEscolhas
            elif (numeroAtual + proximoNumero) > B or (numeroAtual + proximoNumero) < A:
                numeroDeEscolhas = numeroDeEscolhas - 1

print(numeroDeEscolhas)

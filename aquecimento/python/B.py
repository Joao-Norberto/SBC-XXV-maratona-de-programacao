#retorna o fatorial de um número
def fatorial(n):
    fat = 1
    for i in range(n, 1, -1):
        fat = fat * i
    return fat


#retorna o fatorial mais próximo de um número
def fatorial_min(n):
    X = int(1)
    while fatorial(X) <= N:
        X = X + 1
    return X - 1


N = int(input())
qtd_fatoriais = int(0)

while N > 0:
    N = N - fatorial(fatorial_min(N))
    qtd_fatoriais = qtd_fatoriais + 1
    
print(qtd_fatoriais)

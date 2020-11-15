C = int(input())
caixas = []
saldo = 100
saldos = [100]

for i in range(0, C):
    caixas.append(int(input()))


for j in caixas:
    saldo += j
    saldos.append(saldo)

saldos.sort()
saldos.reverse()
print(saldos[0])

P, F = input().split()

P = int(P)
F = int(F)
competidores = []
impares = []
pares = []
for k in range(0, P):
    competidores.append(0)


for i in range(0, F):
    comp, amg = input().split()
    competidores[int(comp) - 1] += 1

for i in competidores:
    if competidores[i] % 2 == 0:
        pares.append(competidores[i])

    else:
        impares.append(competidores[i])
if len(pares) > len(impares):
    print("N")
else:
    print("Y")

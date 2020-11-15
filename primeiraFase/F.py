# Jogador esquerda 1 direita 0
jogadas = input()
acon = []
win = 0
for k in range(0, len(jogadas)):
    acon.append(jogadas[k])
saq = 1
esq = [0, 0]
dire = [0, 0]

for i in acon:
    if i == 'S':
        if saq == 1:
            esq[0] = esq[0] + 1
            saq = 1
        else:
            dire[0] = dire[0] + 1
            saq = 0

    if i == 'R':
        if saq == 1:
            dire[0] = dire[0] + 1
            saq = 0
        else:
            esq[0] = esq[0] + 1
            saq = 1

    if ((dire[0] >= 5) and (dire[0] - esq[0] >= 2) or (dire[0] >= 10)):
        dire[1] = dire[1] + 1
        dire[0] = 0
        saq = 1

    if ((esq[0] >= 5) and (esq[0] - dire[0] >= 2) or (esq[0] >= 10)):
        esq[1] = esq[1] + 1
        esq[0] = 0
        saq = 0

    if i == 'Q':
        if saq == 0:
            print(esq[1], " (", esq[0], ") ", " - ",
                  dire[1], " ( ", esq[0], "*)")
        if saq == 1:
            print(esq[1], " (", esq[0], "*) ",
                  " - ", dire[1], " ( ", esq[0], ")")

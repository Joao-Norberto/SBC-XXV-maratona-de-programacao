L, C = input().split()
L = int(L)
C = int(C)

matrix_linha = list()
linha = list()
matrix_col = list()
coluna = list()
matrix_diag = list()

# adicionando matriz de linhas
for i in range(0, L):
    linha = input()
    matrix_linha.append(linha)

# adicionando matriz de colunas
for i in range(0, C):
    for j in range(0, L):
        coluna.append(matrix_linha[j][i][0])
    line = ''.join(coluna)
    matrix_col.append(line)
    coluna.clear()

# adicionando matriz de diagonais

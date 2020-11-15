N = int(input())
navio = list()
navios = list()
valido = True

for i in range(0, N):
    D, L, R, C = input().split()
    D = int(D)
    L = int(L)
    R = int(R)
    C = int(C)

    # se estiver na horizontal
    if D == 0:
        for j in range(0, ((C+L-1)+1)-C):
            posNavio = [R, C+j]
            navio.append(posNavio)

    # se estiver na vertical
    else:
        for j in range(0, ((R+L-1)+1)-R):
            posNavio = [R+j, C]
            navio.append(posNavio)

    navios.append(navio.copy())
    navio.clear()

# se passou do grid 10x10

# para cada navio
i = int(0)
while i < len(navios):
    # para cada posição
    for j in range(0, len(navios[i])):
        # se a coordenada x ou y for maior que 10
        if navios[i][j][0] > 10 or navios[i][j][1] > 10:
            print('N')
            i = len(navios)
            valido = False
            break
    i = i + 1


# caso esteja no mesmo lugar que outro navio

# se estiverem dentro do grid
if valido:
    counter = int(0)
    while counter < len(navios):
        # para cada posição
        for j in range(0, len(navios[counter])):
            if counter+1 < len(navios):
                next_index = counter+1
            elif counter+1 >= len(navios):
                next_index = 0
            else:
                next_index = len(navios)-1

            if navios[counter][j] in navios[next_index]:
                print('N')
                valido = False
                counter = len(navios)
                break
        counter = counter + 1

if valido:
    print('Y')

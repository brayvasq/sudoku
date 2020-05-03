from Alg_Sudoku.algor_posicion_unica import crear_matriz, printmatriz, obtener_posicion_ver_cadena

cadena_original_2 = "0,0,4,0,0,6,0,2,0,0,0,7,8,0,0,9,1,0,0,0,0,0,0,0,3,0,8,0,1,8,3,0,0,2,0,0,3,0,0,7,8,9,0,0,1,0,0,9,0,0,1,0,6,0,8,0,3,0,0,0,5,0,0,0,4,5,0,0,3,6,0,0,0,2,6,5,0,0,1,0,0"
cadena_nueva    = "5,0,1,3,4,9,7,2,8,4,3,7,8,1,2,6,5,9,9,2,8,7,5,6,1,4,3,1,5,2,0,7,4,0,0,6,8,7,0,5,3,1,4,9,2,6,4,3,2,9,8,5,7,1,3,6,9,4,8,7,2,1,5,2,1,4,9,6,5,0,0,7,7,8,5,1,2,3,9,6,4"


def candidato_unico(matriz : []) -> []:
    candidatos_list = []
    candidato = 0
    pos_i = 0
    pos_j = 0
    if len(matriz) == 9:
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[i])):
                if matriz[i][j] == 0:
                    candidatos = obtener_candidatos(matriz, i, j)
                    #print("Candidatos de la Pos i = " + str(i) + " Pos j = " + str(j) + " " + str(candidatos))
                    if len(candidatos) == 1:
                        candidato = candidatos.pop()
                        pos_i = i
                        pos_j = j
                        # return (pos_i, pos_j,candidato)
                        candidatos_list.append((pos_i, pos_j, candidato))
    else:
        print("Matriz no valida")
    # Sino encuentra un candidato unico retorna cero.
    # return (pos_i, pos_j,candidato)
    if len(candidatos_list) == 0:
        candidatos_list.append((0, 0,0))
    return candidatos_list



def matriz_str_to_int(matriz : []):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i][j] = int(matriz[i][j])



# Para entender este algoritmo seguir un ejemplo en hoja paso a paso
def obtener_candidatos(matriz: [], i: int, j: int) -> []:
    candidatos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    fila_i = matriz[i]
    columna_j = []

    # Candidatos de la fila_i
    for pos_i in range(0, len(fila_i)):
        if fila_i[pos_i] != 0:
            # Trata de remover ese elemento sino lo encuentra no remueve nada
            if candidatos.__contains__(fila_i[pos_i]):
                candidatos.remove(fila_i[pos_i])

    # Obtenemos la columna
    for pos_i in matriz:
        columna_j.append(pos_i[j])

    # Candidatos de columna_j
    for pos_j in range(0, len(columna_j)):
        if columna_j[pos_j] != 0:
            # Trata de remover ese elemento sino lo encuentra no remueve nada
            if candidatos.__contains__(columna_j[pos_j]):
                candidatos.remove(columna_j[pos_j])


    # Obtenemos el cuadrante
    cuadrante = obtener_matriz_cuadrante(matriz, i, j)

    # Recorremos el cuadrante
    for pos_i in range(0, len(cuadrante)):
        for pos_j in range(0, len(cuadrante)):
            # Trata de remover ese elemento sino lo encuentra no remueve nada
            if cuadrante[pos_i][pos_j] != 0:
                if candidatos.__contains__(cuadrante[pos_i][pos_j]):
                    candidatos.remove(cuadrante[pos_i][pos_j])

    return candidatos


def obtener_matriz_cuadrante(matriz: [[]], i: int, j: int) -> [[]]:
    cuadrante = [[0,0,0],[0,0,0],[0,0,0]]
    i_temp = 0
    j_temp = 0
    if len(matriz) == 9:
        if i >= 0 and i <= 2 and j >= 0 and j <= 2:
            for pos_i in range(0, 3):
                for pos_j in range(0, 3):
                    cuadrante[i_temp][j_temp] = matriz[pos_i][pos_j]
                    j_temp += 1
                j_temp = 0
                i_temp += 1
        elif i >= 0 and i <= 2 and j >= 3 and j <= 5:
            for pos_i in range(0, 3):
                for pos_j in range(3, 6):
                    cuadrante[i_temp][j_temp] = matriz[pos_i][pos_j]
                    j_temp += 1
                j_temp = 0
                i_temp += 1
        elif i >= 0 and i <= 2 and j >= 6 and j <= 8:
            for pos_i in range(0, 3):
                for pos_j in range(6, 9):
                    cuadrante[i_temp][j_temp] = matriz[pos_i][pos_j]
                    j_temp += 1
                j_temp = 0
                i_temp += 1
        elif i >= 3 and i <= 5 and j >= 0 and j <= 2:
            for pos_i in range(3, 6):
                for pos_j in range(0, 3):
                    cuadrante[i_temp][j_temp] = matriz[pos_i][pos_j]
                    j_temp += 1
                j_temp = 0
                i_temp += 1
        elif i >= 3 and i <= 5 and j >= 3 and j <= 5:
            for pos_i in range(3, 6):
                for pos_j in range(3, 6):
                    cuadrante[i_temp][j_temp] = matriz[pos_i][pos_j]
                    j_temp += 1
                j_temp = 0
                i_temp += 1
        elif i >= 3 and i <= 5 and j >= 6 and j <= 8:
            for pos_i in range(3, 6):
                for pos_j in range(6, 9):
                    cuadrante[i_temp][j_temp] = matriz[pos_i][pos_j]
                    j_temp += 1
                j_temp = 0
                i_temp += 1
        elif i >= 6 and i <= 8 and j >= 0 and j <= 2:
            for pos_i in range(6, 9):
                for pos_j in range(0, 3):
                    cuadrante[i_temp][j_temp] = matriz[pos_i][pos_j]
                    j_temp += 1
                j_temp = 0
                i_temp += 1
        elif i >= 6 and i <= 8 and j >= 3 and j <= 5:
            for pos_i in range(6, 9):
                for pos_j in range(3, 6):
                    cuadrante[i_temp][j_temp] = matriz[pos_i][pos_j]
                    j_temp += 1
                j_temp = 0
                i_temp += 1
        elif i >= 6 and i <= 8 and j >= 6 and j <= 8:
            for pos_i in range(6, 9):
                for pos_j in range(6, 9):
                    cuadrante[i_temp][j_temp] = matriz[pos_i][pos_j]
                    j_temp += 1
                j_temp = 0
                i_temp += 1

    else:
        print("Matriz no valida ",matriz)

    return cuadrante

if __name__ == "__main__":
    matriz = crear_matriz(cadena_original_2)
    printmatriz(matriz=matriz)
    matriz_str_to_int(matriz)
    print(candidato_unico(cadena_nueva))
    # pos_i, pos_j, numeros = candidato_unico(matriz)
    # # obtenemos la posicion en la cadena
    # posicion_cadena = obtener_posicion_ver_cadena(pos_i,pos_j)
    # print((pos_i,pos_j,numeros))
    # print(posicion_cadena)
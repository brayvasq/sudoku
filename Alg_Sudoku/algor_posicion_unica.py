
cadena_original = "0,0,6,0,3,0,7,0,8,0,3,0,0,0,0,0,0,1,2,0,0,0,0,0,6,0,0,1,0,0,3,5,0,0,0,6,0,7,9,0,4,0,1,5,0,5,0,0,0,1,7,0,0,4,0,0,2,0,0,0,0,0,7,6,0,0,0,0,0,0,8,0,4,0,7,0,6,0,2,0,0"
# cadena_sudoku = "0,0,6,0,3,0,7,0,8,0,3,0,0,0,0,0,0,1,2,0,0,0,0,0,6,0,0,1,0,0,3,5,0,0,0,6,0,7,9,0,4,0,1,5,0,5,0,0,0,1,7,0,0,4,0,0,2,0,0,0,0,0,7,6,0,0,0,0,0,0,8,0,4,0,7,0,6,0,2,0,0"
cadena_sudoku_2 = "0,0,1,9,5,7,0,6,3,0,0,0,8,0,6,0,7,0,7,6,9,1,3,0,8,0,5,0,0,7,2,6,1,3,5,0,3,1,2,4,9,5,7,8,6,0,5,6,3,7,8,0,0,0,1,0,8,6,0,9,5,0,7,0,9,0,7,1,0,6,0,8,6,7,4,5,8,3,0,0,0"
cadena_sudoku_3 = "0,0,1,0,0,9,7,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,5,0,1,4,3,0,5,0,0,0,4,0,0,6,8,7,0,0,0,0,0,9,2,6,0,0,2,0,0,0,7,0,3,6,9,0,8,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,5,1,0,0,9,0,0"
cadena_nueva    = "5,0,1,3,4,9,7,2,8,4,3,7,8,1,2,6,5,9,9,2,8,7,5,6,1,4,3,1,5,2,0,7,4,0,0,6,8,7,0,5,3,1,4,9,2,6,4,3,2,9,8,5,7,1,3,6,9,4,8,7,2,1,5,2,1,4,9,6,5,0,0,7,7,8,5,1,2,3,9,6,4"
##### Crea una matriz a partir de la cadena #########
def crear_matriz(cadena_sudoku: str) -> []:
    for i in range(17, len(cadena_sudoku), 18):
        cadena_sudoku = cadena_sudoku[0:i] + '-' + cadena_sudoku[i + 1:len(cadena_sudoku)]

    matriz = []

    for i in cadena_sudoku.split("-"):
        row = i.split(",")
        matriz.append(row)

    return matriz


def resolver_unica_pos(matriz):
    lista = []
    resp = obtener_posicion_unica(matriz)
    while(resp!=[]):
        lista.append(resp)
        val = resp[0]
        pos = resp[1][0]
        matriz[pos[0]][pos[1]] = val
        #printmatriz(matriz)
        resp = obtener_posicion_unica(matriz)

    return lista


def obtener_posicion_unica1(matriz):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    respuesta = False
    respuesta_final = []
    matriz_candidata = crear_matriz_candidatos()
    for i in range(0,len(matriz)):
        faltantes = []
        for j in nums:
            if not matriz[i].__contains__(j):
                faltantes.append(j)

        opciones = []
        for k in range(0,len(matriz[i])):
            if matriz[i][k] == '0':
                opciones.append([i,k])

                for f in faltantes:
                    posicion = []
                    for o in opciones:
                        matriz_candidata = obtener_candidatos_matriz(f,o,matriz,matriz_candidata)

    #printmatriz(matriz_candidata)
    resp = procesar_matriz_p(matriz_candidata)
    return resp
def procesar_matriz_p(matriz_c):
    respuesta = False
    resp = []
    matriz_temp = []

    resp = verificar_pos_un(matriz_c)

    if len(resp)== 0:
        matriz_temp = obtener_matriz_col(matriz_c)
        resp = verificar_pos_un(matriz_temp)
        if len(resp) > 0:
            pos = resp[1]
            val = resp[0]
            resp = [val, [pos[0], pos[1]]]

    return resp


def obtener_matriz_col(matriz_c):
    matriz_temp = []
    for i in range(0,len(matriz_c)):
        col = []
        for k in range(0,len(matriz_c)):
            col.append(matriz_c[k][i])

        matriz_temp.append(col)
    printmatriz(matriz_temp)
    return matriz_temp

def crear_matriz_candidatos():
    matriz_c = []

    for i in range(0, 9):
        matriz_c.append([])
        for j in range(0, 9):
            matriz_c[i].append([])
            matriz_c[i][j] = []
    #printmatriz(matriz_c)
    return matriz_c


def obtener_candidatos_matriz(f,o,matriz,matriz_c):
   # print("para posicion ",o," ===>")
    if(verifica(f,o,matriz)):
        w =matriz_c[o[0]][o[1]]
    #    print("Se encontro ", f, " :) ")
        if not w.__contains__(f):
            w.append(f)

    return matriz_c


def verificar_pos_un(matriz_c):
    encontro = False
    resp = []
    for i in range(0,len(matriz_c)):
        if encontro:
            break
        for j in range(0,len(matriz_c[i])):
            if encontro:
                break
            if len(matriz_c[i][j]) == 1:
                resp = [matriz_c[i][j][0],[i,j]]
                #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")
                #print(resp)
                #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                break

    return resp


def obtener_posicion_unica(matriz):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    respuesta = False
    posicion = []

    respuesta_final = []
    #### Recorriendo las filas
    for i in range(0, len(matriz)):
        if len(respuesta_final) > 0:
            print("Encontró por fila")
            break
        # Arreglo para las los numeros que faltan en la fila
        faltantes = []

        ## Recorrido que añade los numeros faltantes
        for j in nums:
            if not matriz[i].__contains__(j):
                faltantes.append(j)

        # Lista que guarda las posibles posiciones en la fila
        opciones = []

        for k in range(0, len(matriz[i])):
            if matriz[i][k] == '0':
                opciones.append([i, k])

        respuesta_final = faltantes_pos(faltantes, opciones, respuesta_final, matriz)

    matriz_temp = obtener_matriz_col(matriz)

    if len(respuesta_final) == 0:
        posicion = []

        respuesta_final = []
        #### Recorriendo las filas
        for i in range(0, len(matriz_temp)):
            print("recorriendo columna ",i)
            if len(respuesta_final) > 0:
                print("Encontró por columna")
                break
            # Arreglo para las los numeros que faltan en la fila
            faltantes = []

            ## Recorrido que añade los numeros faltantes
            for j in nums:
                if not matriz_temp[i].__contains__(j):
                    faltantes.append(j)

            # Lista que guarda las posibles posiciones en la fila
            opciones = []

            for k in range(0, len(matriz_temp[i])):
                if matriz_temp[i][k] == '0':
                    opciones.append([i, k])

            respuesta_final = faltantes_pos(faltantes, opciones, respuesta_final, matriz_temp)
            #print("--------------------------------------------------->",respuesta_final)
            if(len(respuesta_final)>0):
                val = respuesta_final[0]
                pos = [respuesta_final[1][0][1],respuesta_final[1][0][0]]
                respuesta_final = [val,[pos]]

    return respuesta_final

def obtener_posicion_unica2(matriz):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    respuesta = False
    posicion = []

    respuesta_final = []
    #### Recorriendo las filas
    for i in range(0, len(matriz)):
        if len(respuesta_final)>0:
            print("Encontró por fila")
            break
        # Arreglo para las los numeros que faltan en la fila
        faltantes = []

        ## Recorrido que añade los numeros faltantes
        for j in nums:
            if not matriz[i].__contains__(j):
                faltantes.append(j)

        # Lista que guarda las posibles posiciones en la fila
        opciones = []

        for k in range(0, len(matriz[i])):
            if matriz[i][k] == '0':
                opciones.append([i, k])

        respuesta_final = faltantes_pos(faltantes,opciones,respuesta_final,matriz)


    if len(respuesta_final)==0:
        for i in range(0, len(matriz)):
            if len(respuesta_final) > 0:
               print("Encontró por columna")
               break
            faltantes = []

            ## Recorrido que añade los numeros faltantes
            for k in range(0,len(matriz)):
                for j in nums:
                    if not matriz[k][i]==j:
                        faltantes.append(j)

            # Lista que guarda las posibles posiciones en la fila
                opciones = []
                if matriz[k][i] == '0':
                   opciones.append([k, i])


            respuesta_final = faltantes_pos(faltantes,opciones,respuesta_final,matriz)

                    ####### Recorrer los faltantes y las opciones y enviar al obtener posición #######
    return respuesta_final

def faltantes_pos(faltantes,opciones,respuesta_final,matriz):
    respuesta = False
    for f in faltantes:
        posicion = []
        if respuesta:
            break
        for o in opciones:
            if respuesta:
                break
            temp = obtener_posicion(f, o, matriz)
            if len(temp) > 0:
                posicion.append(temp)
        # print("para el valor : ", f, " Se encontro los lugares en metodo(obtener posicion unica) => : ", posicion)
        if len(posicion) == 1:
            respuesta = True
            respuesta_final = [f, posicion[0]]

    return respuesta_final

def obtener_posicion(f, o, matriz):
    lugares = []
    if verifica(f, o, matriz):
        lugares.append(o)
    #print("para el valor : ", f, " Se encontro el lugar en metodo(obtener posicion) => : ", lugares)
    return lugares


def verifica(f, o, matriz):
    return verificar_fila(f, o, matriz) and verificar_columna(f, o, matriz) and verificar_recuadro(f, o, matriz)


def verificar_fila(f, o, matriz):
    fila = matriz[o[0]]
    return not fila.__contains__(f)


def verificar_columna(f, o, matriz):
    columna = [c[o[1]] for c in matriz]
    return not columna.__contains__(f)


def verificar_recuadro(f, o, matriz):
    cuandrante = obtener_cuadrante(o)
    valores = []

    for k in cuandrante:
        valores.append(matriz[k[0]][k[1]])

    return not valores.__contains__(f)


def obtener_cuadrante(o):
    if o[1] <= 2 and o[0] <= 2:
        return [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        # return 1
    elif o[1] > 2 and o[1] <= 5 and o[0] <= 2:
        return [[0, 3], [0, 4], [0, 5], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5]]
        # return 2
    elif o[1] > 5 and o[1] <= 8 and o[0] <= 2:
        return [[0, 6], [0, 7], [0, 8], [1, 6], [1, 7], [1, 8], [2, 6], [2, 7], [2, 8]]
        # return 3
    elif o[1] <= 2 and o[0] > 2 and o[0] <= 5:
        return [[3, 0], [3, 1], [3, 2], [4, 0], [4, 1], [4, 2], [5, 0], [5, 1], [5, 2]]
        # return 4
    elif o[1] > 2 and o[1] <= 5 and o[0] > 2 and o[0] <= 5:
        return [[3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5], [5, 3], [5, 4], [5, 5]]
        # return 5
    elif o[1] > 5 and o[1] <= 8 and o[0] > 2 and o[0] <= 5:
        return [[3, 6], [3, 7], [3, 8], [4, 6], [4, 7], [4, 8], [5, 6], [5, 7], [5, 8]]
        # return 6
    elif o[1] <= 2 and o[0] > 5 and o[0] <= 8:
        return [[6, 0], [6, 1], [6, 2], [7, 0], [7, 1], [7, 2], [8, 0], [8, 1], [8, 2]]
        # return 7
    elif o[1] > 2 and o[1] <= 5 and o[0] > 5 and o[0] <= 8:
        return [[6, 3], [6, 4], [6, 5], [7, 3], [7, 4], [7, 5], [8, 3], [8, 4], [8, 5]]
        # return 8
    elif o[1] > 5 and o[1] <= 8 and o[0] > 5 and o[0] <= 8:
        return [[6, 6], [6, 7], [6, 8], [7, 6], [7, 7], [7, 8], [8, 6], [8, 7], [8, 8]]
        # return 9


##### obtiene la posición general en el tablero ########
def obtener_posicion_ver_cadena(x, y):
    return (9 * x) + y


def printmatriz(matriz):
    for i in matriz:
        print(i)


if __name__ == "__main__":

    matriz = crear_matriz(cadena_nueva)
    printmatriz(matriz)
    lista = resolver_unica_pos(matriz)
    print(lista)
    #print("#########################################\n")
    #posicion = obtener_posicion_unica(matriz)
    #print(posicion)

    # Sino encuentra, retorna una lista vacia
    #val = posicion[0]
    #pos = posicion[1][0]
    #matriz[pos[0]][pos[1]] = val
    #printmatriz(matriz)
    #posicion = obtener_posicion_unica(matriz)
    #print(posicion)

    #val = posicion[0]
    #pos = posicion[1][0]
    #matriz[pos[0]][pos[1]] = val
    #printmatriz(matriz)
    # print(obtener_cuadrante([8,6]))




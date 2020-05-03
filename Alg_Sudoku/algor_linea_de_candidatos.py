from Alg_Sudoku.algor_posicion_unica import crear_matriz, printmatriz, verifica,obtener_cuadrante,crear_matriz_candidatos,obtener_candidatos_matriz

cadena_sudoku = "0,0,1,9,5,7,0,6,3,0,0,0,8,0,6,0,7,0,7,6,9,1,3,0,8,0,5,0,0,7,2,6,1,3,5,0,3,1,2,4,9,5,7,8,6,0,5,6,3,7,8,0,0,0,1,0,8,6,0,9,5,0,7,0,9,0,7,1,0,6,0,8,6,7,4,5,8,3,0,0,0"

def resolv_linea_candidatos(matriz):
    lista = []
    resp = linea_candidatos(matriz)
    while (resp != []):
        lista.append(resp)
        val = resp[0]
        pos = resp[1]
        matriz[pos[0]][pos[1]] = val
        #printmatriz(matriz)
        resp = linea_candidatos(matriz)

    return lista

def linea_candidatos(matriz):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    respuesta = False
    respuesta_final = []
    matriz_candidata = crear_matriz_candidatos()
    ### Recorriendo las filas
    for i in range(0, len(matriz)):

        faltantes = []

        ### recojo los numeros faltantes en las filas
        for j in nums:
            if not matriz[i].__contains__(j):
                faltantes.append(j)
                # Lista que guarda las posibles posiciones en la fila
        opciones = []

        for k in range(0, len(matriz[i])):
            if matriz[i][k] == '0':
                opciones.append([i, k])

                ####### Recorrer los faltantes y las opciones y enviar al obtener posición #######

                for f in faltantes:
                    posicion = []
                    for o in opciones:
                        matriz_candidata = obtener_candidatos_matriz(f,o,matriz,matriz_candidata)

    #printmatriz(matriz_candidata)

    resp = procesar_matriz_candidata(matriz_candidata)

    return resp


def procesar_matriz_candidata(matriz_c):
    respuesta = False
    #matriz que obtiene el cuadrante temporal
    matriz_temp = []
    resp = []
    #print("\n\n\nCuadrantes \n")
    for i in range(0,9):
        matriz_temp = []
        #print("Cuadrante ",i)
        if respuesta:
            break
        cuandrante = obtener_cuadrante_numero(i+1)

        matriz_pos = []
        matriz_temp = obtener_matriz_cuadrante(cuandrante,matriz_c,matriz_pos)

        #printmatriz(matriz_temp)
        #print(matriz_pos)
        dict = verificar_matriz_cuadrante(matriz_temp,matriz_c,i+1)

        evaluar_diccionario(dict,matriz_c,matriz_temp,matriz_pos,i+1)

        resp = verificar_matriz_final(matriz_c)

        if len(resp):
            respuesta = True
            break

    #printmatriz(matriz_c)
    return resp
        #print("Fin cuadrante")


def verificar_matriz_final(matriz_c):
    resp = []
    encontro = False
    for i in range(0,9):
        if encontro:
            break
        for j in range(0,9):
            if encontro:
                break
            if len(matriz_c[i][j]) == 1:
                resp.append(matriz_c[i][j][0])
                resp.append([i,j])
                encontro = True

    return resp



def evaluar_diccionario(resp,matriz_c,matriz_temp,matriz_pos,cuadrante):
    #print("Evaluando ",resp," Cuadrante ",cuadrante)
    pos = []
    val = ''
    valor_encontrado = False
    lista_valores = []
    #print(resp)
    for k in resp:
        if resp[k] == 2:
            val = k
            lista_valores.append(val)
            #print("Se encontro ",valor, " Longitud :",resp[k])


   # print("Valor Actual : ",valor)
    for valor in lista_valores:
        pos = []
        #print("Evaluar =>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",valor)
        for i in range(0,3):
            for j in range(0,3):
                #print(matriz_temp[i][j])
                if matriz_temp[i][j].__contains__(valor):
                    pos.append(matriz_pos[i][j])


        if len(pos) == 2:
            if pos[0][0] == pos[1][0]:
                #### misma fila
                #print("misma columan : ",pos," VAlor ",valor)
                #pos_1 = matriz_pos[]
                #print(pos," Valor ",valor," Fila")
                #print("mi fila", matriz_c[pos[0][0]])
                for i in range(0,9):
                    if i != pos[0][1] and i != pos[1][1]:
                        #print(i)
                        if matriz_c[pos[0][0]][i].__contains__(valor):
                            matriz_c[pos[0][0]][i].remove(valor)

            elif pos[0][1] == pos[1][1]:
                #### misma columna
                #print("misma columna : ",pos)
                #print(pos, " Valor ", valor," Columna")
                #print("Mi col ", matriz_c[7][pos[0][1]])
                for i in range(0,9):
                    if i != pos[0][0] and i != pos[1][0]:
                        #print(i)
                        if matriz_c[i][pos[0][1]].__contains__(valor):
                            matriz_c[i][pos[0][1]].remove(valor)



def verificar_matriz_cuadrante(matriz_temp,matriz_c,cuandrante):
    valores_fila = []
    valores = []
    #### buscar por fila
    for i in range(0,3):
        for j in range(0,3):
            for k in matriz_temp[j][i]:
                valores_fila.append(k)
                if not valores.__contains__(k):
                    valores.append(k)

    valor_veces = obtener_repeticiones(valores,valores_fila)
    #print("posicion ====================>",[j,i])
    #print("El diccionario es : ",valor_veces)

    return valor_veces

def obtener_repeticiones(valores,valores_fila):
    diccionario = {}

    for i in valores:
        diccionario[i] = 0

    for j in valores_fila:
        if valores.__contains__(j):
            diccionario[j] += 1

    return diccionario




def obtener_matriz_cuadrante(cuadrante,matriz_c,matriz_pos):
    temp = []
    k = 0
    for i in range(0,3):
        temp.append([])
        matriz_pos.append([])
        for j in range(0,3):
            val = cuadrante[k]
            matriz_pos[i].append(val)
            temp[i].append(matriz_c[val[0]][val[1]])
            k+=1
    return temp

def obtener_cuadrante_numero(cuadrante):
    if cuadrante == 1:
        return obtener_cuadrante([0,0])
    elif cuadrante == 2:
        return obtener_cuadrante([0,3])
    elif cuadrante == 3:
        return obtener_cuadrante([0,6])
    elif cuadrante == 4:
        return obtener_cuadrante([3,0])
    elif cuadrante == 5:
        return obtener_cuadrante([3,3])
    elif cuadrante == 6:
        return obtener_cuadrante([3,6])
    elif cuadrante == 7:
        return obtener_cuadrante([6,0])
    elif cuadrante == 8:
        return obtener_cuadrante([6,3])
    elif cuadrante == 9:
        return obtener_cuadrante([6,6])


if __name__ == "__main__":
    matriz = crear_matriz(cadena_sudoku)
    #printmatriz(matriz)
    resp = resolv_linea_candidatos(matriz)
    print(resp)
    # matriz_c = crear_matriz_candidatos()
    # print(len(matriz_c))
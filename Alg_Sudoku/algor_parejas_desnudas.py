from Alg_Sudoku.algor_posicion_unica import crear_matriz,verificar_pos_un,crear_matriz_candidatos,obtener_candidatos_matriz,obtener_matriz_col,printmatriz
from Alg_Sudoku.algor_linea_de_candidatos import  obtener_cuadrante_numero

cadena_sudoku_t = "4,0,0,2,7,0,6,0,0,7,9,8,1,5,6,2,3,4,0,2,0,8,4,0,0,0,7,2,3,7,4,6,8,9,5,1,8,4,9,5,3,1,7,2,6,5,6,1,7,9,2,8,4,3,0,8,2,0,1,5,4,7,9,0,7,0,0,2,4,3,0,0,0,0,4,0,8,7,0,0,2"
cadena_sudoku_n = "0,0,1,0,0,9,7,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,5,0,1,4,3,0,5,0,0,0,4,0,0,6,8,7,0,0,0,0,0,9,2,6,0,0,2,0,0,0,7,0,3,6,9,0,8,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,5,1,0,0,9,0,0"

def resolv_parejas_desnudas(matriz):
    lista = []
    resp = parejas_desnudas(matriz)
    printmatriz(matriz)
    print(resp)
    while (resp != []):
        #for resp in mlista:
        lista.append(resp)
        val = resp[0]
        pos = resp[1]
        matriz[pos[0]][pos[1]] = val
        #printmatriz(matriz)
        #print("ciclo")
        resp = parejas_desnudas(matriz)
        #print(resp)'''

    return lista

def parejas_desnudas(matriz):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    respuesta = False
    respuesta_final = []

    matriz_candidata = crear_matriz_candidatos()
    #printMatriz(matriz_candidata)

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

    resp = procesar_matriz(matriz_candidata)
    return resp

def procesar_matriz(matriz_c):
    respuesta = False
    matriz_temp = []
    lista = []
    resp = []
    ###Mirar por columnas
    for i in range(0,len(matriz_c)):
        pos = []
        val = []
        obtener_pos_repetida(matriz_c[i],pos,val)
        #print("--------------------------------------------------------------------------")
        #print(pos,val)
        #print("obtiene valores")
        for j in range(0,len(matriz_c[i])):
        #    print("verifica posicion")
            if not pos.__contains__(j):
        #        print("posicion correcta")
                for k in val:
        #            print("recorre valores",k)
                    if matriz_c[i][j].__contains__(k):
        #                print("----------------------->contiene el valor",k)
                        matriz_c[i][j].remove(k)

        for m in pos:
            for n in range(0,9):
                if n != i:
                    for b in val:
                        if(matriz_c[n][m].__contains__(b)):
                            matriz_c[n][m].remove(b)





    #print("#######################33")
    #printmatriz(matriz_c)
    resp = verificar_pos_un(matriz_c)
    '''while(resp!=[]):
        lista.append(resp)
        val = resp[0]
        pos = resp[1]
        matriz_c[pos[0]][pos[1]].remove(val)
        resp = verificar_pos_un(matriz_c)'''

    if len(resp) == 0:
        print("filas")
        ###Mirar por filas
        matriz_temp = obtener_matriz_col(matriz_c)
        #printmatriz(matriz_temp)
        #print("nueva matriz ---------------------")
        #printmatriz(obtener_matriz_col(matriz_temp))
        #obtener_matriz_col(matriz_temp)
        for i in range(0,len(matriz_temp)):
            pos = []
            val = []
            obtener_pos_repetida(matriz_temp[i],pos,val)
            for j in range(0,len(matriz_temp[i])):
                if not pos.__contains__(j):
                    for k in val:
                        if matriz_temp[i][j].__contains__(k):
                            matriz_temp[i][j].remove(k)

            for m in pos:
                for n in range(0, 9):
                    if n != i:
                        for b in val:
                            if (matriz_temp[n][m].__contains__(b)):
                                matriz_temp[n][m].remove(b)

        #print("matriz original")
        #printmatriz(matriz_c)
        #nueva_mat = obtener_matriz_col(matriz_temp)
        #print("matriz_reonvertida")
        #printmatriz(nueva_mat)


        resp = verificar_pos_un(matriz_temp)
        #while(resp!=[]):
        if len(resp) > 0:
            pos = resp[1]
            val = resp[0]
            matriz_temp[pos[0]][pos[1]].remove(val)
            resp = [val,[pos[1],pos[0]]]
            #lista.append(resp)
            #print(resp)
            #resp = verificar_pos_un(matriz_temp)

    if(len(resp)==0):
        revisar_cuadrantes(matriz_c)
        resp = verificar_pos_un(matriz_c)
        '''while(resp!=[]):
            lista.append(resp)
            val = resp[0]
            pos = resp[1]
            matriz_c[pos[0]][pos[1]].remove(val)
            print(resp)
            resp = verificar_pos_un(matriz_c)'''
    return resp

def revisar_cuadrantes(matriz_c):
    lista = []
    for i in range(0,9):
        lista = obtener_cuadrante_numero(i+1)

        valores = []
        for j in lista:
            valores.append(matriz_c[j[0]][j[1]])

        pos = []
        val = []
        obtener_pos_repetida(valores,pos,val)

        for k in range(0,len(pos)):
            if(not pos.__contains__(k)):
                post = lista[k]
                for n in val:
                    if(matriz_c[post[0]][post[1]].__contains__(n)):
                        matriz_c[post[0]][post[1]].remove(n)


def obtener_pos_repetida(col,pos,val):
    for i in range(0,len(col)):
        for j in range(0,len(col)):
            if i != j:
                if(len(col[i])>0):
                    if col[i] == col[j]:
                        if not pos.__contains__(i):
                            pos.append(i)
                            for n in col[i]:
                                val.append(n)

                        if not pos.__contains__(j):
                            pos.append(j)

    #print("$$$$$$$$$$$$$$$$$$$$$$")
    #print(col)
    #print(val)
    #print(pos)
    #print("$$$$$$$$$$$$$$$$$$$$$$")

if __name__=="__main__":
    print("Algor Twins")
    matriz = crear_matriz(cadena_sudoku_n)
    #printMatriz(matriz)
    #matriz = obtener_matriz_col(matriz)
    print()
    print("###################$$$$$$$$$$$$$$")
    #printMatriz(matriz)
    resp = resolv_parejas_desnudas(matriz)
    print(resp)
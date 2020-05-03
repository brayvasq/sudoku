from Client.models.sudoku_client import sudoku_client

if __name__ == '__main__':
    matriz_p2 = "0,0,1,9,5,7,0,6,3,0,0,0,8,0,6,0,7,0,7,6,9,1,3,0,8,0,5,0,0,7,2,6,1,3,5,0,3,1,2,4,9,5,7,8,6,0,5,6,3,7,8,0,0,0,1,0,8,6,0,9,5,0,7,0,9,0,7,1,0,6,0,8,6,7,4,5,8,3,0,0,0"
    matriz_p = "0,0,4,0,0,6,0,2,0,0,0,7,8,0,0,9,1,0,0,0,0,0,0,0,3,0,8,0,1,8,3,0,0,2,0,0,3,0,0,7,8,9,0,0,1,0,0,9,0,0,1,0,6,0,8,0,3,0,0,0,5,0,0,0,4,5,0,0,3,6,0,0,0,2,6,5,0,0,1,0,0"
    cliente = sudoku_client("localhost",21211)
    cliente.request_solve(matriz_p2,3)
    solv =""
    while not cliente.bandera:
        pass

    solv = cliente.respuesta
    print("Imprimiendo el solve", solv)
    print("Columna ",18%9," Fila",18/9)



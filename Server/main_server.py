from Server.models.sudoku_server import sudoku_server

if __name__ == "__main__":
    # El ultimo valor es el id del servidor
    puerto = int(input(">> "))
    serv = sudoku_server(puerto,"Servidorcito de SUDOKU", 1)

from models.server import Server

if __name__ == "__main__":
    # El ultimo valor es el id del servidor
    puerto = int(input(">> "))
    serv = Server(puerto, "Servidorcito de SUDOKU", 1)

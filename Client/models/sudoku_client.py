import socket
from threading import Thread
from Alg_Sudoku.algor_posicion_unica import printmatriz, crear_matriz


class sudoku_client:
    def __init__(self, host: str, port: int) -> None:
        self.matriz_sudoku = ""
        self.socket = None
        self.host = host
        self.port = port
        self.bandera = False
        self.respuesta = ""
        self.hilo = None

    def request_solve(self, matriz_sudoku: str, method: int):
        self.matriz_sudoku = matriz_sudoku
        if self.socket == None:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Para que no espere mas de 10 segundos si el servidor responde o no
            self.socket.settimeout(7)
            try:
                self.socket.connect((self.host, self.port))
            except Exception as ex:
                print("Error en la coneccion con " + str(self.host) + " Puerto " + str(self.port), ex)

        if self.hilo == None:
            self.hilo = Thread(target=self.response_from_server, args=(method,))
            self.hilo.start()

    def response_from_server(self, method: int):
        self.bandera = False
        self.respuesta = ""
        if self.socket != None:

            message = "SOLVE " + str(method) + " " + self.matriz_sudoku
            try:
                self.socket.send(message.encode("utf-8"))
                respuesta = self.socket.recv(1024).decode("utf-8")
                if respuesta != "":
                    respuesta_split = respuesta.split(" ")
                    if respuesta_split[1] != "-1":
                        servidor = respuesta_split[0]
                        posicion = int(respuesta_split[1])
                        numero = respuesta_split[2]
                        # Los prints hay que comentarlos
                        print("Antes")
                        printmatriz(crear_matriz(self.matriz_sudoku))

                        matriz_list_temp = self.convert_matriz_str_to_list(self.matriz_sudoku)
                        matriz_list_temp[posicion] = numero
                        self.matriz_sudoku = self.convert_matriz_list_to_str(matriz_list_temp)

                        print(respuesta)
                        self.respuesta = respuesta
                        print("Despues")
                        printmatriz(crear_matriz(self.matriz_sudoku))
                    else:
                        self.respuesta = respuesta
            except socket.timeout as ex:
                print("Tiempo de espera agotado, no se encontro respuesta por este metodo " + str(method) + " ->", ex)

        else:
            print("No ha iniciado una coneccion valida, no se puede esperar una respuesta")

        self.bandera = True
        self.hilo = None

    def convert_matriz_str_to_list(self, matriz: str):
        matriz_temp = matriz.split(",")
        return matriz_temp

    def close_connection(self):
        try:
            if self.socket != None:
                print("--> Cerrando conexion ")
                self.socket.close()
                self.socket = None
        except Exception as ex:
            print("Error cerrando el socket del cliente", ex)

    def convert_matriz_list_to_str(self, matriz: []):
        matriz_temp = ""
        longitud_matriz = len(matriz)
        for i in range(0, longitud_matriz):
            if i != longitud_matriz - 1:
                matriz_temp += matriz[i] + ","
            else:
                matriz_temp += matriz[i]
        return matriz_temp

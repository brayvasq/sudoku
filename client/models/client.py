import socket
from threading import Thread
from utils.matrix import Matrix


class Client:
    """
    Client to connect with sudoku server

    ...
    Methods
    -------
    request_solve(sudoku_matrix: str, method: int)
        Stablish a connection and ask for a solution

    response_from_server(method: int)
        Ask the server to solve a sudoku with a specific algorithm

    close_connection()
        Closes a server connection
    """

    def __init__(self, host: str, port: int) -> None:
        """
        Parameters
        ----------
        host : str
            The server ip o domain
        port : int
            The server port
        """
        self.sudoku_matrix = ""
        self.socket = None
        self.host = host
        self.port = port
        self.flag = False
        self.response = ""
        self.thread = None

    def request_solve(self, sudoku_matrix: str, method: int):
        """
        Stablish a connection and ask for a solution

        Parameters
        ----------
        sudoku_matrix : str
            The representative sudoku string
        method : int
            The algorithm to execute to solve the sudoku
        """
        self.sudoku_matrix = sudoku_matrix
        if self.socket == None:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Maximum time to wait for a response
            self.socket.settimeout(7)
            try:
                self.socket.connect((self.host, self.port))
            except Exception as ex:
                print("Error: connection: " + str(self.host) + " port: " + str(self.port), ex)

        if self.thread == None:
            self.thread = Thread(target=self.response_from_server, args=(method,))
            self.thread.start()

    def response_from_server(self, method: int):
        """
        Ask the server to solve a sudoku with a specific algorithm

        Parameters
        ----------
        method : int
            The algorithm to execute to solve the sudoku
        """
        self.flag = False
        self.response = ""
        if self.socket != None:

            message = "SOLVE " + str(method) + " " + self.sudoku_matrix
            try:
                self.socket.send(message.encode("utf-8"))
                response = self.socket.recv(1024).decode("utf-8")
                if response != "":
                    response_split = response.split(" ")
                    if response_split[1] != "-1":
                        server = response_split[0]
                        position = int(response_split[1])
                        number = response_split[2]

                        print("Before built matrix")
                        Matrix.print_matrix(Matrix.build_matrix(self.sudoku_matrix))

                        matriz_list_temp = Matrix.to_list(self.sudoku_matrix)
                        matriz_list_temp[position] = number
                        self.sudoku_matrix = Matrix.to_str(matriz_list_temp)

                        print(response)
                        self.response = response
                        print("After built matrix")
                        Matrix.print_matrix(Matrix.build_matrix(self.sudoku_matrix))
                    else:
                        self.response = response
            except socket.timeout as ex:
                print("Error: Connection timeout. A response cannot be found for method: " + str(method) + " =>", ex)

        else:
            print("Error: A valid connection doesn't created, a response can't be waited")

        self.flag = True
        self.thread = None


    def close_connection(self):
        """
        Closes a server connection
        """
        try:
            if self.socket != None:
                print("Info: Closing connection ")
                self.socket.close()
                self.socket = None
        except Exception as ex:
            print("Error: An error occurs closing connection", ex)

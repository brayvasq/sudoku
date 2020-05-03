import socket
from threading import Thread
from Server.models.socket_controller import socket_controller


class sudoku_server:
    def __init__(self, port, name, id_server):
        self.session_id = 1
        self.name = name
        self.port = port
        self.clients = []
        self.id_server = id_server
        self.quitar = False
        self.thread_server = Thread(target=self.run())
        self.thread_server.start()

    def write_message(self, msg):
        for i in self.clients:
            i.write_message(msg)

    def run(self):
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serverSocket.bind(("127.0.0.1", self.port))
            serverSocket.listen(10)
            print("Servidor iniciado con exito en el puerto",self.port)
            while not self.quitar:
                try:
                    socket_c, addr = serverSocket.accept()
                    print("Conexion iniciada con",addr)
                    client = socket_controller(socket_c, addr, self.name, self.session_id, self.id_server, self)
                    self.clients.append(client)

                    self.session_id += 1
                except Exception as ex:
                    print("Error 1 de server ", ex)

            for cl in self.clients:
                cl.close()
            serverSocket.close()
        except Exception as ex:
            print("Error 2 de servidor ", ex)

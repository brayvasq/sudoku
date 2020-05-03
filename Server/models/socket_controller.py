from Alg_Sudoku.algor_candidato_unico import candidato_unico, crear_matriz, matriz_str_to_int, printmatriz
from Alg_Sudoku.algor_posicion_unica import obtener_posicion_ver_cadena,resolver_unica_pos
from Alg_Sudoku.algor_linea_de_candidatos import resolv_linea_candidatos
from Alg_Sudoku.algor_parejas_desnudas import resolv_parejas_desnudas
import threading


class socket_controller:
    def __init__(self, nsocket, addres, name, the_id, id_server, server):
        self.server = server
        self.the_id = the_id
        self.name = name
        self.addres = addres
        self.the_socket = nsocket
        self.id_server = id_server
        self.the_thread = threading.Thread(target=self.run)
        self.the_thread.start()

    def run(self):
        # self.write_message("Bienvenido al servidor de algoritmos para la solucion de Sudokus\n")
        # self.write_message("Metodos que se ofrecen:"
        #                   "\n1 : Posicion Unica"
        #                   "\n2 : Candidato Unico"
        #                   "\n3 : Linea de candidatos\n")
        resp = ""
        try:
            while (not resp.upper().startswith("QUIT")):
                val = self.the_socket.recv(1024)
                resp = val.decode('utf-8')
                if (resp.upper().startswith("SOLVE ")):
                    # self.write_message("Estamos procesando su peticion\n")
                    resp_split = resp.split(" ")
                    if len(resp_split) == 3:
                        metodo_seleccionado = int(resp_split[1])
                        # Removemos el salto de linea con rstrip
                        matriz_sudoku = resp_split[2].rstrip()
                        if len(matriz_sudoku) == 161:
                            matriz = crear_matriz(matriz_sudoku)
                            # printmatriz(matriz)
                            print("Metodo a usar por la sesion " + str(self.the_id) + ", Con ip y puerto : ",
                                  self.addres)
                            if metodo_seleccionado == 1:
                                print("Posicion unica")
                                respuesta_temp = resolver_unica_pos(matriz)
                                # Aunque parezca extraño asi verificamos que la lista no este vacia
                                if len(respuesta_temp)>0 :
                                    respuesta = str(self.id_server)
                                    for respval in respuesta_temp:
                                        pos_i = respval[1][0][0]
                                        pos_j = respval[1][0][1]
                                        numero = respval[0]
                                        posicion_cadena = obtener_posicion_ver_cadena(pos_i, pos_j)
                                        respuesta += " "+str(posicion_cadena) + " " + str(numero)
                                else:
                                    respuesta = str(self.id_server) + " -1"
                                self.write_message(respuesta)

                            elif metodo_seleccionado == 2:
                                print("Candidato unico")
                                matriz_str_to_int(matriz)
                                respuesta = str(self.id_server)
                                candidatos_list = candidato_unico(matriz)
                                # Si encontro algo entonces responde
                                print("Candidatos unicos ",candidatos_list)
                                for tup_temp in candidatos_list:

                                    pos_i, pos_j, numero = tup_temp
                                    if not (pos_i == 0 and pos_j == 0 and numero == 0):
                                        posicion_cadena = obtener_posicion_ver_cadena(pos_i, pos_j)
                                        respuesta += " " + str(posicion_cadena) + " " + str(numero)

                                    else:
                                        respuesta += " -1"
                                print("Candidato unica, respuesta ", respuesta)
                                self.write_message(respuesta)
                            elif metodo_seleccionado == 3:
                                print("Linea de candidatos")
                                respuesta_temp = resolv_linea_candidatos(matriz)
                                if len(respuesta_temp)>0:
                                    respuesta = str(self.id_server)
                                    for respval in respuesta_temp:
                                        pos_i = respval[1][0]
                                        pos_j = respval[1][1]
                                        numero = respval[0]
                                        posicion_cadena = obtener_posicion_ver_cadena(pos_i,pos_j)
                                        respuesta += " " + str(posicion_cadena) + " " + str(numero)
                                else:
                                    respuesta = str(self.id_server) + " -1"
                                self.write_message(respuesta)
                            elif metodo_seleccionado == 4:
                                print("parejas desnudas")
                                respuesta_temp = resolv_parejas_desnudas(matriz)
                                if len(respuesta_temp)>0:
                                    respuesta = str(self.id_server)
                                    for respval in respuesta_temp:
                                        pos_i = respval[1][0]
                                        pos_j = respval[1][1]
                                        numero = respval[0]
                                        posicion_cadena = obtener_posicion_ver_cadena(pos_i,pos_j)
                                        respuesta += " " + str(posicion_cadena) + " " + str(numero)

                                else:
                                    respuesta = str(self.id_server) + " -1"
                                self.write_message(respuesta)
                        else:
                            # self.write_message("Matriz no valida\n")
                            pass
                    else:
                        # self.write_message("Comando solve incompleto, SOLVE #Algoritmo MATRIZ")
                        pass
                else:
                    if not resp.upper().startswith("QUIT"):
                        # self.write_message("Comando no valido\n")
                        pass
        except Exception as ex:
            print("Algo ocurrio con la coneccion con " + str(self.addres), ex)
        self.close()

    def close(self):
        try:
            print("--> Cerrando conexion " + str(self.the_id) + ", con ip y puerto " + str(self.addres) + " \n")
            self.the_socket.close()
            self.server.clients.remove(self)
        except Exception as ex:
            print("error cerrando un socket ", ex)

    def write_message(self, msg):
        #msg = msg+"\r\n"
        self.the_socket.send(msg.encode('utf-8'))

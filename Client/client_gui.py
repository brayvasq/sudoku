import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QMessageBox
from PyQt5 import uic
import threading
from Client.models.sudoku_client import sudoku_client


class ventana(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        uic.loadUi("client_sudoku.ui",self)

        self.setWindowTitle("SUDOKU!!")
        self.txt_host.setText("localhost")

        #self.cadena = "0,0,6,0,3,0,7,0,8,0,3,0,0,0,0,0,0,1,2,0,0,0,0,0,6,0,0,1,0,0,3,5,0,0,0,6,0,7,9,0,4,0,1,5,0,5,0,0,0,1,7,0,0,4,0,0,2,0,0,0,0,0,7,6,0,0,0,0,0,0,8,0,4,0,7,0,6,0,2,0,0"

        #self.cadena = "0,2,0,8,9,4,0,0,0,8,0,5,3,6,1,0,0,7,1,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,2,3,0,7,0,0,0,0,0,6,0,6,4,0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,4,1,5,7,0,8,0,0,0,9,2,8,0,5,0"
        self.cadena = "0,0,1,0,0,9,7,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,5,0,1,4,3,0,5,0,0,0,4,0,0,6,8,7,0,0,0,0,0,9,2,6,0,0,2,0,0,0,7,0,3,6,9,0,8,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,5,1,0,0,9,0,0"
        #self.cadena = "4,0,0,2,7,0,6,0,0,7,9,8,1,5,6,2,3,4,0,2,0,8,4,0,0,0,7,2,3,7,4,6,8,9,5,1,8,4,9,5,3,1,7,2,6,5,6,1,7,9,2,8,4,3,0,8,2,0,1,5,4,7,9,0,7,0,0,2,4,3,0,0,0,0,4,0,8,7,0,0,2"
        #self.cadena = "0,0,6,0,3,0,7,0,8,0,3,0,0,0,0,0,0,1,2,0,0,0,0,0,6,0,0,1,0,0,3,5,0,0,0,6,0,7,9,0,4,0,1,5,0,5,0,0,0,1,7,0,0,4,0,0,2,0,0,0,0,0,7,6,0,0,0,0,0,0,8,0,4,0,7,0,6,0,2,0,0"

        self.__init_tabla()

        self.list_client = []

        self.list_solve = []

        self.dict_clients = {"1":0,"2":0,"3":0}

        self.__init_clients()

        self.__cambiar_colores()

        self.btn_get_str.clicked.connect(self.__obtener_cadena)

        self.btn_conexion.clicked.connect(self.__conectar)

        self.btn_solve.clicked.connect(self.__solve)
        self.btn_solve_all.clicked.connect(self.__solve_all)

    def __init_tabla(self):
        k = 0
        cad = self.cadena.replace(",","")
        for i in range(0, 9):
            for j in range(0, 9):
                w = self.tbl_sudoku.setCellWidget(i, j, QLineEdit(cad[k]))
                k+=1

    def __init_clients(self):
        for i in range(0,3):
            self.list_client.append(None)

        for i in range(0,5):
            self.list_solve.append(0)

    def __cambiar_colores(self):
        self.cadena = ""
        self.items = []
        for i in range(0, 9):
            for j in range(0, 9):
                w = self.tbl_sudoku.cellWidget(i, j)
                if w.text() != "0":
                    w.setReadOnly(True)
                    w.setStyleSheet("color:red;")


    def __solve_all(self):
        serv = self.cbx_servers.currentText()
        nserv = int(serv) - 1
        method = int(self.cbx_method.currentText())
        try:

            solucion = True
            while(not self.__resuelto() and solucion):
                self.__obtener_cadena()
                resp = self.__find_resp(1,self.cadena,1)
                if(not resp):
                    resp = self.__find_resp(2,self.cadena,2)
                    if(not resp):
                        resp = self.__find_resp(3,self.cadena,3)
                        if (not resp):
                            solucion = False
                            self.lbl_status.setText("no hay solución")

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("No se pudo realizar la operacion")
            msg.exec_()

    def __find_resp(self,nserv,str_matriz,method):
        booleano = False
        self.list_client[nserv].request_solve(self.cadena, method)
        resp = ""
        while not self.list_client[nserv].bandera:
            pass
        resp = self.list_client[nserv].respuesta
        self.txt_response.setText(resp)

        ################ ubicando en la matriz  ##################
        lista_valores = resp.split(" ")
        print(lista_valores)

        pos_general = -1
        fila = -1
        colum = -1
        val = ""

        for i in range(1,len(lista_valores)):
            self.dict_clients[lista_valores[0]] += 1
            #print(self.dict_clients)
            print("---------------> El indice es : ",i)
            if(i%2 == 0):
                ## Numero
                val = lista_valores[i]
                print("obtengo valor",val)
                w = self.tbl_sudoku.cellWidget(fila, colum)
                w.setText(val)
                w.setStyleSheet("color:green;")

                val = ""
                pos_general = -1
                booleano = True
                self.list_solve[method - 1] += 1
                if method == 1:
                    self.lbl_serv_1.setText(str(self.list_solve[0]))
                elif method == 2:
                    self.lbl_serv_2.setText(str(self.list_solve[1]))
                elif method == 3:
                    self.lbl_serv_3.setText(str(self.list_solve[2]))
            else:
                ## valor
                pos_general = int(lista_valores[i])
                fila = pos_general/9
                colum = pos_general%9
                print("Posicion x : ",colum," y : ",fila )




        return booleano

    def __solve(self):
        self.__obtener_cadena()
        serv = self.cbx_servers.currentText()
        nserv = int(serv) - 1
        method = int(self.cbx_method.currentText())
        try:

            if not self.__resuelto():
                self.__find_resp(nserv,self.cadena,method)

        except Exception as ex:
            print("Erorr")
            '''msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("No se pudo realizar la operacion"+str(ex))
            msg.exec_()'''

    def __resuelto(self):
        resp = True
        for i in range(0, 9):
            if not resp:
                break
            for j in range(0, 9):
                if not resp:
                    break
                w = self.tbl_sudoku.cellWidget(i, j)
                if w.text() != "0":
                    resp = False

        if resp:
            self.lbl_status.setText("resuelto")

        return resp

    def __conectar(self):
        host = self.txt_host.text()
        port = self.txt_port.text()
        serv = self.cbx_servers.currentText()

        if host != "" or port != "":
            port = int(port)
            nserv = int(serv) - 1
            try:
                self.list_client[nserv] = sudoku_client(host,port)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setText("Conexion realizada con exito")
                msg.exec_()
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setText("No se pudo realizar la conexión")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Indique el host y el puerto")
            msg.exec_()



    def __obtener_cadena(self):
        self.cadena = ""
        for i in range(0,9):
            for j in range(0,9):
                w = self.tbl_sudoku.cellWidget(i, j)
                self.cadena += w.text() + ","
        self.cadena = self.cadena[0:len(self.cadena) - 1]
        self.txa_str.setText(self.cadena)



if __name__ == "__main__":
    # INSTANCIA DE LA APLICAION PRINCIPAL
    app = QApplication(sys.argv)
    # INSTANCIA DE LA CLASE VENTANA
    _ventana = ventana()
    # SE MUESTRA LA VENTANA
    _ventana.show()

    # SE EJECUTA LA APP
    app.exec_()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QMessageBox
from PyQt5 import uic
import threading
from models.client import Client


class Window(QMainWindow):
    """
    GUI client to interact with the sudoku

    ...
    Methods
    -------
    __init_table()
        Setup the UI matrix to represent the sudoku

    __init_clients()
        Setup UI options for clients and algorithms

    __switch_colors()
        Setup UI sudoku colors and values

    __solve_all()
        Action to request a full sudoku solve

    __find_resp()
        Stablish a connection and ask for a solution

    __solve()
        Ask for a single value to place in the matrix

    __solved()
        Checks if a sudoku is solved.

    __connect()
        Creates a new client and a new connection.

    __get_string()
        Get the representative sudoku string and puts it in a text area.
    """

    def __init__(self):
        """
        UI constructor
        """
        QMainWindow.__init__(self)

        # Loading the client ui layout (It was built using QtDesigner)
        uic.loadUi("client_sudoku.ui", self)

        self.setWindowTitle("SUDOKU!!")
        self.txt_host.setText("localhost")

        # self.cadena = "0,0,6,0,3,0,7,0,8,0,3,0,0,0,0,0,0,1,2,0,0,0,0,0,6,0,0,1,0,0,3,5,0,0,0,6,0,7,9,0,4,0,1,5,0,5,0,0,0,1,7,0,0,4,0,0,2,0,0,0,0,0,7,6,0,0,0,0,0,0,8,0,4,0,7,0,6,0,2,0,0"

        # self.cadena = "0,2,0,8,9,4,0,0,0,8,0,5,3,6,1,0,0,7,1,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,2,3,0,7,0,0,0,0,0,6,0,6,4,0,0,0,9,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,4,1,5,7,0,8,0,0,0,9,2,8,0,5,0"
        self.sudoku_str = "0,0,1,0,0,9,7,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,5,0,1,4,3,0,5,0,0,0,4,0,0,6,8,7,0,0,0,0,0,9,2,6,0,0,2,0,0,0,7,0,3,6,9,0,8,0,0,0,0,0,0,0,0,0,0,0,0,7,0,0,5,1,0,0,9,0,0"
        # self.cadena = "4,0,0,2,7,0,6,0,0,7,9,8,1,5,6,2,3,4,0,2,0,8,4,0,0,0,7,2,3,7,4,6,8,9,5,1,8,4,9,5,3,1,7,2,6,5,6,1,7,9,2,8,4,3,0,8,2,0,1,5,4,7,9,0,7,0,0,2,4,3,0,0,0,0,4,0,8,7,0,0,2"
        # self.cadena = "0,0,6,0,3,0,7,0,8,0,3,0,0,0,0,0,0,1,2,0,0,0,0,0,6,0,0,1,0,0,3,5,0,0,0,6,0,7,9,0,4,0,1,5,0,5,0,0,0,1,7,0,0,4,0,0,2,0,0,0,0,0,7,6,0,0,0,0,0,0,8,0,4,0,7,0,6,0,2,0,0"

        self.__init_table()

        self.list_client = []

        self.list_solve = []

        self.dict_clients = {"1": 0, "2": 0, "3": 0}

        self.__init_clients()

        self.__switch_colors()

        self.btn_get_str.clicked.connect(self.__get_string)

        self.btn_conexion.clicked.connect(self.__connect)

        self.btn_solve.clicked.connect(self.__solve)
        self.btn_solve_all.clicked.connect(self.__solve_all)

    def __init_table(self):
        """
        Setup the UI matrix to represent the sudoku
        """
        k = 0
        cad = self.sudoku_str.replace(",", "")
        for i in range(0, 9):
            for j in range(0, 9):
                w = self.tbl_sudoku.setCellWidget(i, j, QLineEdit(cad[k]))
                k += 1

    def __init_clients(self):
        """
        Setup UI options for clients and algorithms
        """
        for i in range(0, 3):
            self.list_client.append(None)

        for i in range(0, 5):
            self.list_solve.append(0)

    def __switch_colors(self):
        """
        Setup UI sudoku colors and values
        """
        self.sudoku_str = ""
        self.items = []

        for i in range(0, 9):
            for j in range(0, 9):
                w = self.tbl_sudoku.cellWidget(i, j)
                if w.text() != "0":
                    w.setReadOnly(True)
                    w.setStyleSheet("color:red;")

    def __solve_all(self):
        """
        Action to request a full sudoku solve
        """
        serv = self.cbx_servers.currentText()
        nserv = int(serv) - 1
        method = int(self.cbx_method.currentText())
        try:

            solution = True
            while (not self.__solved() and solution):
                self.__get_string()
                resp = self.__find_resp(1, self.sudoku_str, 1)
                if (not resp):
                    resp = self.__find_resp(2, self.sudoku_str, 2)
                    if (not resp):
                        resp = self.__find_resp(3, self.sudoku_str, 3)
                        if (not resp):
                            solution = False
                            self.lbl_status.setText("Error: The sudoku doesn't have solution")

        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Error: Operation couldn't be performed")
            msg.exec_()

    def __find_resp(self, nserv, str_matrix, method):
        """
        Stablish a connection and ask for a solution

        Parameters
        ----------
        nserv : int
            Number of servers (algorithms)

        str_matrix : str
            The representative sudoku string

        method : int
            The algorithm to execute to solve the sudoku

        Return
        ------
            True if a response is obtained
        """
        result = False
        self.list_client[nserv].request_solve(self.sudoku_str, method)
        resp = ""

        while not self.list_client[nserv].flag:
            pass

        resp = self.list_client[nserv].response
        self.txt_response.setText(resp)

        ################ Places a value into the matrix  ##################
        values_list = resp.split(" ")
        print(values_list)

        pos_general = -1
        row = -1
        column = -1
        val = ""

        for i in range(1, len(values_list)):
            self.dict_clients[values_list[0]] += 1
            # print(self.dict_clients)
            print("---------------> The index is : ", i)
            if (i % 2 == 0):
                ## Numero
                val = values_list[i]
                print("Getting value", val)
                w = self.tbl_sudoku.cellWidget(row, column)
                w.setText(val)
                w.setStyleSheet("color:green;")

                val = ""
                pos_general = -1
                result = True
                self.list_solve[method - 1] += 1
                if method == 1:
                    self.lbl_serv_1.setText(str(self.list_solve[0]))
                elif method == 2:
                    self.lbl_serv_2.setText(str(self.list_solve[1]))
                elif method == 3:
                    self.lbl_serv_3.setText(str(self.list_solve[2]))
            else:
                ## Value
                pos_general = int(values_list[i])
                row = pos_general / 9
                column = pos_general % 9
                print("Position x : ", column, " y : ", row)

        return result

    def __solve(self):
        """
        Ask for a single value to place in the matrix
        """
        self.__get_string()
        serv = self.cbx_servers.currentText()
        nserv = int(serv) - 1
        method = int(self.cbx_method.currentText())

        try:

            if not self.__solved():
                self.__find_resp(nserv, self.sudoku_str, method)

        except Exception as ex:
            print("Error: The operation couldn't be performed")
            '''msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("No se pudo realizar la operacion"+str(ex))
            msg.exec_()'''

    def __solved(self):
        """
        Checks if a sudoku is solved.

        Return
        ------
            True if the sudoku is solved
        """
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
            self.lbl_status.setText("Info: Solved!")

        return resp

    def __connect(self):
        """
        Creates a new client and a new connection.
        """
        host = self.txt_host.text()
        port = self.txt_port.text()
        serv = self.cbx_servers.currentText()

        if host != "" or port != "":
            port = int(port)
            nserv = int(serv) - 1
            try:
                self.list_client[nserv] = Client(host, port)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setText("Info: Connection established")
                msg.exec_()
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setText("Error: Connection couldn't be established")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Error: Please specify host and port")
            msg.exec_()

    def __get_string(self):
        """
        Get the representative sudoku string and puts it in a text area.
        """
        self.sudoku_str = ""
        for i in range(0, 9):
            for j in range(0, 9):
                w = self.tbl_sudoku.cellWidget(i, j)
                self.sudoku_str += w.text() + ","
        self.sudoku_str = self.sudoku_str[0:len(self.sudoku_str) - 1]
        self.txa_str.setText(self.sudoku_str)


if __name__ == "__main__":
    # Creates an app
    app = QApplication(sys.argv)
    # Creates a window
    _window = Window()
    # Show the window
    _window.show()

    # Execute the app
    app.exec_()

class Matrix:
    """
    Util class with basic operations over sudoku matrix

    ...
    Methods
    -------
    @staticmethod\n
    build_matrix(sudoku_string: str)
        Returns an array of arrays (Matrix) built from a string

    @staticmethod\n
    print_matrix(matrix)
        Prints each array from a matrix

    @staticmethod\n
    to_list(matrix : str)
        Converts a sudoku str to an array

    @staticmethod
    to_str(matrix : [])
        Converts a sudoku array to string
    """

    @staticmethod
    def build_matrix(sudoku_string: str) -> []:
        """
        Returns an array of arrays (Matrix) built from a string

        Parameters
        ----------
        sudoku_string : str
                Sudoku representative string. It's separated using '-'

        Return
        ------
        An array of arrays representing a sudoku matrix
        """
        for i in range(17, len(sudoku_string), 18):
            sudoku_string = sudoku_string[0:i] + '-' + sudoku_string[i + 1:len(sudoku_string)]

        matrix = []

        for i in sudoku_string.split("-"):
            row = i.split(",")
            matrix.append(row)

        return matrix

    @staticmethod
    def print_matrix(matrix):
        """
        Prints each array from a matrix

        Parameters
        ----------
        matrix : []
                Array of arrays representing a sudoku matrix
        """
        for i in matrix:
            print(i)

    @staticmethod
    def to_list(matrix : str):
        """
        Converts a sudoku str to an array

        Parameters
        ----------
        matrix : str
            Sudoku representative string,
        """
        temp = matrix.split(",")
        return temp

    @staticmethod
    def to_str(matrix : []):
        """
        Converts a sudoku array to string

        Parameters
        ----------
        matrix : []
            Sudoku representative array,
        """
        temp = ""
        size = len(matrix)
        for i in range(0, size):
            if i != size - 1:
                temp += matrix[i] + ","
            else:
                temp += matrix[i]
        return temp

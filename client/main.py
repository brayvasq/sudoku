from models.client import Client

if __name__ == '__main__':
    matrix_p2 = "0,0,1,9,5,7,0,6,3,0,0,0,8,0,6,0,7,0,7,6,9,1,3,0,8,0,5,0,0,7,2,6,1,3,5,0,3,1,2,4,9,5,7,8,6,0,5,6,3,7,8,0,0,0,1,0,8,6,0,9,5,0,7,0,9,0,7,1,0,6,0,8,6,7,4,5,8,3,0,0,0"
    matrix_p = "0,0,4,0,0,6,0,2,0,0,0,7,8,0,0,9,1,0,0,0,0,0,0,0,3,0,8,0,1,8,3,0,0,2,0,0,3,0,0,7,8,9,0,0,1,0,0,9,0,0,1,0,6,0,8,0,3,0,0,0,5,0,0,0,4,5,0,0,3,6,0,0,0,2,6,5,0,0,1,0,0"
    client = Client("localhost", 25000)
    client.request_solve(matrix_p2, 3)
    solv =""
    while not client.flag:
        pass

    solv = client.response
    print("Response: ", solv)
    print("Column: ", 18 % 9, " Row: ", 18 / 9)



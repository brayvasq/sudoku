
# Sudoku project
Sudoku solver using Python, PyQt5 and sockets.

> :warning: This project was created in the year 2017-1 with educational/study purposes only. 

| Lenguaje | Versión        | SO                |
| -------- | -------------- | ----------------- |
| Python   | Python 3.6.9   | Ubuntu 18.04.1    |

## Algorithms
- Unique Position (http://www.playsudoku.biz/posicion-unica.aspx)
- Unique candidates (http://www.playsudoku.biz/candidatos-unicos.aspx)
- Candidate lines (http://www.playsudoku.biz/lineas-de-candidatos.aspx)
- Naked couples (http://www.playsudoku.biz/lineas-de-candidatos.aspx)

## Run project
```bash
# Creating environment
virtualenv .
# Installing dependencies
# Installing dependencies
pip install -r requirements.txt

# Running Server
cd server/

## It will ask the port number
## >> 25000
python main.py

# Running client
cd client/

## Running CLI example.
## It will execute an example predefined. Also, uses the port 25000 by default
python main.py

## Running UI
## It will execute an Graphical UI client, built in PyQt5.
python ventana.py
```

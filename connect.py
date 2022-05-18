import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\franz\Documents\Database1.accdb;')
    print("Database is connected")

except pyodbc.Error:
    print("Database is NOT connected")

import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\sayom\OneDrive\Documents\Database1.accdb;')
    print("Database is connected")

    user_id = 10

    database = connection.cursor()
    database.execute('DELETE from Table1 where id=?', (user_id))
    connection.commit()

    print("Data is deleted")

except pyodbc.Error:
    print("Database is NOT connected")

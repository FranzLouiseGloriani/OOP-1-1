import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\franz\Documents\Database1.accdb;')
    print("Database is connected")

    user_id = 11
    Fullname = "Franz Louise B. Gloriani"
    Age = 19
    Course = "BSCPE"
    Address = "Cavite"
    Grade = 100
    database = connection.cursor()
    database.execute('UPDATE Table1 SET Fullname=? WHERE id=?', (Fullname, user_id))
    database.execute('UPDATE Table1 SET Age=? WHERE id=?', (Age, user_id))
    database.execute('UPDATE Table1 SET Course=? WHERE id=?', (Course, user_id))
    database.execute('UPDATE Table1 SET Address=? WHERE id=?', (Address, user_id))
    database.execute('UPDATE Table1 SET Grade=? WHERE id=?', (Grade, user_id))
    connection.commit()
    print("Database is updated")

except pyodbc.Error:
    print("Database is NOT connected")

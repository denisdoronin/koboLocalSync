import sqlite3

sqliteConnection = sqlite3.connect('.kobo\\KoboReader.sqlite')
cursor = sqliteConnection.cursor()

readShelfSQL = "SELECT Name FROM Shelf"
cursor.execute(readShelfSQL)
record = cursor.fetchall()

for index in record:
    print(index)


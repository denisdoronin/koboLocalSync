import sqlite3
import uuid
from datetime import datetime
import sys

#create new "Collection" in Kobo database
def KoboCreateCollection(connectionString, collectionName):
    sqliteConnection = sqlite3.connect(connectionString)
    cursor = sqliteConnection.cursor()

    #check if collection already exists
    findCollectionSQL = "SELECT Name FROM Shelf WHERE Name = '" + collectionName + "'"
    row = cursor.execute(findCollectionSQL).fetchone()
    if row is not None:
        print(row)
        print("Collection '", collectionName, "' already exists. No need to create.")
    
    #create new collection
    else: 
        dateTime = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        id = str(uuid.uuid1())
        insert2ShelfSQL = "INSERT INTO Shelf (CreationDate, Id, InternalName, LastModified, Name,"\
                        +"Type,_IsDeleted, _IsVisible, _IsSynced, _SyncTime, LastAccessed) "\
                        +"VALUES ("\
                        + "'" + dateTime + "','" + id + "','" + collectionName + "','" + dateTime + "','" + collectionName\
                        + "','UserTag','false', 'true', 'true','" + dateTime + "','" + dateTime + "');"
    
        try:
            cursor.execute(insert2ShelfSQL)
            sqliteConnection.commit()
            print("Collection: '", collectionName, "' created successfully.")
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
    
    cursor.close()
    sqliteConnection.close()
    return
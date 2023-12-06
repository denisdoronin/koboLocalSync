import os
import shutil

#get list of all folders under "shelfpath" excluding files
#return list of folders
def readLocalShelfFolders(shelfpath): 
    folders = []
    for folder in os.listdir(shelfpath):
        absPath = os.path.abspath(shelfpath+folder)
        if os.path.isdir(absPath) == True: 
            folders.append(folder)

    print("\nList of local folders under", shelfpath, ":\n    ", folders, "\n")
    return folders

def listFilesInFolders(folders, shelfpath):
    for folder in folders:
        print("Folder: ", folder)
        print("  Files: ", os.listdir(shelfpath+folder))
    return

#get list of files in supported formats from folder
def getBooksFromFolder(path, supportedFormats):
    files = os.listdir(path)
    books = []
    for file in files:
        name, extension = os.path.splitext(file)
        if extension.replace(".","").upper() in supportedFormats:
            books.append(file)
    return books


#create new folder on Kobo device. new Folder Name == new Collection Name
def createFolder(collectionName, koboRootFolder):
    print("Creating folder ", collectionName, " on Kobo.")
    os.makedirs(koboRootFolder+collectionName,mode=0o777,exist_ok=True)
    return

#copy file to Kobo device
def copyFile(src, dst):
    print("Adding book file to Kobo: ", dst)
    shutil.copyfile(src, dst)
    return
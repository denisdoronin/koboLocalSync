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

    print("\nSubfolders under folder with books:\n  ", folders)
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
    os.makedirs(koboRootFolder+collectionName,mode=0o777,exist_ok=True)
    return

#copy file to Kobo device
def copyFile(collectionName, fileName, localFolder, koboRootFolder):
    #shutil.copyfile(localFolder+collectionName+fileName, koboRootFolder+collectionName)
    shutil.copyfile("books\\06-May-2023\\Budzhold_Shalion_1_Proklyatie-Shaliona.191641.fb2.epub", "kobo\\06-May-2023\\Budzhold_Shalion_1_Proklyatie-Shaliona.191641.fb2.epub")
    return
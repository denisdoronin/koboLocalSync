import os

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



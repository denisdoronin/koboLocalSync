import yaml
import os

#read file with settings (kobo file system details, books location on local PC)
def readSettings(settingsFile):
    with open(settingsFile, "r") as stream:
        try:
            settings = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print ("ERROR: Can't open settings file: ", exc)
            exit()
        finally:
            stream.close()

    print("Settings:") 
    print("  Kobo database path: ", settings['kobo']['path'])
    print("  Kobo database file: ", settings['kobo']['databasefile'])
    print("  Local folder with books: ", settings['local']['shelfpath'])

    return settings

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



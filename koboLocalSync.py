from readsettings import readSettings
from filesystemutils import readLocalShelfFolders, listFilesInFolders, createFolder, copyFile
from sqlutils import KoboCreateCollection

def main():
    settings = readSettings("settings.yaml")
    #KoboCreateCollection(settings['kobo']['dbfile'], "Test Test 5")
    
    folders = readLocalShelfFolders(settings['local']['shelfpath'])
    createFolder(folders[0], settings['kobo']['rootfolder'])
    #copyFile(folders[0]+"\\", "Budzhold_Shalion_1_Proklyatie-Shaliona.191641.fb2.epub", settings['local']['shelfpath'], settings['kobo']['rootfolder'])



    #listFilesInFolders(folders, settings['local']['shelfpath'])
    return

main()

from readsettings import readSettings
from filesystemutils import readLocalShelfFolders
from filesystemutils import listFilesInFolders
from sqlutils import KoboCreateCollection

def main():
    settings = readSettings("settings.yaml")
    KoboCreateCollection(settings['kobo']['dbfile'], "Test Test 5")
    
    #folders = readLocalShelfFolders(settings['local']['shelfpath'])
    #listFilesInFolders(folders, settings['local']['shelfpath'])
    return

main()

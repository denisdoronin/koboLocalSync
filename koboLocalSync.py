from filesystemutils import readSettings
from filesystemutils import readLocalShelfFolders
from filesystemutils import listFilesInFolders
from sqlutils import KoboCreateCollection

def main():
    settings = readSettings("settings.yaml")
    connectionString = settings['kobo']['path']+settings['kobo']['databasefile']
    KoboCreateCollection(connectionString, "Test Test 4")
    
    #folders = readLocalShelfFolders(settings['local']['shelfpath'])
    #listFilesInFolders(folders, settings['local']['shelfpath'])
    return

main()

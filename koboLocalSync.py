from filesystemutils import readSettings
from filesystemutils import readLocalShelfFolders
from filesystemutils import listFilesInFolders

def main():
    settings = readSettings("settings.yaml")
    folders = readLocalShelfFolders(settings['local']['shelfpath'])
    listFilesInFolders(folders, settings['local']['shelfpath'])
    return

main()

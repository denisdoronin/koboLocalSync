from readsettings import readSettings
from filesystemutils import readLocalShelfFolders, listFilesInFolders, getBooksFromFolder, createFolder, copyFile
from sqlutils import KoboCreateCollection

def main():
    # 1. read settings
    settings = readSettings("settings.yaml")
    shelfPath = settings['local']['shelfpath']
    shelfPath = shelfPath if shelfPath[-1] == '\\' else shelfPath + '\\'
    koboRoot = settings['kobo']['rootfolder']
    koboRoot = koboRoot if koboRoot[-1] == '\\' else koboRoot + '\\'
    koboDB = koboRoot + settings['kobo']['dbfile']
    supportedFormats = settings['kobo']['supportedformats'].replace(" ", "").upper().split(",")

    # 2. read local folders
    folders = readLocalShelfFolders(shelfPath)


    # 3. For every folder
    for folder in folders:                
        # 4. Check it's not empty and content at least 1 file of supported format
        books = getBooksFromFolder(shelfPath + folder, supportedFormats)
        
        if len(books) != 0:
            # 5. Create folder on device
            createFolder(folder, koboRoot)
            # 6. Create collection (foldername) in DB
            KoboCreateCollection(koboDB, folder)
            # 7. Copy every supported file from local folder to on-device folder
            for book in books:
                copyFile(shelfPath + folder + '\\' + book, koboRoot + folder + '\\' + book)

        
        
        
        # 8. Assotiate every copied file with collection in DB


    #KoboCreateCollection(settings['kobo']['dbfile'], "Test Test 5")
    
    
    #createFolder(folders[0], settings['kobo']['rootfolder'])
    #copyFile(folders[0]+"\\", "Budzhold_Shalion_1_Proklyatie-Shaliona.191641.fb2.epub", settings['local']['shelfpath'], settings['kobo']['rootfolder'])



    #listFilesInFolders(folders, settings['local']['shelfpath'])
    return

main()

import yaml

#read file with settings (kobo file system details, books location on local PC)
def readSettings(settingsFile):
    settings = {}
    with open(settingsFile, "r") as stream:
        try:
            settings = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print ("ERROR: Can't open settings file: ", exc)
            exit()
        finally:
            stream.close()

    print("Settings:") 
    print("    Kobo database path: ", settings['kobo']['dbfile'])
    print("    Kobo root folder: ", settings['kobo']['rootfolder'])
    print("    Kobo supported formats: ", settings['kobo']['supportedformats'])
    print("    Local folder with books: ", settings['local']['shelfpath'])

    return settings

# koboLocalSync
Copies local folders structure and books in these folders from your PC to Kobo book reader. 
Creates collections with the same names as folders, registeres books from folders in new collections

Existing folders and books will NOT be over written
Any files, books, collections will not be deleted from Kobo.

Nested folders are not supported.

RISKS: This software adds records to Kobo device internal DB. Use at your own risk.

RUN: koboLocalSync.py


SETTING.YAML:

kobo: #kobo device settings
    dbfile: .kobo\KoboReader.sqlite #path to kobo database file. Likely should say like this.
    rootfolder: #root folder of Kobo device. For windows based PC it should be something like e:\
    supportedformats: EPUB, EPUB3, FlePub, PDF, MOBI, JPEG, GIF, PNG, BMP, TIFF, TXT, HTML, RTF, CBZ, CBR, FB2
local: #local PC settings
    shelfpath: books\ #location of foldes with your books

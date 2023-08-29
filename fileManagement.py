import os
import shutil

def getFileExtention(file):
    try:
        return str(file[-3]+file[-2]+file[-1])
    except IndexError:
        return

def makeFolders(ISO, pictrues, Zips):
    try:
        os.mkdir(ISO)
        print('(+) Succesfully made ISO folder')
    except FileExistsError:
        print('(?) '+ISO+' Already exist')
    try:
        os.mkdir(pictrues)
        print('(+) Succesfully made Images folder')
    except FileExistsError:
        print('(?) '+pictrues+' Already exist')
    try:
        os.mkdir(Zips)
        print('(+) Succesfully made Zips folder')
    except FileExistsError:
        print('(?) '+Zips+' Already exist')
    
def putFileInIsoFolder(file, pathToFile, pathToIsoFolder):
    shutil.move(pathToFile+'\\'+file,pathToIsoFolder)
    print('(+) '+file+' moved successfuly into ISO folder')
    
def putFileInImagesFolder(file, pathToFile, pathToImagesFolder):
    shutil.move(pathToFile+'\\'+file,pathToImagesFolder)
    print('(+) '+file+' moved successfuly into Images folder')

def putFileInZipFolder(file, pathToFile, pathToZipFolder):
    shutil.move(pathToFile+'\\'+file,pathToZipFolder)
    print('(+) '+file+' moved successfuly into Zip folder')

desktop = 'C:\\Users\\siemi\\Desktop'
isoFolder = 'C:\\Users\\siemi\\Desktop\\IsoImages'
pictrues = 'C:\\Users\\siemi\\Desktop\\Images'
zipFolder = 'C:\\Users\\siemi\\Desktop\\Images'
fileList = os.listdir(desktop)

makeFolders(isoFolder, pictrues, zipFolder)

for file in fileList:
    if(getFileExtention(file) == 'iso'):
        putFileInIsoFolder(file,desktop,isoFolder)
    elif(getFileExtention(file) == 'png' or getFileExtention(file) == 'jpg'):
        putFileInImagesFolder(file,desktop,pictrues)
    elif(getFileExtention(file) == 'zip' or getFileExtention(file) == '.gz' or getFileExtention(file) == 'tar' or getFileExtention(file) == 'rar'):
        putFileInZipFolder(file,desktop,zipFolder)
    else:
        print('(-) Cant find place for this file: '+file)
    
    
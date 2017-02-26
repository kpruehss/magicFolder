import os, glob
from shutil import copyfile
# get the current directory to run script on
# curDir = os.getcwd()
# testing scandir fucntionality. Will be removed later
# with os.scandir(curDir) as list:
#     for entry in list:
#         if not entry.name.startswith('.') and entry.is_file():
#             filelist = (os.path.splitext(entry.name))
#             print(filelist[1])

#             for file in filelist:
#                 key = 'Pictures'
#                 if file[1] == '.jpeg':
#                    fileDict[key] = file
#                 print(fileDict)
def getFiles():
    fileDict = {"Documents":[], "Pictures":[], "Music":[], "Videos":[], "Archives":[]}

    documentTypes = ('*.txt', '*.rtf', '*.doc', '*.docx', '*.pdf', '*.odt', '*.ods', '*.xls', '*.xlsx')

    imageTypes = ('*.jpg', '*.jpeg', '*.png', '*.gif', '*.tiff', '*.bmp', '*.svg',)

    musicTypes = ('*.mp3', '*.wav', '*.aac', '*.wma', '*.m4a', '*.m4b',)

    videoTypes = ('*.vob', '*.wmv', '*.swf', '*.mov', '*.mpg', '*.mp4', '*.divx',)

    archiveTypes = ('*.zip', '*.tar', '*.tar.*', '*.7z', '*.7za', '*.rar', '*.pkg.*', '*.msi')
        
    documents = []
    images = []
    music = []
    video = []
    archives = []

    for files in documentTypes:
        documents.extend(glob.iglob(files))
   
    for files in imageTypes:
        images.extend(glob.iglob(files))
    
    for files in musicTypes:
        music.extend(glob.iglob(files))

    for files in videoTypes:
        video.extend(glob.iglob(files))

    for files in archiveTypes:
        archives.extend(glob.iglob(files))

    fileDict["Documents"].extend(documents)
    fileDict["Pictures"].extend(images)
    fileDict["Music"].extend(music)
    fileDict["Videos"].extend(video)
    fileDict["Archives"].extend(archives)
    
    return fileDict

files = getFiles()

# for each in files:
#     if each == 'Documents':
#         print(each)

def moveFiles(files):
    for each in files['Pictures']:
        os.rename(each, f'/home/kartug/Pictures/{each}')
        print(f"{os.getcwd()}/{each} ----> /home/kartug/Pictures/{each}")

moveFiles(files)
import os

# get the current directory to run script on
curDir = os.getcwd()
fileDict = {}
# testing scandir fucntionality. Will be removed later
with os.scandir(curDir) as list:
    for entry in list:
        if not entry.name.startswith('.') and entry.is_file():
            filelist = (os.path.splitext(entry.name))
            #print(filelist[1])

            for file in filelist:
                key = 'Pictures'
                if file[1] == '.jpeg':
                   fileDict[key] = file
                print(fileDict)
                fileDict.
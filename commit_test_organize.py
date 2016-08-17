import os
fileCount = 0
extension = (".exe")

for folderName, subfolders, filenames in os.walk('Z:\\Users\\James\\Desktop'):


    for i in filenames:
        if i.endswith(extension):
            print (i)
            fileCount += 1
print ("The number of ", extension, "files is", fileCount)


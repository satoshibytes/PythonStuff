#A simple script to move file spread across subdirs to a single folder based on file extension.
#Import modules
import os
from posixpath import splitext
import shutil

#Set variables and folders
srcFolder='G:\Western Fonts' #Source folder - no trailing slash
destFolder='' #Destination folder - no trailing slash
approvedExtensions=['.ext1','.ext2'] #Extensions of files to move - must have a dot with the extension

#Operational variables
folderSubList=[]
copyCount=0
notCopiedCount=0

#First get a list of folders
for path in os.listdir(srcFolder): #Gather the list of folders
    if (os.path.isdir and path[0] is not '.'): #Ignore hidden folders and files beginning with .
        folderSubList.append(srcFolder+"\\"+path) #Append the list and place it in a list
        #print (path)

#Now look in each folder to move files
for thisFolder in folderSubList: #Iterate through the folder list
    files = os.listdir(thisFolder) #list the files
    for file in files: #iterate through the file list
        fileSplit= splitext(file) #Split the file to get the extension
        extension=fileSplit[1] #Extension variable
        if extension in approvedExtensions: #verify the extension
            print("-> File moved: " + file)
            shutil.copy2(thisFolder+"\\"+file,destFolder+"\\"+file)
            copyCount+=1
        else:
            print("<- File not moved: " +file)
            notCopiedCount+=1

        #print(os.path.isfile(thisFolder))

print ("Total files moved: "+str(copyCount) + " | Not moved: "+str(notCopiedCount))

#!/usr/bin/env python3

import os
import re
import datetime
import time
import math
import shutil
import sys

targetDirectory = ""
listOfFiles = []


def showSelectedFiles():
    print("Total files selected: " + str(len(listOfFiles)))
    if(len(listOfFiles) == 0):
        return
    else:
        for i in os.listdir(targetDirectory):
            print(i)
            print('\n')


def setTargetDirectory():
    targetDirectory = input("Enter target directory: ")
    print("Target directory selected")


def createDummyFiles():
    noOfFilesRequired = int(input("Enter the no. of dummy files required: "))
    startFileNameWith = input("Enter the file name to append to each file name: ")
    fileName = startFileNameWith
    fileMode = "w+"
    noOfFilesRequired += 1
    for i in range(1, noOfFilesRequired):
        open(fileName + str(i), fileMode)

# renames every file inside that directory to a specified name with a
# sequence number
def bulkRename():
    if(len(listOfFiles) == 0):
        print("0 files selected")
        return

    if(targetDirectory == ""):
        print("Inside current directory")
    else:
        print("In directory -> " + targetDirectory)
    finalName = input("Rename selected file to: ")
    i = 1
    for initialName in os.listdir(targetDirectory):
        os.rename(targetDirectory + "/" + initialName,
                  targetDirectory + "/" + finalName + str(i))
        i += 1
    print("Renamed " + len(listOfFiles) + " files")


# renames selected files inside that directory to a specified name
def renameSeletecFiles():
    if(len(listOfFiles) == 0):
        print("0 files selected")
        return

    if(targetDirectory == ""):
        print("Inside current directory")
    else:
        print("In directory -> " + targetDirectory)

    finalName = input("Rename selected files to: ")
    i = 1
    for initialName in listOfFiles:
        os.rename(targetDirectory + "/" + initialName,
                  targetDirectory + "/" + finalName)
        i += 1
    print("Renamed " + len(listOfFiles) + " files")

# takes list of files and a matching string, and filters that list of
# files that contains with this string
def filterFilesListByString():
    inputString = input("Enter a string to search in filenames: ")
    index = 0
    while index < len(listOfFiles):
        if not(re.search(".*" + inputString + ".*", listOfFiles[index])):
            del(listOfFiles[index])
        else:
            index += 1
    print("Selected " + str(len(listOfFiles)) + " files")

def filterFilesListByType():
    inputString = input("Enter a the type of files to be selected: ")
    inputString = "." + inputString
    index = 0
    while index < len(listOfFiles):
        if not(re.search(".*" + inputString + ".*", listOfFiles[index])):
            del(listOfFiles[index])
        else:
            index += 1
    print("Selected " + str(len(listOfFiles)) + " files")


def filterFilesListByTime():
    timeFrom = input("Time from: ")
    timeUpto = input("Time upto: ")
    with os.scandir(directory) as dir_entries:
        for entry in dir_entries:
            createDate = datetime.datetime.fromtimestamp(
                int(entry.stat().st_ctime))
            if(createDate <= timeUpto and createDate >= timeFrom):
                continue
            else:
                listOfFiles.remove(entry.name)
    print("Selected " + str(len(listOfFiles)) + " files")


def filterFilesListBySize():
    minSize = int(input("Minimum size: "))
    maxSize = int(input("Maximum size: "))
    with os.scandir(directory) as dir_entries:
        for entry in dir_entries:
            currSize = entry.stat().st_size
            if(currSize <= maxSize and currSize >= minSize):
                continue
            else:
                listOfFiles.remove(entry.name)
    print("Selected " + str(len(listOfFiles)) + " files")


# use src and des without "/" at front e.g 'user/jonty/folder/des/file.txt'
def copyPasteSelectedFiles():
    if(len(listOfFiles) == 0):
        print("0 files selected")
        return

    src = input("Enter the source directory: ")
    des = input("Enter the destination directory: ")
    
    s = ""
    for i in listOfFiles:
        s = src + "/" + i
        shutil.copy2(s, des)
    print("Copied " + str(len(listOfFiles)) + " files")

# delete selected files...Duh!!
def deleteSelectedFiles():
    if(len(listOfFiles) == 0):
        print("0 files selected")
        return

    for i in listOfFiles:
        s = targeDirectory + "/" + i
        os.remove(s)
    print("Deleted " + str(len(listOfFiles)) + " files")

# move selected files
def moveSelectedFiles():
    if(len(listOfFiles) == 0):
        print("0 files selected")
        return

    src = input("Enter the source directory: ")
    des = input("Enter the destination directory: ")

    s = ""
    for i in listOfFiles:
        s = src + i
        d = des + i
        shutil.move(s, d)
    print("Moved " + str(len(listOfFiles)) + " files")


def main():
    print("\t**********************************************")
    print("\t************  Bulk File Handler!  *************")
    print("\t**********************************************")

    # 1. Select or filter the list of files on which you want to perform the
    # actions

    # 2. Apply action to selected files

    # 3. Done


if __name__ == "__main__":
    globals()[sys.argv[1]]()

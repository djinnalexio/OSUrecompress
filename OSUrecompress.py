#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from os.path import isdir, join
import argparse 
import shutil

help_text = """

Compress beatmaps folders back to '.osz' files.
"""

#Initialize parser
parser = argparse.ArgumentParser(prog="OSUrecompress", description= help_text)

#Add arguments
parser.add_argument("--source", help = "Path to the Source Directory that contains uncompressed beatmaps/skins")
parser.add_argument("--destination", help = "Path to the Output Directory where compressed OSZ/OSK files will be generated")
parser.add_argument("-b", "--beatmaps", action="store_true", help = "Beatmap mode to compress beatmap folders into '.OSZ' files")
parser.add_argument("-s", "--skins", action="store_true", help = "Skin mode to compress skin folders into '.OSK' files")
parser.add_argument("-R", "--remove", action="store_true", help = "Deletes source files after compression to save space.\n!!!DELETION IS IRREVERSIBLE!!!")


#Read arguments from command line
args = parser.parse_args()

#pass arguments to variables
sourceDir = args.source
destDir = args.destination
deleteSources = args.remove


#function to check which was selected
def verifyMode():
    if args.beatmaps & args.skins:
        print("Please choose only one mode: '--beatmaps' or '--skins'")
        exit()
    elif args.beatmaps:
        return "Songs", "beatmap", ".osz"
    elif args.skins:
        return "Skins", "skin", ".osk"
    else:
        print("No mode was selected. Please use '-b' to compress OSU beatmaps or '-s' to compress OSU skins.")
        exit()


#function to check that input and output directories exist
def checkDirs(dirName,inputDir,outputDir):
    dirList = [inputDir,outputDir]
    dirLabelList = ["source", "destination"]

    for i in range(0,2):
        if not dirList[i]:#if path is not given
            print ("The {0} directory was not given! Please use '--{1} followed by your source directory.".format(
                dirLabelList[i].upper(), dirLabelList[i]))
            exit()
        
        elif not isdir(dirList[i]):#if path is not an existing directory
            print ("The {0} directory does not exist! Check that the path to your {1} directory is correct.".format(
                dirLabelList[i].upper(), dirLabelList[i]))
            exit()

        else:#if the path is correct
            pass

    print ("\nOsu! '{0}' Folder: {1} \nFolder for generated compressed files: {2}".format(dirName,inputDir,outputDir))


#function to get list of beatmaps/skins
def scanSource(inputDir):
    osuItemList = [] #list of folders contained in the source folder

    for osuFolder in os.listdir(inputDir): #for each item in the source folder
        if isdir(join(inputDir, osuFolder)): #if it's a directory
            osuItemList.append(osuFolder) #add it to the list
    
    #outputing list
    print ("\nListing all folders found in the source folder:")
    print (*osuItemList, sep="\n")
    
    #let user check list
    fileListCheck = input ("\nis this list of %ss correct? [Y/n] " % osuFile)
    if not fileListCheck.upper() == "Y":
        print ("""
        Please check the source path or the contents of your source folder.
        It should contain folders with %s names.""" % osuFile)
        exit()

    print ("\n{0} {1}s found. All items on this list will be turned into '{2}' files.".format(len(osuItemList), osuFile, osuType))
    return osuItemList
    

#function to check if users wants to delete files in source folder
def verifyRemove():
    
    print ("""
    You requested removal of the original {0} files right after compression. 
    The goal of this option is to save space by deleting the uncompressed {0}s
    and keeping only the new '{1}' files.
    DELETION THROUGH THIS METHOD IS IRREVERSIBLE, but you can still get your
    {0}s back by re-extracting the generated '{1}' files.
    """.format(osuFile, osuType)
    )
    
    rcheck = input("\nproceed with Removal of original files? [Y/n] ")
    if rcheck.upper() == "Y":# if yes
        print ("Removal ENABLED: Original files will be deleted.")
        confirm = input("Continue? [y/N] ")
        if confirm.upper() == "N":
            exit()
        else:
            pass
        return True
    else: #any other answer
        print ("Removal DISABLED: Original files will be left untouched.")
        confirm = input("Continue? [y/N] ")
        if confirm.upper() == "N":
            exit()
        else:
            pass
        return False
        


#function to compress files into desired format, and erase sources if requested
def OSUcompresser(osuItemList,inputDir,outputDir):
    if deleteSources:
        print ("\nStarting compression WITH removal...")
    else:
        print ("\nStarting compression...")

    newFileList = [] # list of generated files

    for folder in osuItemList:
         #compress folders into zip files
        shutil.make_archive(join(outputDir, folder), 'zip', join(inputDir, folder))
         
         #replace the file extension to make it OSU! compatible
        os.rename(r'{0}.zip'.format(join(outputDir, folder)), r'{0}{1}'.format(join(outputDir, folder), osuType))

        #Add it to list of generated files      
        newFileList.append(join(outputDir, folder))

        #Remove source folder if requested
        if deleteSources: shutil.rmtree(join(inputDir, folder))

        #print percentage completion
        percentComplete = round((len(newFileList)/len(osuItemList))*100)
        print ("\t{0}%\r".format(percentComplete))

    print ("COMPLETE!!!")
    print ("\nListing generated files:")
    for file in newFileList:
        print('{0}{1}'.format(file, osuType))   



if __name__ == "__main__":

    folderName, osuFile, osuType = verifyMode()
    
    checkDirs(folderName,sourceDir,destDir)

    OSUitemList = scanSource(sourceDir)

    if deleteSources: deleteSources = verifyRemove()

    OSUcompresser(OSUitemList,sourceDir,destDir)
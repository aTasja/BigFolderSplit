# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:14:40 2018

@author: A.Shatova
"""
import os
import filecmp


class ToSmallFolders:
    def __init__(self):
        self.dirName = os.getcwd() # get current directory
        self.allNames = os.listdir(self.dirName) # get full list of files in current directory 
        
        
    # create new list of file names without this script and other Folders
    def getNames(self):
        namesToWorkWith = []
        for name in self.allNames:
            if "toSmallFolders" not in name and "." in name:
                namesToWorkWith.append(name)
        return namesToWorkWith
    
    
    # create folder in current directory for files with the same names if the folder does not exist yet
    def makeFolder(self, fileName):
        newFolderName = self.dirName +"\\"+ fileName.split(".")[0]
        try:
            os.mkdir(newFolderName)
        except FileExistsError:
            pass
        return newFolderName

    # check if files do not exist in destionation folders
    # and move files to new folders
    # othervise let them unmoved
    def moveFiles(self):
        namesToWorkWith = self.getNames()
        
        for name in namesToWorkWith:
            _from =  os.path.join(self.dirName, name)
            newFolderName = self.makeFolder(name)
            _to = os.path.join(newFolderName, name)
            if name in os.listdir(newFolderName):
                if filecmp.cmp(name, os.listdir(newFolderName)[os.listdir(newFolderName).index(name)]):
                    print ('File with the name ' + name + ' already exists in the folder ' + newFolderName + '. Unable to move.')
            else:
                os.rename(_from, _to)
                

if __name__ == "__main__":      
    makeMove = ToSmallFolders()
    makeMove.moveFiles()


# -*- coding: utf-8 -*-
# Xiaofan Wu
#CS 111 Problem Set 9
#fileProcessing

import os
from pylab import *

def helper(nameOfFolder):
    #create an empty list 
    lists=[]
    #for each of the item in the folder, complete the directory name
    
    for eachFile in os.listdir(nameOfFolder):
        relativePathName=nameOfFolder+"/"+eachFile
        #if the item is a folder, recursively invoke the function to check again
        if os.path.isdir(relativePathName):
            
            listOfFilesinDir=helper(relativePathName)
            #addd the file names to the empty list 
            lists.extend(listOfFilesinDir)
            
           

        else: 
            #otherwise, it has to be a file, so add the file name to the list 
            
            lists.append(relativePathName)
            
           
    return lists 




def writeAllFilenames(nameOfFolder,nameOfOutput):
    #check if the path actually exist
    if os.path.exists(nameOfFolder)==False:
        print "The folder name supplied does not exist."
    #check if the given directory is not a file 
    elif os.path.isfile(nameOfFolder)==True:
        print "It is the name of a regular file rather than a folder. " 
        
    else:
        #otherwise call the helper function to create the list of all file names

        lists=helper(nameOfFolder)
        #open the file of output 
        testfilenames = open(nameOfOutput, 'w')
        for eachline in lists:
            #add eachline in the list of the files, add it to the file 
            
            testfilenames.write(eachline+"\n") 
        testfilenames.close() 
            
writeAllFilenames('test-folder', 'test-filenames.txt') 
  

def getAllFileType(filename):
    #Create an empty list 
    frelist=[]
    #open the file
    lines = open(filename).readlines()
    #for each line in the file, strip the line at ".", and take only the 
    #second part after the ".", so only the file type is kept. Then add
    #the file type to the empty list each time 
    for eachline in lines:
        eachline_after_strip=eachline.strip().split('.')
        filetype=eachline_after_strip[1]
        frelist.append(filetype)
    return frelist

def make_a_dictionary(filename):
    #create an empty dictionary
    fredictionary={}
    #invoke previous function to get a list of all the file type. 
    list_Of_File_type=getAllFileType(filename)
    #for each file type, if the file type name is not already in the dictionary,
    #create a new key. If it is in the key already, just add one to the value.
    for Each_File_Type in list_Of_File_type:
        if Each_File_Type not in fredictionary.keys():
            fredictionary[Each_File_Type]=1
        else:
            fredictionary[Each_File_Type]+=1
    return fredictionary
   

def makePieChart(dictionary_of_freq1):
    #get all the keys to a list
    keys=dictionary_of_freq1.keys()
    #get all the values to a list
    values=dictionary_of_freq1.values()
    #create the figure and set size and color 
    figure (1, figsize=(6,6),facecolor='white')
    # title the chart 
    title('Relative frequencies of file extensions')
    # pie makes the pie chart
    pie(values,labels=keys)
    show()
        
def makeBarGraph(dictionary_of_freq2):
    #sort all the keys, then put them in a list
    keysAfterSort=sorted(dictionary_of_freq2.keys())
    #create an empty count list, add values of each correspond keys to the 
    #count list 
    count=[]
    for eachitem in keysAfterSort:
        count.append(dictionary_of_freq2[eachitem])
        
    figure(2)
    position = arange(len(count))
    #reverse the sorted keys
    yticks(position, keysAfterSort[::-1])
    #draw the bar graph
    barh(position, count[::-1], 0.5, align='center')
    #title the graph 
    title('Absolute frequencies of file extensions')
    show()
    
def chartFileTypes(filename):
    #get the dictionary of file and frequency
    dictionary_of_freq=make_a_dictionary(filename)
    #invoke the pie chart function 
    makePieChart(dictionary_of_freq)
    #invoke the bar graph function 
    makeBarGraph(dictionary_of_freq)
    

chartFileTypes('test-filenames.txt')  
    

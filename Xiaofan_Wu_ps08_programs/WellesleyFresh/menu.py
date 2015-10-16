#Xiaofan Wu
#CS 111 Problem set 8
#Menu

#Import wellesley fresh and get all entries in the file
import wellesleyFresh
allEntries = wellesleyFresh.getAllEntries()

#Task 1
def getMenu(lists,day,dininghall):
    #Go through each dictionary in the list of dictionaries
    for val in lists:
        #if the each value of the key "hall" is the same as the the given
        #dinning hall in the invocation and each value of the key "day" is the 
        #same as the day in the given invocation,rint out the value of the 
        #key meal and the value of the key dish. 
            
        if val['hall']==dininghall and val['day']==day:
            #p
            print val['meal']+ ":" + val['dish']
            
#test function
getMenu(allEntries, 'Thursday', 'Bates') 
        
       
        
#Task 2
def helper(listOfDictionaries):
    #create an empty dictionary
    countDict={}
    #For each dictionary in the list of dictionaries, we check if the 
    for entry in listOfDictionaries:
        for word in entry['dish'].split():
            #for the words in the value of the key dish, check if the word
            #is in dictionary countDict, if it is not, create a new key and 
            #its value will start at 1. 
            if word not in countDict.keys():
               
                countDict[word]=1
            #Otherwise,add one to the value of the already existing key. 
            else:
                countDict[word]+=1
            
    return countDict

    
def printDishWords(listOfDictionaries,threshold):
    #invoke the helper function to get a dictionary of each word as the key
    #and number that it appears as the corresponding value.
    countdict=helper(listOfDictionaries)
    #get a list of the keys
    wordsInDict=countdict.keys()
    #sort the list of all the keys
    wordsInDict.sort()
    #For each item in the wordsInDict, find if the value is greater than the
    #given integer threshold. If it is, print of the menu item and the number
    #of time it appears 
    for menuitems in wordsInDict:
        
        if countdict[menuitems] >= threshold:
            print menuitems.lower() + '\t' + str(countdict[menuitems])
            
#test functions
printDishWords(allEntries, 20)

#task 3
#create a helper function
def helper1(eachEntry,searchterms):
    #For each term in the list of the given search term, lower all letter 
    #first. Then check if each term appears in the dictionary at least once.
    #If it appears at least once, then return true, otherwise return false. 
    for terms in searchterms:
        terms2=terms.lower()
        
        if  (terms2 not in eachEntry['dish'].lower())\
        and (terms2 not in eachEntry['hall'].lower()) \
        and  (terms2 not in eachEntry['meal'].lower())\
        and (terms2 not in eachEntry['day'].lower()):
            return False
       
    return True
        
def searchMenu(dictionariesgiven,searchterms):
    #Create an empty list
    lists=[]

    for entry in dictionariesgiven:
        #for each dictionary in the given list of dictionaries, check if
        #each term in the list of search term given appear at least once.
        if helper1(entry,searchterms):
            #if it does, append the string to the empty list
           lists.append(entry['hall']+":"+entry['meal']+":"+entry['dish']+
           ":"+entry['day'])
    #since each string starts with the hall, sorting the list will sort 
    #according to the first letter of the string, which is the first letter
    #of the dining hall.   
    lists.sort()
    #For each string in the list, print out the string. 
    for ind in lists:
        print ind
           
              
           

#test functions          
searchMenu(allEntries, ['chicken', 'dinner'])     
searchMenu(allEntries, ['chicken', 'dinner', 'tower'])      
searchMenu(allEntries, ['chicken', 'dinner', 'tower', 'wed'])
searchMenu(allEntries, ['at', 'bar', 'thu'])

  
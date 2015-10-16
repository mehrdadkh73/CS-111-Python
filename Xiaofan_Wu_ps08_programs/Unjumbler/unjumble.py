#Xiaofan Wu
#CS 111 Problem set 8
# Unjumbler

# You are provided with this one helper function

def getLinesFromFile(fileName):
    '''Returns a list of strings where each string is a line from the
        specified file. The trailing newline character is not included
        as part of a string in the list.'''
    return(map(lambda s: s.strip(), list(open(fileName, 'r'))))

# Write all other functions on your own!

#1 

def unjumbleKey(word):
    #lower all letters, then sort the letters in the word, then join the 
    #letter together with nothing in between each letter
    wordsorted= ''.join(sorted(word.lower()))
    return wordsorted
    
#tester function
print unjumbleKey('argle')
print unjumbleKey('regal')
print unjumbleKey('Star')
print unjumbleKey('histrionics')

#2
def makeUnjumbleDictionary(fileName):
    #create an empty dictionary
    DictionaryAsOfNow={}
    #get the file
    lists=getLinesFromFile(fileName)
    #for each word in the file, unjumble the word by invoking unjumbleKey. 
    #This way, all the word is sorted alphabetically. For example,
    #regal becomes aeglr.
    for word in lists:
        
        unjumbledword=unjumbleKey(word)
        
        #If the already unjumbled word is not in key of the dictionary 
        #created, add that key and assign its value to the word that's not
        #unjumbled.        
        if unjumbledword not in DictionaryAsOfNow:
            DictionaryAsOfNow[unjumbledword]=[word]
            
        #if the unjumbled word already exist, append the word to the already
        #existing key's value.
        
        else:
            DictionaryAsOfNow[unjumbledword].append(word)
            
    return DictionaryAsOfNow
    
#testing function 
print makeUnjumbleDictionary('tinyWordList.txt')       

#3  
def unjumble(lists,word):
    #Invoke unjumbleKey function to get the sorted word, then check if that
    #word already exist in the key of the dictionary after
    #makeUnjumbleDictionary is invoked. If the unjumbled word matches one 
    #of the keys in the dictionary, return the vaules in that key. Since 
    #the key is already a list, we just need to return it.
    if unjumbleKey(word) in lists.keys():
        
        return lists[unjumbleKey(word)]
    else:
        return []
        
tinyUnjumbleDict = makeUnjumbleDictionary('tinyWordList.txt')        
print unjumble(tinyUnjumbleDict, 'argle')
print unjumble(tinyUnjumbleDict, 'arst')
print unjumble(tinyUnjumbleDict, 'foobar')

#4
def mostAnagrams(elts):
    #create an empty list
    lists=[]
    #get all the values in the dictionaries.
    values=elts.values()
    #For each value in in the values, check if the len of the value is 
    #greater then the lenghth of the initial list. If it is, the initial 
    #list becomes that word. Keep doing this until the longest length is 
    #found. 
    for val in values:
        if len(val)>len(lists):
            lists=val
            
    return lists
tinyUnjumbleDict = makeUnjumbleDictionary('tinyWordList.txt')   
print mostAnagrams(tinyUnjumbleDict) 

LargeUnjumbleDict=makeUnjumbleDictionary('largeWordList.txt')
print mostAnagrams(LargeUnjumbleDict)

#['arest', 'arets', 'aster', 'astre', 'earst', 'rates', 'reast', 'resat', 
#'serta', 'stare', 'stear', 'strae', 'tares', 'tarse', 'taser', 'tears', 
#'teras']





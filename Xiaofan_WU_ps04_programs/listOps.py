#Xiaofan Wu
#CS 111 Problemset 4
#ListOps

#############################
######   sumMultiplesOf #####
#############################
#1A
#Test if each number has remainder of 0, if it has remainder of 0, it means
#that the number is multiple of n. Then finally add all the number in the list
#that is multiple of n.
def sumMultiplesOf(n,nums):
    results=[]
    
    for number in nums:
        if number%n==0:
            results.append(number)
    final=sum(results)
    return final

def testSumMultiplesOf(n, elts):
    
    print('sumMultiplesOf(' + str(n)
          + ', ' + str(elts)
          + ') -> ' + str(sumMultiplesOf(n,elts)))
    
testSumMultiplesOf (2, [8, 12, 5, 7, 9, 6, 10]) 
testSumMultiplesOf (3, [8, 12, 5, 7, 9, 6, 10])
testSumMultiplesOf (4, [8, 12, 5, 7, 9, 6, 10])
testSumMultiplesOf (5, [8, 12, 5, 7, 9, 6, 10])
testSumMultiplesOf (6, [8, 12, 5, 7, 9, 6, 10])
testSumMultiplesOf (7, [8, 12, 5, 7, 9, 6, 10])
testSumMultiplesOf (11, [8, 12, 5, 7, 9, 6, 10])

#############################
######  allSubstringsOf #####
#############################
#1B
#First test if each string in a list is not in the given string, because once
#we find one mistake, it will be considered False. If we don't find any mistakes
#in the list, then it has to be true.

def allSubstringsOf(s,strs):  
    for letter in strs:
        if letter not in s:
            return False
    return True

def testAllSubstringOf(n, elts):
     print('allSubstringsOf(' + str(n)
          + ', ' + str(elts)
          + ') -> ' + str(allSubstringsOf(n,elts)))

testAllSubstringOf('abcdef', ['c', 'def', 'bc', 'cde', 'abcdef', 'a'])
testAllSubstringOf('abcdef', ['g', 'def', 'bc', 'cde', 'abcdef', 'a'])
testAllSubstringOf('abcdef', ['c', 'def', 'ed', 'cde', 'abcdef', 'a'])
testAllSubstringOf('abcdef', ['c', 'def', 'bc', 'cde', 'abcdef', 'cbd'])

#############################
######  isSorted        #####
#############################   
#1c 
#We need to figure out if the the previous string in a list is greater than 
#the string after. If it is, that means some where in the list, the previous
#number is greater than the next number. If this happens, then return false.
#After we check for every string in the list, if nothing is false, then it has 
#to be true.                
def isSorted(listnumber):
    for i in range(len(listnumber)-1):
        if listnumber[i]>listnumber[i+1]:
            return False
       
    return True
def testIsSorted(elts):
    print('isSorted(' + str(elts)
          + ') -> ' + str(isSorted(elts)))
     
testIsSorted([])
testIsSorted([42])
testIsSorted([17,23])
testIsSorted([17, 17, 23, 23])
testIsSorted([23,17])
testIsSorted(range(10))
testIsSorted(range(2,10) + [1])
testIsSorted(range(1,5) + [6,5] + range(7,10))
testIsSorted('a bat came down every fifth game'.split())
testIsSorted('a bat came down from the ceiling'.split())
testIsSorted('to be or not to be'.split())

#############################
######  Suffixes        #####
#############################  


#1d
#Splice the word given from 0 to the length of the word, then index 1 to the
#length of the word, then index 2 to the length of the word. After we get to the 
#last letter in the list, append everything in one list. 

def suffixes(suffix):
    newlist=[]
    for i in range (len(suffix)):
        final=suffix[i:len(suffix)]
        newlist.append(final)
    return newlist
    
      
def testsuffixes(elts):
    print('suffixes(' + str(elts)
          + ') -> ' + str(suffixes(elts)))
      
testsuffixes('abcdef')
testsuffixes('computer')
        
#############################
######  mapCapitalize   #####
#############################  

#1e
#Use python given function to capitalize every word in the list, then append 
#this result to a new list.
   
def mapCapitalize(lowercase):
    results=[]
    for lowercase_word in lowercase:
        listofcapitalizedword=str.capitalize(lowercase_word)
        results.append(listofcapitalizedword)
    return results
    
def testmapCapitalize(elts):
    print('mapCapitalize(' + str(elts)
          + ') -> ' + str(mapCapitalize(elts)))
   
testmapCapitalize(['abc', 'de', 'f', ''])
testmapCapitalize('To be or not to be'.split())
pets = ['bunny', 'cat', 'dog']
#test if involking mapCapitalze on the list changes the original list. 
testmapCapitalize(pets)
print pets 

#############################
###### filterSortedPairs#####
############################# 

#1f
#Using index to find the first and second sub-string in each string in the list.
#Then compare the two substring. If the second one is greater or euqal to the
#first one, then append to the new list.

def filterSortedPairs(lists):
    results=[]
    for n in range(0,len(lists)):
        if lists[n][0]<=lists[n][1]:
            results.append(lists[n])
    return results
def testfilterSortedPairs(elts):
    print('filterSortedPairs(' + str(elts)
          + ') -> ' + str(filterSortedPairs(elts)))
    
    
testfilterSortedPairs([(2, 1), (5, 8), (7, 7), (3, 2), (1, 9), (2, 8), (7, 3)])
[(5, 8), (7, 7), (1, 9), (2, 8)]   

testfilterSortedPairs([('to', 'be'), ('be', 'or'), ('or', 'not'), ('not', 'to')])

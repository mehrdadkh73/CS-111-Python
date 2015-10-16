#xiaofan Wu and Jingyao Liu
#CS 111 Problem set 7
#powerlist
#3a
def concatToListsRec(elt,listoflists):
    #if listoflists is empty, return empty list
    if len(listoflists)==0:
        return []
    else:
        #add elt to the first element of the list 
        n = [[elt] + listoflists[0]]
        #invoke listoflists only from the second element or index one and add n.
        return n + concatToListsRec(elt, listoflists[1:])
        
#some test functions
print concatToListsRec(17, [[]]) 
print concatToListsRec(17, [[7]])
print concatToListsRec(17, [[7, 8, 9]]) 
print concatToListsRec(17, [[7, 8], [9, 10]]) 
print concatToListsRec(17, [])
print concatToListsRec('I', [['came'], ['saw'], ['conquered']]) 
print concatToListsRec(False, [[], [9], ['spring', 'is', 'coming']])
print concatToListsRec(2, [[[True], ['blue']], ['who?', 'KNEW!']])

#3b         
def powerlistRec(lists):
    #if listoflists is empty, return empty list
    if len(lists)==0:
        return [[]]  
    else:
        #invoke the helper function concatToListRec. The two parameters are the
        #first element in the list (The list will be invoked each time by taking
        #out the first element of the list). 
        n=concatToListsRec(lists[0],powerlistRec(lists[1:]))
        #invoke powerlistRec function that the first element of the list is 
        #dropped each time then add n as defined previously.
        return n+powerlistRec(lists[1:])
#test functions       
print powerlistRec([])
print powerlistRec([4]) 
print powerlistRec([3, 4])
print powerlistRec([2, 3, 4]) 
print powerlistRec([1, 2, 3, 4]) 
print powerlistRec(['yellow','red','blue'])
print powerlistRec([True,'blue',2])
print powerlistRec([True,'blue',2, ['who?']])


#3c
# define helper function that does the same thing as concatToListsRec with loop
def concatToListsLoop(n, listOfLists):
    result = []
# use for loop to add each element to the result list after it's 
#concatenated with the given element
    for elt in listOfLists:
        result.append([n]+elt)
    return result
        
def powerlistLoop(myList):
# set a list of an empty list as the initial result list
    result = [[]]
    for elt in myList:
# invoke helper function to concatenate the element to all elements 
#in current result and return the list of these lists
# set result to be the current result plus this list to keep the previous lists
        result = result + concatToListsLoop(elt, result)
    return result
    
#test functions    
print powerlistLoop([])
print powerlistLoop([1]) 
print powerlistLoop([1, 2]) 
print powerlistLoop([1, 2, 3])
print powerlistLoop([1, 2, 3, 4])


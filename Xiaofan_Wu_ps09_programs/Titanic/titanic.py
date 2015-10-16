#YuanzhenPn & Xiaofan Wu
#CS 111 Pset 09
#Task2:Titanic
from pylab import*
#2a_______________________________________________
#get the item from the left of the equal sign
def getKey(s):
    #split the word at the equal sign
    word=s.split('=')
    #get the word to the left
    leftWord=word[0]
    #clean the spaces around
    leftWord.strip()
    return leftWord
    

#get the item from the right of the equal sign
def getValue(s):
    word=s.split('=')
    #get the word to the right
    rightWord=word[1]
     #clean the spaces around
    rightWord.strip()
    return rightWord


def helperfunction(line):
    #create an empty dictionary 
    
    dictionaryOfPassenger={}
    #split the dictionary at ;
    listofwords=line.strip().split(';')
    #for each of the word afte split at ; in one dictionary. Check if victim
    #is in the word, if it is, create a new dictionary named 'name' and 'status'
    #and add the values by splitting the word at the "("
    for eachword in listofwords:
        
        if 'victim' in eachword:
            
            dictionaryOfPassenger['name']=eachword[:eachword.find('(victim)')]
            dictionaryOfPassenger['status']='victim'
            #loop through the index in case there are passengers that do not
            #have one of the keys. 
            for i in range(1,len(listofwords)):
                dictionaryOfPassenger[getKey(listofwords[i].strip())]=getValue(listofwords[i])
        #If the word survivor in the word, do the same thing as previously
        #except this time the values will be survivor for status.     
        elif 'survivor' in eachword:
            dictionaryOfPassenger['name']=eachword[:eachword.find('(survivor)')]
            dictionaryOfPassenger['status']='survivor'
            #loop through the index in case there are passengers that do not
            #have one of the keys. 
            for i in range(1,len(listofwords)):
                dictionaryOfPassenger[getKey(listofwords[i].strip())]=getValue(listofwords[i])
                
    return dictionaryOfPassenger

    
 
def createListOfTitanicPassengers(fileName):
    #create an empty list
    list_of_dictionaries=[]
    #read all the lines in the file
    lines = open(fileName).readlines()
    #for each line in this file 
    for eachline in lines:
        #invoke the helper function to create each passenger dictionary and then
        #append each dictionary 
        list_of_dictionaries.append(helperfunction(eachline))
        
    return list_of_dictionaries
        

     
# 2b_________________________________________________________

def createDictionaryOfVictimsCabinClassOccurrences(passengers):
    #create an empty dictionary
    dictionary_for_class={}
    #For each dictionary in the list of dictionaries of passengers, check if
    #the status is victim. 
    for entry in passengers:
        if entry['status']=='victim':
            #if status is victim and the value is not in the dictionary for 
            #class, create a new key and start with one. 
         
            if entry['class'] not in dictionary_for_class.keys():
                dictionary_for_class[entry['class'] ]=1
            #Otherwise,add one to the value of the already existing key. 
            else:
                dictionary_for_class[entry['class'] ]+=1
    return dictionary_for_class
    

   # '''Given a list where each entry is a dictionary with
   # information about a passenger on the Titanic, returns
   # a new dictionary whose keys are the cabin classes of the
   # Titanic victims and whose values are the number of
   # victims in the corresponding cabin class.'''
   
def pieChartFromOccurrenceDictionary(d):
    #get all the keys of the dictionary into a list
    keys=d.keys()
    #get all the values of the dictionary into a list
    occurence=d.values()
    #give values to the figure size and background
    figure (1, figsize=(6,6),facecolor='white')
    # title the pie chart 
    title('Pie Chart Of Victims by Cabin Classes')
    # pie makes the pie chart
    pie(occurence,labels=keys)
    show()
    # make the plot visible

   

     
def pieChartOfVictimsCabinClasses(fileName):
    #invoke the createListOfTitanicPassengers to get all passenger info into
    #a dictionary. 
    ListOfTitanicPassengers=createListOfTitanicPassengers('titanic.txt')
    #Invoke createDictionaryOfVictimsCabinClassOccurrences function to 
    #create a dictionary of victim in each class and the number of victim 
    cabinClassDictionary=createDictionaryOfVictimsCabinClassOccurrences(ListOfTitanicPassengers) 
    #draw the pie graph         
    pieChartFromOccurrenceDictionary(cabinClassDictionary)

    
    

pieChartOfVictimsCabinClasses('titanic.txt')

    #Given a file with information on Titanic passengers,
    #causes a pie chart to be displayed that illustrates
    #the relative number of Titanic victims from each cabin
    #class.'''

#2C-----------------------------------------------------------------------  

#define a function that takes in a list of dictionary
#returns a list of ages of all survivors 
#by looping through the given list of dictionary
def getListOfSurvivorsAges(passengers):
    list_for_age=[]
    for entry in passengers:
        if 'age' in entry:
            list_for_age.append(float(entry['age']))
            
    return list_for_age

#define a function that takes in a list of numerical data and the number of
#equal sized intervals to bin the data into,
#the function returns a new list where each entry contains 
#the number of instances from the input list 
#in the corresponding equal sized interval. 
#The interval size should be the quantity 
#(one more than the maximum element in the input list) divided by the
#number of intervals.
def histogram(data, numberOfIntervals):
    #calculate the maximun and the intervalSize
    Max=(max(data)+1)
    intervalSize=Max/numberOfIntervals
    #create an empty list to keep count of people in different age group
    count=[]
    
    #create 2 for loops to 
    #1. set the base case(number of survivors) for each age group to be 0
    #2. keep the counting the number of survivors in each age group
    for number_of_items in range(numberOfIntervals):
        count.append(0)
    for age in data:
        count[int(age/intervalSize)]+=1
    return count
                
#define a function that takes in a list corresponding to a histogram for
#a set of data and given the maximum value of the data,displays a bar graph of the histogram. 
#The graph has the specified title. 
#In the graph, I made the x-axis label to be the rounded medium of the age range.
def barGraphOfHistogram(hist, maximum, graphTitle):
    Positions=arange(len(hist))
    bar(Positions,hist,0.8,align='center')
    intervalSize= (maximum+1)/len(hist)
    labels_for_X_axis=[]
    
    #In the graph, we made the x-axis label to be the rounded medium of the age range.
    for number in range(len(hist)):
        labels_for_X_axis.append(str(round((number+.5)*intervalSize)))
    xticks(Positions,labels_for_X_axis)
    
    title(graphTitle)
    show()
       
       
#define a function that takes in a file name and number of age group.
#it returns a bar graph displaying the number of survivors in different age group
#at the end by invoking all the helper functions defined previously
def barGraphOfSurvivorsAges(fileName, numberOfAgeGroups):
    list_of_dict_for_passengers=createListOfTitanicPassengers(fileName)
    list_for_age=getListOfSurvivorsAges(list_of_dict_for_passengers)
    count = histogram(list_for_age, numberOfAgeGroups)   
    figure(2)  
    barGraphOfHistogram(count,max(list_for_age), 'Number of Survivors in ' +str(numberOfAgeGroups)+' Ages Groups')          
              
#Test Case
barGraphOfSurvivorsAges('titanic.txt', 7)
  




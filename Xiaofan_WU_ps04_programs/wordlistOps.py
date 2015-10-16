# Xiaofan Wu and Jingyao Liu
# CS111 Problem Set 4
# Wordlist Functions

# Given the name of a file, returns a list of lines from the file.
# All leading and trailing whitespace characters are removed from each line.
def wordsFromWordlistFile(filename):
    print('Reading lines of wordlist file ' + filename + ' into list... ')
    lines = open(filename).readlines()  # Read in all lines from file
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()  # Remove trailing newline '\n' character
    print('Done. Read ' + str(len(lines)) + ' lines')
    return lines
    
#############################
######   longestWords   #####
#############################

# This code is provided to you as an example of a wordlist manipulation function

def longestWords(elts):
    # Determine length of longest words
    lengthOfLongest = -1
    for s in elts:
        if len(s) > lengthOfLongest:
            lengthOfLongest = len(s)

    # Create list of words that have longest length
    words = []
    for s in elts:
        if len(s) == lengthOfLongest:
            words.append(s)
    return words    

def testLongestWords(wordFile):
    wordList = wordsFromWordlistFile(wordFile)
    print('longestWords(' + wordFile + ') -> ' + str(longestWords(wordList)))

###############################
#####   beginAndEndWith   #####
###############################

def beginAndEndWith(n, mylist):
    result = []
    for s in mylist:
    # find words of the right length
        if len(s) >= 2*n:
    # find words that begin and end correctly
            if s[:n] == s[-n:]:
                result.append(s)
    return result

def testBeginAndEndWith(n, wordFile):
    wordList = wordsFromWordlistFile(wordFile)
    print('beginAndEndWith(' + str(n) + ', ' + str(wordFile) + ') -> ' 
    + str(beginAndEndWith(n, wordList)))
                    
testBeginAndEndWith(1, 'tinyWordList.txt')
testBeginAndEndWith(2, 'smallWordList.txt')
testBeginAndEndWith(3, 'smallWordList.txt')
testBeginAndEndWith(3, 'mediumWordList.txt')
testBeginAndEndWith(4, 'mediumWordList.txt')
testBeginAndEndWith(4, 'largeWordList.txt')
testBeginAndEndWith(5, 'largeWordList.txt')            

##################################
#####   mostOccourrencesOf   #####
##################################

def mostOccurrencesOf(s, mylist):
    # Find the largest amount of occurrences of 's' in any word in mylist
    numMostOccurrences = -1
    for w in mylist:
        if w.count(s) > numMostOccurrences:
            numMostOccurrences = w.count(s)

    # Create list of words that have the longest length
    words = []
    for w in mylist:
        if w.count(s) == numMostOccurrences:
            words.append(w)
    return words  

def testMostOccurrencesOf(s, wordFile):
    wordList = wordsFromWordlistFile(wordFile)
    print('mostOccurrencesOf(' + str(s) + ', ' + str(wordFile) + ') -> ' 
    + str(mostOccurrencesOf(s, wordList)))

testMostOccurrencesOf('p', 'tinyWordList.txt')
testMostOccurrencesOf('s', 'smallWordList.txt')
testMostOccurrencesOf('s', 'mediumWordList.txt')
testMostOccurrencesOf('u', 'largeWordList.txt')

################################
#####   mostOccurrences   #####
################################
#
def mostOccurrences(mylist):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    # add pairs of letters and their corresponding words using the prev function
    for s in range(26):
        result.append([alphabet[s], mostOccurrencesOf(alphabet[s], mylist)])
    return result
    
def testMostOccurrences(wordFile):
    wordList = wordsFromWordlistFile(wordFile)
    print('mostOccurrences(' + str(wordFile) + ') -> ' 
    + str(mostOccurrences(wordList)))
   
testMostOccurrences('tinyWordList.txt')
testMostOccurrences('smallWordList.txt') 

######################################
######   wordLengthFrequencies   #####
######################################
#
def wordLengthFrequencies(mylist):
    # determine the length of longest word
    lengthOfLongest = -1
    for w in mylist:
        if len(w) > lengthOfLongest:
            lengthOfLongest = len(w)
    
    # add pairs of length and num of words of that length to the result list
    result = []
    for n in range(1,lengthOfLongest+1):
        count = 0
        for w in mylist:
            if len(w) == n:
                count = count + 1
        result.append((n, count))
    return result
    
def testWordLengthFrequencies(wordFile):
    wordList = wordsFromWordlistFile(wordFile)
    print('wordLengthFrequencies(' + str(wordFile) + ') -> ' 
    + str(wordLengthFrequencies(wordList)))
    
testWordLengthFrequencies('tinyWordList.txt')
testWordLengthFrequencies('smallWordList.txt')
testWordLengthFrequencies('mediumWordList.txt')
testWordLengthFrequencies('largeWordList.txt')
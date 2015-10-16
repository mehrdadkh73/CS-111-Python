# Return a list of words from a string, ignoring punctuation, but including internal apostrophes.
# This does a better job than split() at getting words from a string. For example:
#
#   >>> 'He said, "I will!", but she said, "I won\'t"'.split()
#   'He', 'said,', '"I', 'will!",', 'but', 'she', 'said,', '"I', 'won\'t"']
# 
#   >>> wordParser.wordsFromString('He said, "I will!", but she said, "I won\'t"')
#   ['He', 'said', 'I', 'will', 'but', 'she', 'said', 'I', "won't"]

def wordsFromString(string):
    wordsSoFar = []
    currentString = ""
    stringlen = len(string)
    for index in range(stringlen):
        char = string[index]
        if char.isalpha():
            currentString = currentString + char
        elif (char == "'" and currentString != ""
              and index < stringlen-1 and string[index+1].isalpha):
            # Treat internal apostrphes as part of a word
            currentString = currentString + char
        elif currentString != "":
            wordsSoFar.append(currentString)
            currentString = ""
        # Otherwise, do nothing
    # Get last word:
    if currentString != "":
        wordsSoFar.append(currentString)
    return wordsSoFar

# Xiaofan Wu
# CS111 Problem Set 3
# String Classification

from stringOps import *

# Returns True if the simplified version of s is a palindrome, 
# and False otherwise.

def isPalindrome(s):
    #simply the sentence
    simplifys=simplify(s)
    #reverse and check if the reverse is the same as the original
    reverses=reverse(simplifys)
    if simplifys==reverses:
        return True
    else:
        return False
        
   
# Returns True if the simplified version of s is middling, 
# and False otherwise.
def isMiddling(s):
    #simplify the sentence   
    simplify2=simplify(s)
    
    #find the first half of the sentence
    firsthalf2=firstHalf(simplify2)
    
    #check if the first and the last letter of the simplified 
    #half sentence is the same
    if first(firsthalf2)==last(firsthalf2):
        return True
    else:
        return False
        
    #find the last half of the sentence
    lasthalf2=lastHalf[simplify2]
    
    #check if the first and the last letter of the simplified second half 
    #sentence is the same
    if first(lasthalf2)==last(lasthalf2):
        return True
    else:
        return False

def classify(s):
    if isMiddling(s):
    #Check if the sentence isMiddling and palindrome       
        if isPalindrome(s): 
             print ('a middling palindrome: ' + s)
             
    #Otherwise it means that the sentence is only middling.           
        else:        
             print ('just middling: ' + s)
    #check if the sentence is palindrome
    elif isPalindrome(s): 
        print('just a palindrome: ' + s)     
    #Otherwise it is neither middling nor palindrome   
    else:
        print('neither middling nor a palindrome: ' + s)
       
       
    

 
# Test cases   
classify('A lob, a rap as bat stabs --- a parabola!')
classify('A pitch, a rap as bat stabs --- a parabola!')
classify('A launch, a rap as bat stabs --- a parabola!')
classify('A man, a plan, a canal: Panama')
classify('A banana, a plan, a canal: Panama')
classify('Cigar? Toss it in a can. It is so tragic!')
classify('Cigar? Toss it in a pan. It is so tragic!')
classify('Cigar? Toss it in a pot. It is so tragic!')
classify('Cigar? Toss it on a cat. It is so tragic!')
classify('Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.')
classify('Golf? No, sir. Prefer prison flog!')
classify('No lemon or melon')
classify('No lemon, no melon')
classify('No lemons or melons')
classify('No lemons see melons')
classify('No lemons, no melon')
classify('No lemons, no melons')
classify('No lemons, not melons')
classify('Stressed? No tips? Spit on desserts!')
classify('You say "Goodbye!", but I say "Hello"')
classify('You utter "Goodbye!", but I say "Hello"')
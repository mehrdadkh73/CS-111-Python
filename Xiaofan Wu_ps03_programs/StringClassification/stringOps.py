# String Operations

# Returns an output string in which all nonalphabetic letters from
# input string have been removeed and all all letters have been lowercased.
# E.g. simplify('You say "Goodbye!", but I say "Hello"') ==> 'yousaygoodbyebutisayhello'
def simplify(s):
    return ''.join(c for c in s.lower() if c.isalpha())

# Returns a string that is the reverse of the input string
# E.g. reverse('rabbit') ==> 'tibbar'
def reverse(s):
    return s[::-1]

# Return the first half of a string. If the input string has odd length,
# the middle letter is included. If the input string is empty, 
# returns the empty string. 
#   firstHalf('rabbit') ==> 'rab'
#   firstHalf('bunny') ==> 'bun'
#   firstHalf('') ==> ''
def firstHalf(s):
    if s == '':
        return ''
    else: 
        return s[:(len(s)+1)/2]

# Return the last half of a string. If the input string has odd length,
# the middle letter is included. If the input string is empty, 
# returns the empty string. 
#   lastHalf('rabbit') ==> 'bit'
#   lastHalf('bunny') ==> 'nny'
#   lastHalf('') ==> ''
def lastHalf(s):
    if s == '':
        return ''
    else: 
        return s[len(s)/2:]

# Returns the first character of a nonempty string.
# Signals an error for the empty string.
#   first('rabbit') ==> 'r'
#   first('bunny') ==> 'b'
def first(s):
    return s[0]

# Returns the last character of a nonempty string.
# Signals an error for the empty string.
#   last('rabbit') ==> 't'
#   last('bunny') ==> 'y'
def last(s):
    return s[len(s)-1]
    
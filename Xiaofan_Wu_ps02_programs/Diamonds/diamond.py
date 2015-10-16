#Xiaofan Wu
#CS 111 PS 2
#Make diamonds

#Code that is given
zeroStar  = '     '
oneStar   = '  *  '
twoStar   = ' * * '
threeStar = '* * *'
empty     = ''

#Apply divide and conquer method 

#print eight lines of diamonds
def diamond8():
    diamond4()
    diamond4()
    
#Print four lines of diamonds
def diamond4():
    diamond2()
    diamond2()
    
#add the space in between the stars and print two lines of diamonds
def diamond2():
    diamond1(empty,zeroStar)  
    diamond1(zeroStar,empty)

#Print the diamond four time horizontally
def diamond1(prefix,after):
    print ((prefix + oneStar + after) *4)
    print ((prefix + twoStar + after) *4)
    print ((prefix + threeStar + after) *4)
    print ((prefix + twoStar + after) *4)
    print ((prefix + oneStar + after) *4)

#Invoke the code
diamond8()


 
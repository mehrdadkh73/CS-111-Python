# Xiaofan Wu
# CS111 Problem Set 1
# Making change

# Convert the string to a number that the computer will recognize
dollar = float(raw_input('How much money do you want to make change for? ')) 

# Convert dollar to cents, round the cents,and convert cents to integer
cents = int(round(dollar *100)) 
print('We can make change for $' + str(dollar) + ' using:')


# Determine and print out number of $20 dollar bill
num20dollar = cents/2000
print(str(num20dollar) + ' $ 20 bills')

# Compute remaining amount (in cents) that we want to make change for
cents = cents - num20dollar*2000 


# Determine and print out number of $10 dollar bill
num10dollar = cents/1000
print(str(num10dollar) + ' $ 10 bills')

# Compute remaining amount (in cents) that we want to make change for
cents = cents - num10dollar*1000  


# Determine and print out number of $5 dollar bill
num5dollar = cents/500
print(str(num5dollar) + ' $ 5 bills')

# Compute remaining amount (in cents) that we want to make change for
cents = cents - num5dollar*500  


# Determine and print out number of $1 dollar bill
num1dollar = cents/100
print(str(num1dollar) + ' $ 1 bills')

# Compute remaining amount (in cents) that we want to make change for
cents = cents - num1dollar*100  


# Determine and print out number of quarters 
numQuarters = cents/25
print(str(numQuarters) + ' quarters')

# Compute remaining amount (in cents) that we want to make change for
cents = cents - numQuarters*25  


# Determine and print out number of dimes
numDimes = cents/10    
print(str(numDimes) + ' dimes')

# Compute remaining amount (in cents) that we want to make change for
cents= cents - numDimes*10


# Determine and print out number of nickels
numNickels = cents/5
print(str(numNickels) + ' nickels') 

# Compute remaining amount (in cents) that we want to make change for
cents= cents - numNickels*5 


# Pennies can be used for any remaining amount
print(str(cents) + ' pennies')

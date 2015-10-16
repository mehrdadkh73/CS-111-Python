#Xiaofan Wu
#CS 111 PS 2 
#Sale

from cs1graphics import*
import random


#Create a sale function that takes three arguments
def sale(price,discountRate,taxRate):
    
    #calculate discount price
    discountPrice = ((1-(discountRate/100.0))*price)
   
    #calculate sale tax
    saleTax = taxRate/100*discountPrice
    
    #print message with the result limited to 2 digit after the decimal
    print ("The original price is " + "{0:.2f}".format(price))
    print ("The sale price after a " + str(discountRate) +  " percent discount is " + "{0:.2f}".format(discountPrice))
    print("A " + str(taxRate) + " percent tax on the sales price is " + "{0:.2f}".format(saleTax))
    
    #Calculate the final cost after discount and tax
    finalCost = "{0:.2f}".format(float(discountPrice) + float(saleTax))
    return finalCost
    
#Create a run function that takes zero argument but does what is required 
def run():
    
    #Ask for the price of the item
    price = float(raw_input("Please enter a price: "))
    
    #Randonly generate the discount rate
    discountRate = random.randint(10,40)
    
    #Ask for the tax rate
    taxRate = float(raw_input("What is the sales tax rate? "))
    
    #Print the sale price and invoke the sale function 
    print ("sale (" + str(price) +", " + str(discountRate) + ", " + str(taxRate) + ")")
    print ("Result returned is "+ str(sale(price,discountRate,taxRate)))
    

#=============================================================
#    Course-Lab: CS104 -- Lab-04 – Shipping Charges
#    Filename: Lab4_ShippingCharges.py
#    Author: Curtis Collins
#    Purpose: 	Demonstrate basic Python programming skills by designing, and developing a
#		programming solution that utilizes multiple functions for calculating shipping 
#		charges. Four shipping rates have been pre-defined based on package weight.
#=============================================================

def twoPoundsOrLess(weight):
    print("Your total is: $" , round((weight * 1.10),2))

def betweenTwoAndSix(weight):
    print("Your total is: $" , round((weight * 2.20),2))

def betweenSixAndTen(weight):
    print("Your total is: $" , round((weight * 3.70),2))

def greaterThanTen(weight):
    print("Your total is: $" , round((weight * 3.80),2))
          
def main():


    weight = input("Enter the weight of the package in pounds: ")

    weight = float(weight)

    if (weight <= 2):
        twoPoundsOrLess(weight)
    elif (weight > 2 and weight <6):
        betweenTwoAndSix(weight)
    elif(weight > 6 and weight < 10):
        betweenSixAndTen(weight)
    else:
        greaterThanTen(weight)
        
    

main()

'''Enter the weight of the package in pounds: 5
Your total is: $ 11.0
Enter the weight of the package in pounds: 10
Your total is: $ 38.0
Enter the weight of the package in pounds: 7
Your total is: $ 25.9
'''

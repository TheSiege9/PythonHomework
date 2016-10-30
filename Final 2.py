def main():


    shirtNumber = int(input("Please enter how many shirts you would like:"))

    if shirtNumber < 0:
        print("Please enter a non-negative integer")
    elif shirtNumber < 5:
        print("The cost of each shirt is $12 and the total cost is: $", shirtNumber * 12)
    elif shirtNumber >= 5 and shirtNumber <= 10:
        print("The cost of each shirt is $10.8 and the total cost is: $", shirtNumber * 10.8)
    elif shirtNumber >= 11 and shirtNumber <= 20:
        print("The cost of each shirt is $10.2 and the total cost is: $", shirtNumber * 10.2)
    elif shirtNumber >= 21 and shirtNumber <= 30:
        print("The cost of each shirt is $9.6 and the total cost is: $", shirtNumber * 9.6)
    elif shirtNumber > 30:
        print("The cost of each shirt is $9 and the total cost is: $", shirtNumber * 9)
    
        



main()

'''
Please enter how many shirts you would like:4
The cost of each shirt is $12 and the total cost is: $ 48
>>> ================================ RESTART ================================
>>> 
Please enter how many shirts you would like:0
The cost of each shirt is $12 and the total cost is: $ 0
>>> ================================ RESTART ================================
>>> 
Please enter how many shirts you would like:8
The cost of each shirt is $10.8 and the total cost is: $ 86.4
>>> ================================ RESTART ================================
>>> 
Please enter how many shirts you would like:-2
Please enter a non-negative integer
'''

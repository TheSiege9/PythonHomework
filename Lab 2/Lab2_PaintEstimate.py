#
#=============================================================
#    Course-Lab: CS104 -- Lab-02 – Paint Estimation
#    Filename: Lab2_PaintEstimate.py
#    Author: Curtis Collins
#    Purpose: Ask user to enter info and then calculate the price of the painting job
#=============================================================



def main():

    #prompt for the necessary things
    width = input("Enter the width of the room: ")
    height = input("Enter the height of the room: ")
    paintPrice = input("Enter the cost of the paint being used: ")

    #convert to numbers
    width = float(width)
    height = float(height)
    paintPrice = float(paintPrice)
    #proceed with calculations
    area = width * height
    amountLabor = 8 *(area / 115)
    amountPaint = area / 115
    #make sure the amount of paint isn't less than 1
    if (area % 115 == 0):
        amountPaint = (area) / 115
    else:
        amountPaint = (area - area % 115) / 115 + 1

    #calculate money amounts
    laborCost = 20 * amountLabor
    paintCost = paintPrice * amountPaint

    #round to the right decimals
    fixLaborCost = round(laborCost, 2)
    fixPaintCost = round(paintCost, 2)
    fixAmountLabor = round(amountLabor, 1)

    #caluclate total
    totalCost = fixLaborCost + fixPaintCost

    
    
    #print out the information
    print("The area of the wall is ", area, " sq. ft.")
    print("The amount of paint needed is ", amountPaint, " gl.")
    print("The amount of hours required will be ", fixAmountLabor)
    print("The labor will cost $", fixLaborCost)
    print("The paint will cost $", fixPaintCost)
    print("The total cost of the projcet will be $", totalCost)
main()

"""
Enter the width of the room: 50
Enter the height of the room: 50
Enter the cost of the paint being used: 10
The area of the wall is  2500.0  sq. ft.
The amount of paint needed is  22.0  gl.
The amount of hours required will be  173.9
The labor will cost $ 3478.26
The paint will cost $ 220.0
The total cost of the projcet will be $ 3698.26
>>> ================================ RESTART ================================
>>> 
Enter the width of the room: 20
Enter the height of the room: 30
Enter the cost of the paint being used: 5
The area of the wall is  600.0  sq. ft.
The amount of paint needed is  6.0  gl.
The amount of hours required will be  41.7
The labor will cost $ 834.78
The paint will cost $ 30.0
The total cost of the projcet will be $ 864.78
>>> ================================ RESTART ================================
>>> 
Enter the width of the room: 45
Enter the height of the room: 60
Enter the cost of the paint being used: 20
The area of the wall is  2700.0  sq. ft.
The amount of paint needed is  24.0  gl.
The amount of hours required will be  187.8
The labor will cost $ 3756.52
The paint will cost $ 480.0
The total cost of the projcet will be $ 4236.52
"""

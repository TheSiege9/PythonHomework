#=============================================================
#    Course-Lab: CS104 – Lab 6, Arrays – Total Sales
#    Filename: Lab_6_ Arrays_TotalSales.py
#    Author: Curtis Collins
#    Purpose: 	To write the correct program
#=============================================================



def main():

    weekArray = [0] * 7
    dayOfTheWeek = 0
    dailyValue = float(input("Please enter the sales from today."))

    while dayOfTheWeek < 6:
        
        weekArray[dayOfTheWeek] = dailyValue

        dailyValue = float(input("Please enter the sales from today."))

        dayOfTheWeek = dayOfTheWeek + 1

    weekArray[dayOfTheWeek] = dailyValue

    print("The weekly totals are: $", sum(weekArray))
    

main()


'''
Please enter the sales from today.1
Please enter the sales from today.1
Please enter the sales from today.1
Please enter the sales from today.1
Please enter the sales from today.1
Please enter the sales from today.1
Please enter the sales from today.1
The weekly totals are: $ 7.0
>>> ================================ RESTART ================================
>>> 
Please enter the sales from today.5
Please enter the sales from today.5
Please enter the sales from today.5
Please enter the sales from today.5
Please enter the sales from today.5
Please enter the sales from today.5
Please enter the sales from today.5
The weekly totals are: $ 35.0
>>> ================================ RESTART ================================
>>> 
Please enter the sales from today.15
Please enter the sales from today.21
Please enter the sales from today.02
Please enter the sales from today.35
Please enter the sales from today.86
Please enter the sales from today.48
Please enter the sales from today.21
The weekly totals are: $ 228.0
'''

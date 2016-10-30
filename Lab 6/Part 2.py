#=============================================================
#    Course-Lab: CS104 – Lab 6, Arrays – Rainfall Statistics
#    Filename: Lab_6_ Arrays_RainfallStats.py
#    Author: Curtis Collins
#    Purpose: 	To write the approriate program.
#=============================================================


def main():


    rainfallArray = [0] * 12

    monthArray = ["January", "February", "March", "April",
                  "May", "June","July", "August", "September", "October", "November", "December"]

    monthlyRainfall = float(input("Please enter the amount of rain recieved January in inches."))

    i = 0
    x = 1

    while i < 11:

        rainfallArray[i] = monthlyRainfall

        print("The month is:", monthArray[x])

        monthlyRainfall = float(input("Please enter the amount of rain recieved for this month in inches."))

        i = i + 1
        x = x + 1

    rainfallArray[i] = monthlyRainfall
    
    print("The total amount of rainfall for this year was:", sum(rainfallArray), "inches")
    print("The average rainfall for this year was:", sum(rainfallArray)/int(len(rainfallArray)), "inches")

    print("The month with the highest amount of rainfall is:", monthArray[rainfallArray.index(max(rainfallArray))])
    print("The month with the lowest amount of rainfall is:", monthArray[rainfallArray.index(min(rainfallArray))])



main()


'''
Please enter the amount of rain recieved January in inches.50
The month is: February
Please enter the amount of rain recieved for this month in inches.10
The month is: March
Please enter the amount of rain recieved for this month in inches.10
The month is: April
Please enter the amount of rain recieved for this month in inches.10
The month is: May
Please enter the amount of rain recieved for this month in inches.5
The month is: June
Please enter the amount of rain recieved for this month in inches.10
The month is: July
Please enter the amount of rain recieved for this month in inches.3
The month is: August
Please enter the amount of rain recieved for this month in inches.6
The month is: September
Please enter the amount of rain recieved for this month in inches.4
The month is: October
Please enter the amount of rain recieved for this month in inches.2
The month is: November
Please enter the amount of rain recieved for this month in inches.79
The month is: December
Please enter the amount of rain recieved for this month in inches.50
The total amount of rainfall for this year was: 239.0 inches
The average rainfall for this year was: 19.916666666666668 inches
The month with the highest amount of rainfall is: November
The month with the lowest amount of rainfall is: October

Please enter the amount of rain recieved January in inches.20
The month is: February
Please enter the amount of rain recieved for this month in inches.1
The month is: March
Please enter the amount of rain recieved for this month in inches.51
The month is: April
Please enter the amount of rain recieved for this month in inches.4
The month is: May
Please enter the amount of rain recieved for this month in inches.60
The month is: June
Please enter the amount of rain recieved for this month in inches.3
The month is: July
Please enter the amount of rain recieved for this month in inches.2
The month is: August
Please enter the amount of rain recieved for this month in inches.5
The month is: September
Please enter the amount of rain recieved for this month in inches.8
The month is: October
Please enter the amount of rain recieved for this month in inches.4
The month is: November
Please enter the amount of rain recieved for this month in inches.9
The month is: December
Please enter the amount of rain recieved for this month in inches.6
The total amount of rainfall for this year was: 173.0 inches
The average rainfall for this year was: 14.416666666666666 inches
The month with the highest amount of rainfall is: May
The month with the lowest amount of rainfall is: February

Please enter the amount of rain recieved January in inches.6
The month is: February
Please enter the amount of rain recieved for this month in inches.4
The month is: March
Please enter the amount of rain recieved for this month in inches.5
The month is: April
Please enter the amount of rain recieved for this month in inches.2
The month is: May
Please enter the amount of rain recieved for this month in inches.3
The month is: June
Please enter the amount of rain recieved for this month in inches.1
The month is: July
Please enter the amount of rain recieved for this month in inches.2
The month is: August
Please enter the amount of rain recieved for this month in inches.5
The month is: September
Please enter the amount of rain recieved for this month in inches.7
The month is: October
Please enter the amount of rain recieved for this month in inches.9
The month is: November
Please enter the amount of rain recieved for this month in inches.8
The month is: December
Please enter the amount of rain recieved for this month in inches.6
The total amount of rainfall for this year was: 58.0 inches
The average rainfall for this year was: 4.833333333333333 inches
The month with the highest amount of rainfall is: October
The month with the lowest amount of rainfall is: June
'''

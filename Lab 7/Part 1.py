#=============================================================
#    Course-Lab: CS104 -- Lab-07A – Astronomy Helper
#    Filename: Lab7A_AstronomyHelper.py
#    Author: Curtis Collins
#    Purpose: 	To print out information about planets.
#=============================================================

def main():



    print("Please make a selection from the choices below.")
    print("1: Mercury")
    print("2: Venus")
    print("3: Earth")
    print("4: Mars")
    print("5: Exit the program.")


    userInput = int(input("Please enter number here:"))

    
    if userInput == 1:
        print()
        print("Mercury")
        print("-------------------------------------------------------------------")
        print("Average distance from the sun		        57.9 million kilometers")
        print("Mass						3.31 x 10∧23 kg")
        print("Surface temperature				-173 to 430 degrees Celsius")
        
        

    elif userInput == 2:
        print()
        print("Venus")
        print("-------------------------------------------------------------------")
        print("Average distance from the sun		        108.2 million kilometers")
        print("Mass						4.87 x 10∧24 kg")
        print("Surface temperature				472 degrees Celsius")
        


    elif userInput == 3:
        print()
        print("Earth")
        print("-------------------------------------------------------------------")
        print("Average distance from the sun		        149.2 million kilometers")
        print("Mass						5.967 x 10∧24 kg")
        print("Surface temperature				-50 to 50 degrees Celsius")


    elif userInput == 4:
        print()
        print("Mars")
        print("-------------------------------------------------------------------")
        print("Average distance from the sun		        227.9 million kilometers")
        print("Mass						0.6424 x 10∧24 kg")
        print("Surface temperature				-140 to 20 degrees Celsius")



    elif userInput == 5:
        quit()

        
                    


main()

'''
Please make a selection from the choices below.
1: Mercury
2: Venus
3: Earth
4: Mars
5: Exit the program.
Please enter number here:2

Venus
-------------------------------------------------------------------
Average distance from the sun		        108.2 million kilometers
Mass						4.87 x 10∧24 kg
Surface temperature				472 degrees Celsius
>>> ================================ RESTART ================================
>>> 
Please make a selection from the choices below.
1: Mercury
2: Venus
3: Earth
4: Mars
5: Exit the program.
Please enter number here:3

Earth
-------------------------------------------------------------------
Average distance from the sun		        149.2 million kilometers
Mass						5.967 x 10∧24 kg
Surface temperature				-50 to 50 degrees Celsius
>>> ================================ RESTART ================================
>>> 
Please make a selection from the choices below.
1: Mercury
2: Venus
3: Earth
4: Mars
5: Exit the program.
Please enter number here:1

Mercury
-------------------------------------------------------------------
Average distance from the sun		        57.9 million kilometers
Mass						3.31 x 10∧23 kg
Surface temperature				-173 to 430 degrees Celsius
'''

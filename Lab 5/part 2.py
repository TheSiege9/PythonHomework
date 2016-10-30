def main():

    print("This program will add up to 100 numbers. Entering a negative will end the program and display your answer.")
    addArray = [0] * 100
    userNum = int(input("Please enter a number."))
    i = 0
    
    while userNum > 0:

        addArray[i] = userNum

        userNum = int(input("Please enter a number"))

        i = i + 1
    


    print("Your result is:", sum(addArray))

    
main()

'''
This program will add up to 100 numbers. Entering a negative will end the program and display your answer.
Please enter a number.10
Please enter a number10
Please enter a number5
Please enter a number20
Please enter a number56
Please enter a number43
Please enter a number16
Please enter a number-9
Your result is: 160
'''

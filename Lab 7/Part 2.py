#=============================================================
#    Course-Lab: CS104 -- Lab-07B – Alphabetic Number Translator
#    Filename: Lab7B_AlphabeticNumberTranslator.py
#    Author: Curtis Collins
#    Purpose: 		To change letters to the correspoding number on a phone.
#=============================================================



def main():

    userString = input("Please enter your phone number in the format XXXXXXXXXX")


    phoneArray = list(userString)

    outputString = [0] * 10

    i = 0

    while i < 10:


        if phoneArray[i] == "a" or phoneArray[i] == "A" or phoneArray[i] == "b" or phoneArray[i] == "B" or phoneArray[i] == "c" or phoneArray[i] == "C":
            phoneArray[i] = 2

        elif phoneArray[i] == "d" or phoneArray[i] == "D" or phoneArray[i] == "e" or phoneArray[i] == "E" or phoneArray[i] == "f" or phoneArray[i] == "F":
            phoneArray[i] = 3

        elif phoneArray[i] == "g" or phoneArray[i] == "G" or phoneArray[i] == "h" or phoneArray[i] == "H" or phoneArray[i] == "i" or phoneArray[i] == "I":
            phoneArray[i] = 4

        elif phoneArray[i] == "j" or phoneArray[i] == "J" or phoneArray[i] == "k" or phoneArray[i] == "K" or phoneArray[i] == "l" or phoneArray[i] == "L":
            phoneArray[i] = 5

        elif phoneArray[i] == "m" or phoneArray[i] == "M" or phoneArray[i] == "n" or phoneArray[i] == "N" or phoneArray[i] == "o" or phoneArray[i] == "O":
            phoneArray[i] = 6

        elif phoneArray[i] == "p" or phoneArray[i] == "P" or phoneArray[i] == "q" or phoneArray[i] == "Q" or phoneArray[i] == "r" or phoneArray[i] == "R" or phoneArray[i] == "s" or phoneArray[i] == "S":
            phoneArray[i] = 7

        elif phoneArray[i] == "t" or phoneArray[i] == "T" or phoneArray[i] == "u" or phoneArray[i] == "U" or phoneArray[i] == "v" or phoneArray[i] == "V":
            phoneArray[i] = 8

        elif phoneArray[i] == "w" or phoneArray[i] == "W" or phoneArray[i] == "x" or phoneArray[i] == "X" or phoneArray[i] == "y" or phoneArray[i] == "Y" or phoneArray[i] == "z" or phoneArray[i] == "Z":
            phoneArray[i] = 9

        i = i + 1


    x = 0


    while x < 10:

        outputString[x] = str(phoneArray[x])

        x = x + 1
        
    
    
    print(''.join(outputString))


main()

'''
Please enter your phone number in the format XXXXXXXXXXaiemvplqkd
2436875753
>>> ================================ RESTART ================================
>>> 
Please enter your phone number in the format XXXXXXXXXXkaldhencyvu
5253436298
>>> ================================ RESTART ================================
>>> 
Please enter your phone number in the format XXXXXXXXXXjguetdncmj
5483836265
'''

def main():


    quarterlyWater = [0] * 4
    quarter = 1
    averageWater = 0
    i = 0

    while i < 4:


        print("It is quarter", quarter)
        quarterlyWater[i] = int(input("Please enter the amount of water for this quarter"))
        
    
        quarter = quarter + 1
        i = i + 1



    averageWater = round(sum(quarterlyWater) / 12,2)
    

    print("Your bill is: $", averageWater)

    if averageWater > 75:
        print("You are using too much water.")
    elif averageWater >= 25 and averageWater <= 75:
        print("You are using a normal amount of water.")
    else:
        print("You are saving the world water. Thank You!")



main()


'''
>>> 
It is quarter 1
Please enter the amount of water for this quarter300
It is quarter 2
Please enter the amount of water for this quarter200
It is quarter 3
Please enter the amount of water for this quarter225
It is quarter 4
Please enter the amount of water for this quarter275
Your bill is: $ 83.33
You are using too much water.
>>> ================================ RESTART ================================
>>> 
It is quarter 1
Please enter the amount of water for this quarter100
It is quarter 2
Please enter the amount of water for this quarter150
It is quarter 3
Please enter the amount of water for this quarter75
It is quarter 4
Please enter the amount of water for this quarter125
Your bill is: $ 37.5
You are using a normal amount of water.
'''

def main():

    count = 0
    num = 900
    byNine = 0
    byFive = 0
    byTwo = 0
    
    while num > 0:


        if num % 2 == 0:
            count = count + 1
            byTwo = byTwo + 1
        elif num % 5 == 0:
            count = count + 1
            byFive = byFive + 1
        elif num % 9 == 0:
            count = count + 1
            byNine = byNine + 1

        num = num - 1
    
    print("The amount of numbers from 900 to 1 divisible by by 9, 5, or 2 is: " , count)

main()

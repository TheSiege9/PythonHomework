def main():

    bugCount = 0

    for i in range (1,8,1):

        tempCount = 0
        tempCount = input("How many bugs were collected today?")
        tempCount = int(tempCount)
        bugCount = bugCount + tempCount

    print("Your total bugs collected over seven days is:", bugCount)
main()

'''
How many bugs were collected today?5
How many bugs were collected today?10
How many bugs were collected today?2
How many bugs were collected today?3
How many bugs were collected today?8
How many bugs were collected today?7
How many bugs were collected today?4
Your total bugs collected over seven days is: 39
'''

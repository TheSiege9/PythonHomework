#Program 6-2 (random_numbers2.py)
# This program displays five random
# numbers in the range of 1 through 100.

import random
def main():
    for count in range(5):
        # Get a random number from (1, 100]
        number = random.randint(1, 100)        # number from [1, 100], has 10
        number = random.randrange(10)      # number from 1 through 9, no 10, [1, 9]
        number = random.randrange(5, 10)  # the range of 5 through 9, no 10, [5, 9]
        number = random.randrange(0, 41, 10)   # the range [0, 41), 0, 10, 20, 30, 40
    number = random.uniform(1.0, 10.0) 
                 #In this statement the random.uniform function returns a random floating-point  
                 #number in the range of 1.0 through 10.0 and assigns it to the number variable.
        # Display the number.
    print(number)  

# Call the main function.
main()




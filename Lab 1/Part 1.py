
def main():
    # inputs and displays a person’s address, nicely formatted
    print("Program that displays a person’s address, nicely formatted\n")
    firstName = input("Enter your first name: ")
    lastName = input("Now enter your last name: ")
    streetAddress = input("Next enter your street address, (e.g., 943 West Main St.): ")
    city = input("Next enter the name of your city or town: ")
    state = input("Next enter your state: ")
    ZIP = input("Enter your zip-code: ")
    phoneNumber = input("Finally, enter your phone number (e.g., 719-598-0200):")
    print("\nHere is the address of:",firstName,lastName)
    print("\tStreet:\t",streetAddress)
    print("\tCity:\t",city)
    print("\tState:\t",state)
    print("\tZIP:\t",ZIP)
    print("\tPhone Number:\t",phoneNumber)
    
main()

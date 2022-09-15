# Nickname Generator By Aditya
import random

#Variables
nicknames = ["Rest", "In", "Peace", "Lizzy", "Hot", "Forever"]
firstName = input("Please enter your first name:\n")
lastName = input("Please enter your last name:\n")

#Program Loop
programLoop = True

while programLoop:

    # Print the options
    print("SELECT FROM OPTIONS BELOW:")
    print("1: Change Name")
    print("2: Display a Random Nickname")
    print("3: Display All Nicknames")
    print("4: Add a nickname")
    print("5: Remove a Nickname")
    print("6: Exit")

# Get the users Input
    userInput = input("Please enter a selection: \n")


# Change the Name

    if(userInput == "1"):
        newFirst = input("Please Enter your new First Name: \n")
        newLast = input("Please Enter your new Last Name: \n")
        firstName = newFirst
        lastName = newLast
        print("Your new name is:" , firstName , lastName)


# Random Nickname

    elif(userInput == "2"):
          print(firstName, nicknames[random.randint(0, len(nicknames))], lastName) 

# Display All the Nicknames

    elif(userInput == "3"):
          for i in nicknames:
            print(firstName, i, lastName)


# Add A Nickname

    elif(userInput == "4"):
        addName = input("Please Enter a Name to add: \n")

        if addName in nicknames:
            print("Name is Already in the List")
        else:
            nicknames.append(addName)
            print("Name Added")


# Remove a Nickname

    elif(userInput == "5"):
        removeName = input("Please enter a name to remove: ")
        if removeName in nicknames:
            nicknames.remove(removeName)
            print(removeName, "Has been removed")
        else: 
            print(removeName, "has not been found")


# End the Program

    elif (userInput == "6"):
        programLoop = False
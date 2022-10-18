name = input("What is your username? \n")
allowedUsers = ["Tolulope", "Tosin", "Gbemiga"]
allowedPassword = ["PassTolu", "PassTosin", "PassGbemiga"]

if(name in allowedUsers):
    password = input("What is your password? \n")
    userId = allowedUsers.index(name)
    
    if(password in allowedPassword[userId]):
        print("Welcome %s" % name)
        print("Available Options")
        print("Option 1: Check Balance")
        print("Option 2: Withdraw")
        print("Option 3: Transfer")

        selectedOptions = int(input("Please select an option \n"))
        if (selectedOptions == 1):
            print("You have selected option %s" % selectedOptions)
        elif (selectedOptions == 2):
            print("You have selected option %s, please enter the amount you wish to withdraw and press 'Enter'" % selectedOptions)
        elif (selectedOptions == 3):
            print("You have selected option %s, please enter the account number and the amount you wish to transfer and press'Enter'" % selectedOptions)
        else:
            print("Invalid option selected, please try again")
    else:
        print("Invalid user, please enter a valid name")

else:
    print("Name not found, please try again later")
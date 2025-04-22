
global final

def deposition():
    depo = (input("How much would you like to deposit into your account?"))
    while not depo.isdigit():
        depo = int(input("Please enter a number!"))
    return accountBalance(depo)


def withdrawal():
    withdraw = input("How much would you like to withdraw from your account?")
    while not withdraw.isdigit():
        withdraw = int(input("Please enter a number!"))
    c = "-" + str(withdraw)
    return accountBalance(c)


def transactions(trans):
    a = list()
    if trans == 1:
        a.append(1)
    if trans == 2:
        a.append(2)
    if trans == 3:
        a.append(3)
    if trans == 4:
        return retTrans(a)


def retTrans(a):
    for x in a:
        if x == 1:
            print("You checked your account balance")
        elif x == 2:
            print("You deposited into your account")
        elif x == 3:
            print("You withdrew from your account")

    return None


def accountBalance(amount):
    final = 2000
    final+=int(amount)
    return print("You currently have $" + str(final) + " dollars in your account")



def getAccountBalance():
    return print("You currently have $" + str(final) + " dollars in your account")


def terminate():
    response1 = input("Would you like to terminate this transaction? (Y/N)")
    if response1 == "Y":
        return print("Thank you for using ATM service# 12.4")
    elif response1 == "N":
        welcomePage()
    else:
        response1 = input("Please enter either Y or N!")
        while not response1 == "Y" and response1 == "N":
            response1 = input("Please enter either Y or N!")
    return terminate()

def welcomePage():
    print("Welcome " + userName)
    print("Please select an option below:")
    print("Enter 1 to check your account balance")
    print("Enter 2 to deposit into your account")
    print("Enter 3 to withdraw from your account")
    print("Enter 4 for recent transactions within your account")

    response = int(input())

    if response == 1:
        getAccountBalance()
        transactions(1)
    if response == 2:
        deposition()
        transactions(2)
    if response == 3:
        withdrawal()
        transactions(3)
    if response == 4:
        transactions(4)


if __name__ == '__main__':
    count = 4
    userName = input("Please enter your username")
    while not userName.isalpha():
        userName = input("You cannot enter a special char or digit as your username!")
    while not userName == "Patrick":

        if not count == 0:
            userName = input("This user is not in our database. Please try again!")
            print("You have " + str(count - 1) + " more tries left")
            count -= 1
        else:
            print("You have been locked out of your account")
            quit()

    passWord = input("Please enter your password")
    while not passWord.isdigit() or not passWord == "123":
        if not count == 0:
            passWord = input("Incorrect password. Please check for any illegal symbols")
            print("You have " + str(count - 1) + " more tries left")
            count -= 1
        else:
            print("You have been locked out of your account")
            quit()

    welcomePage()
    terminate()

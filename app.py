import os 

# clear the terminal for a cleaner interface (for linux/ mac users)
def clearTerminal():
    os.system('clear')

# takes username and prints it
def printName():
    userName = input("Whats your name? \n")
    clearTerminal()
    return userName

# too complicated to explain
def iDoNothing():
    pass

# prints bigger number from 2 nums
def bigger(n1, n2):
    return n1 if n1 > n2 else n2


clearTerminal()
print('Hello ' + printName())

print(bigger(4,7))


#Variables
age = input("How old are you? ")
continueagever = input("Do you wish to continue?  Yes or no. ")


#Functions
def oldenough():
    print("You may continue. ")
def tooyoung():
    print("You Shall Not Pass! ")

if len(age) == 2:
    oldenough()
else:
    tooyoung()

if oldenough() == True:
    continueagever
if len(continueagever) == 3:
    print("Too bad!!!")
else:
    print("Awwww")

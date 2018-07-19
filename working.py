def print1():
    print("Options are: ")
    print("1 , 2 , 3 , or q")
def option1():
    print("1")
def option2():
    print("2")
def option3():
    print("3")
print1()
answer1 = str(input("What number would you like to go to? "))
while ((answer1 != "quit") and (answer1 != "q")):
        if (answer1 == "1"):
            option1()
        elif (answer1 == "2"):
            option2()
        elif (answer1 == "3"):
            option3()
        else:
            print("Error! Try again!")
        answer1 = str(input("What number would you like to go to? "))
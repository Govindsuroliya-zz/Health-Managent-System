import datetime
# Health Management System.
# 3 clients - Harry , Rohan and Hmmad


def gettime():  # to add date and time in log
    return datetime.datetime.now()


def storedata(userinput):  # for input Data for User.
    if userinput == 1:  # Harry
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            value = input("Enter your Exercise\n")
            with open("Harry-exercise.txt", "a") as op:
                op.write(str([str(gettime())])+" : " + value+"\n")
            print("Successfully Written Value.")
        elif c == 2:
            value = input("Enter your Food\n")
            with open("Harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("Successfully Written Value.")
    elif userinput == 2:  # Rohan
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            value = input("Enter your Exercise\n")
            with open("Rohan-exercise.txt", "a") as op:
                op.write(str([str(gettime())])+" : " + value+"\n")
            print("Successfully Written Value.")
        elif c == 2:
            value = input("Enter your Food\n")
            with open("Rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("Successfully Written Value.")
    elif userinput == 3:  # Hmmad
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            value = input("Enter your Exercise\n")
            with open("Hmmad-exercise.txt", "a") as op:
                op.write(str([str(gettime())])+" : " + value+"\n")
            print("Successfully Written Value.")
        elif c == 2:
            value = input("Enter your Food\n")
            with open("Hmmad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + " : " + value + "\n")
            print("Successfully Written Value.")
        else:
            print("You enter un-valid input")
    else:
        print("Please Enter valid input between 1 to 3")


def output(userinput):  # for user Showinng output for data.
    if userinput == 1:  # Harry
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            with open("Harry-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Harry-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("You enter un-valid input")
    elif userinput == 2:  # Rohan
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            with open("Rohan-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("You enter un-valid input")
    elif userinput == 3:  # hmmad
        c = int(input("Enter 1 for Exercise and 2 for Food"))
        if c == 1:
            with open("Hmmad-exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("Hmmad-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("You enter un-valid input")
    else:
        print("Please Enter valid input between 1 to 3")


print("Welcame to Health Management System \n")
log_ID = "Admin"
log_PASS = "Admin"
# we put User Inputs in Varibles.
print("If you want to exit this program plase press Q")

ID_system = input("Please Enter Your ID.\n")
print("\n")
while ID_system != log_ID:
    if ID_system == "q":
        break
    print("Acess Not Allowed\n")
    ID_system = input("Please Enter Your ID.\n")
    print("\n")
# here serect work in script
if (log_ID == ID_system):
    PASS_system = input("Please Enter Your PASSWORD.\n")
    print("\n")
    while PASS_system != log_PASS:
        if ID_system == "q":
            break
        print("Acess Not Allowed\n")
        PASS_system = input("Please Enter Your PASSWORD.\n")
        print("\n")
    if (log_PASS == PASS_system):
        print("Acess Allowed")
        a = int(input("Press 1 for enter the values or Press 2 for enter show values"))
        if a == 1:
            b = int(input("Press 1 for Harry , Press 2 for Rohan , Press for Hmmad"))
            storedata(b)

        elif a == 2:
            b = int(input("Press 1 for Harry , Press 2 for Rohan , Press for Hmmad"))
            output(b)

        else:
            print("Your Enterd incorrent Value Please try again")

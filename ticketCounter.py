import sys
import os
import time
from datetime import datetime


def clear():
    os.system("clear||cls")


def userInterface():
    print("|===================|")
    print("|Enter '99' to exit.|")
    print("|===================|")
    print("\n")

    print("Enter to get ticket : ")
    x = input(">> ").strip()
    if x == "99":
        sys.exit()

    print("Do you want to get the ticket(y/n): ")
    Ques = input(">> ").strip()
    if Ques == "99":
        sys.exit()

    if Ques != "y":
        clear()
        print("\n| Ticket not taken! Try again! |")

        print("\n")

        userInterface()
    else:
        print("Thankyou for using.......... ")

        try:
            file = open("Data.txt", "r")
            read = int(file.read())
            file.close()
        except:
            file = open("Data.txt", "w")
            file.write("0")
            file.close()
            clear()
            print("Error found! Try again!")
            userInterface()

        ticket = read + 1
        write = str(ticket)

        file = open("Data.txt", "w")
        file.write(write)
        file.close()

        gotoStaff(write)

        print(f"Your ticket number is {ticket}")
        time.sleep(5)

        clear()
        userInterface()


def gotoStaff(write):
    # print("going to the staff for further inqeury..........")
    file = open("staffInterface.txt", "a")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(write + "\t")
    file.write(timestamp)
    file.write("\n")
    file.close()


clear()

userInterface()

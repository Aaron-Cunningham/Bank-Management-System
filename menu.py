import pandas as pd
from pathlib import Path
from datetime import datetime
import random
from self import self


class menu:
    # Sets the column and row display options
    clients = Path(__file__).parent / "data/client_data.csv"
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    def menu(self):
        """Creates a menu system with the print function"""

        print("************************************************")
        print()
        print("             Bank Management Console           ")
        print()
        print("************************************************\n"
              )
        default = 0
        print("Select 1 to view all clients\n"
              "Select 2 to remove account holders\n"
              "Select 3 to add a new account\n"
              "Select 4 to add money to an account\n"
              "Select 5 to remove money to an account\n"
              "Select 6 to edit a clients deatils\n"
              "\n"
              "************************************************")
        # Exception so only users can input ints
        try:
            option = int(input("Enter your choice: "))
        except:
            print("Enter int values only")
            menu.menu(self)

        # Menu option buttons
        if option == 1:
            print(
                "********************************************************************************************************************************************\n"
                "                                                                 CLIENTS                                                                    \n"
                "********************************************************************************************************************************************")
            menu.viewClients(self)
        elif option == 2:
            menu.remove(self)
        elif option == 3:
            menu.addClient(self)
        elif option != default:
            print("Only input a number specified")
            menu.menu(self)

    def viewClients(self):
        """Views clients in the CSV file"""
        clients = pd.read_csv("data/client_data.csv")
        print(clients)
        print("Would you like to return to the menu?\n"
              "1: Yes\n"
              "2: Exit")
        option = int(input('Enter your option: '))
        if option == 1:
            menu.menu(self)
        elif option == 2:
            exit()

    def remove(self):
        clients = pd.read_csv("data/client_data.csv")

        print(clients)

        AccountNumber = int(input("Enter the account number of the account you wish to delete"))
        clients.drop(clients[clients['Account Number'] == AccountNumber].index, inplace=True)
        clients.to_csv("data/client_data.csv", index = False)
        print(clients)
        print("****************************************\n"
              "           Client deleted                \n"
              "****************************************")
        print("Would you like to return to the menu?\n"
              "1: Yes\n"
              "2: Exit")
        option = int(input('Enter your option: '))
        if option == 1:
            menu.menu(self)
        elif option == 2:
            exit()

    def addClient(self):
        """Adds a new client to the CSV file/Bank"""
        # User inputs when adding a new client
        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        title = input("Enter Title: ")
        occupation = input("Enter Occupation: ")
        accountNumber = random.randint(4000, 4999)
        # While loop until user enters right format
        while True:
            # Try except when user enters wrong values
            try:
                birthday = "29/01/1999" #input("Enter Birthday in this format dd/m/yyyy: ")
                dateOfBirth = datetime.strptime(birthday, '%d/%m/%Y').date()
                # Breaks out of loop
                break
            except:
                print("Enter in this format dd/m/yyyy")
        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                accountBalance = int(input("Enter account balance: "))
                # Breaks out of loop
                break
            except ValueError:
                print("Enter only int values")
        while True:
            try:
                overDraftLimit = int(input("Enter overdraft limit: "))
                break
            except ValueError:
                print("Enter only int values")

        # Reads CSV file
        clients = pd.read_csv("data/client_data.csv")
        # Adds data based on what was inputted
        clients.loc[len(clients)] = [firstName, lastName, title, accountNumber, dateOfBirth, occupation, accountBalance,
                                     overDraftLimit]
        clients.to_csv("data/client_data.csv", index = False)
        print(clients)
        print("****************************************\n"
              "        Successfully Added Client               \n"
              "****************************************")
        print("Would you like to return to the menu?\n"
              "1: Yes\n"
              "2: Exit")
        # Options to return to menu or exit program
        option = int(input('Enter your option: '))
        if option == 1:
            menu.menu(self)
        elif option == 2:
            exit()




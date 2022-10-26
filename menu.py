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
              "Select 5 to withdraw money from an account\n"
              "Select 6 to edit a clients deatils\n"
              "Select 7 to search for a specific client\n"
              "Select 8 to exit the program"
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
            menu.viewClients(self, clients=True)
        elif option == 2:
            menu.remove(self)
        elif option == 3:
            menu.addClient(self)
        elif option == 4:
            menu.depositMoney(self)
        elif option == 5:
            menu.withdrawMoney(self)
        elif option == 7:
            menu.accountSearch(self)
        elif option == 8:
            exit()
        elif option != default:
            print("Only input a number specified")
            menu.menu(self)


    def viewClients(self, clients):
        """Views all clients in the CSV file"""
        clients = pd.read_csv("data/client_data.csv")
        print(clients)
        menu.returnToMenu(self)

    def remove(self):
        clients = pd.read_csv("data/client_data.csv")

        print(clients)
        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                AccountNumber = int(input("Enter the account number of the account you wish to delete"))
                # Breaks out of loop
                break
            except ValueError:
                print("Enter only int values")
        clients.drop(clients[clients['Account Number'] == AccountNumber].index, inplace=True)
        # clients.to_csv("data/client_data.csv", index = False)
        print(clients)
        print("****************************************\n"
              "           Client deleted                \n"
              "****************************************")
        menu.returnToMenu(self)

    def addClient(self):
        """Adds a new client to the CSV file/Bank"""
        print("****************************************\n"
              "           Add Client Details               \n"
              "****************************************")
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
                birthday = "29/01/1999"  # input("Enter Birthday in this format dd/m/yyyy: ")
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
        # clients.to_csv("data/client_data.csv", index = False)
        print(clients)
        print("****************************************\n"
              "        Successfully Added Client               \n"
              "****************************************")
        menu.returnToMenu(self)


    def depositMoney(self):
        """This function deposits money to a clients account"""
        # Reads CSV file
        clients = pd.read_csv("data/client_data.csv")
        print(clients)
        print("*******************************************************************************")
        print()
        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the user to enter the account number to add money to
                accountNumber = int(input("     Enter the account number of the account you wish to deposit money to: "))
                # Breaks out of loop when int value added
                break
            except ValueError:
                print("Enter only int values")
        print("*******************************************************************************")
        print()

        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the desired deposit amount
                deposit = int(input("     Enter the amount you wish to deposit: "))
                # Breaks out of loop when int value added
                break
            except ValueError:
                print("Enter only int values")
        # Locates the row of the account number that matches input from user and edits balance from users input
        clients.loc[clients['Account Number']==accountNumber, ['Account balance']] = clients['Account balance'] + deposit
        print(clients)
        print("*********************************************\n"
              "           Clients money deposited                \n"
              "*********************************************")
        clients.to_csv("data/client_data.csv", index = False)
        menu.returnToMenu(self)


    def withdrawMoney(self):
        """This function withdraws money from a clients account"""
        # Reads CSV file
        clients = pd.read_csv("data/client_data.csv")
        # Fee variable to charge for overdraft
        fee = 5
        print(clients)
        print("*******************************************************************************")
        print()

        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the user to enter the account number to add money to
                accountNumber = int(
                    input("     Enter the account number of the account you wish to withdraw money from: "))
                # Breaks out of loop when int used
                break
            except ValueError:
                print("Enter only int values")
        print("*******************************************************************************")
        print()
        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the desired deposit amount
                withdraw = int(input("     Enter the amount you wish to withdraw: "))
                # Breaks out of loop when int used
                break
            except ValueError:
                print("Enter only int values")

        # Locates the row of the account number that matches input from user and edits balance from users input
        clients.loc[clients['Account Number'] == accountNumber, ['Account balance']] = clients['Account balance'] - withdraw
        # Adds £5 fee if the client goes over their overdraft limit
        clients.loc[clients['overdraft limit'] > clients['Account balance'], 'Account balance']-=fee
        # Writes to CSV file with updated data
        clients.to_csv("data/client_data.csv", index = False)


        print(clients)
        print("*********************************************\n"
              "           Clients money deposited                \n"
              "*********************************************")

        menu.returnToMenu(self)

    def accountSearch(self):
        """This function views data of a specific client using account number"""
        default = 0
        clients = pd.read_csv("data/client_data.csv")
        print()
        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for account number
                accountNumber = int(input('*********************************************\n'
                                          '      Enter Account number of client: '))
                # Breaks out of loop when int used
                break
            except ValueError:
                print("Enter only int values")

        print()

        client = (clients.loc[clients['Account Number'] == accountNumber])
        print(client)
        print()
        print("*********************************************")
        menu.returnToMenu(self)


    def returnToMenu(self):
        """Function that returns user back to the menu"""
        default=0
        print("Would you like to return to the menu?\n"
              "1: Yes\n"
              "2: Exit")
        while True:
            # Try except when user enters wrong value in input
            try:
                option = int(input('Enter your option: '))
                # Breaks out of loop
                break
            except ValueError:
                print("Menu options only!")
                menu.returnToMenu(self)
        # Menu options
        if option == 1:
            menu.menu(self)
        elif option == 2:
            exit()
        elif option != default:
            menu.returnToMenu(self)
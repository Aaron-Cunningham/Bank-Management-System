import re

import pandas as pd
# from menu import Menu
import random
from self import self


# Creates menu object to use functions from menu
# menu = Menu()

class Functions:
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    def viewClients(self):
        """Views all clients in the CSV file"""
        clients = pd.read_csv("data/client_data.csv")
        print(clients)
        Functions.returnToMenu(self)

    def removeClient(self):
        from menu import Menu
        clients = pd.read_csv("data/client_data.csv")
        # option variable set at 0 default
        option = 0
        default = 0

        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                accountNumber = int(input("Enter the account number of the account you wish to delete: "))
                # Breaks out of loop
                break
            except ValueError:
                print("Enter only int values")

        # While loop while condition is true
        while True:
            # Trys to find account holder with user input
            try:
                accountHolder = (clients.loc[clients['Account Number'] == accountNumber])
                # If Data set is empty(Client can't be found)
                if accountHolder.empty == True:
                    raise Exception
                break
                # Catches exception to allow re-search
            except:
                print("No account found, would you like to try again?\n"
                      "1: Yes\n"
                      "2: Return to menu")
                # Try except to
                try:
                    option = int(input("Enter your choice: "))
                except:
                    print("Enter int values only")
                if option == 1:
                    Functions.removeClient(self)
                elif option == 2:
                    Menu.menu(self)
                    break
        print('*' * 107)
        print(accountHolder)
        print('*' * 107)
        print("Are you sure you want to remove this account?\n"
              "1: Yes\n"
              "2: Return to menu")
        while True:
            # Try except when user enters wrong value in input
            try:
                option = int(input('Enter your option: '))
                # Breaks out of loop
                break
            except ValueError:
                print("Menu options only!")

        # Menu options
        if option == 1:
            clients.drop(clients[clients['Account Number'] == accountNumber].index, inplace=True)
        elif option == 2:
            Menu.menu(self)
        elif option != default:
            print("Not a valid input, aborted deletion")
            Menu.menu(self)
        clients.to_csv("data/client_data.csv", index = False)
        print('*' * 107)
        print("                                            Client deleted                                  ")
        print('*' * 107)
        Functions.returnToMenu(self)

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
                dateOfBirth = input("Enter Birthday in this format mm/dd/yyyy: ")
                # dateOfBirth = datetime.strptime(birthday, '%m/%d/%Y').date()
                # birthday = pd.to_datetime(pd.Series(input("Enter Birthday in this format m/dd/yyyy: ")))
                # dateOfBirth = birthday.dt.strftime('%m/%d/%Y')
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
                if overDraftLimit > 0:
                    print("Enter only negative values")
                elif overDraftLimit < 0:

                    break
            except ValueError:
                print("Enter only int values")

        # Reads CSV file
        clients = pd.read_csv("data/client_data.csv")
        # Adds data based on what was inputted
        clients.loc[len(clients)] = [firstName, lastName, title, accountNumber, dateOfBirth, occupation, accountBalance,
                                     overDraftLimit]
        clients.to_csv("data/client_data.csv", index=False)
        print(clients)
        print("****************************************\n"
              "        Successfully Added Client               \n"
              "****************************************")
        Functions.returnToMenu(self)

    def depositMoney(self):
        """This function deposits money to a clients account"""

        from menu import Menu
        # Reads CSV file
        clients = pd.read_csv("data/client_data.csv")

        print("*" * 79)
        print()
        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the user to enter the account number to add money to
                accountNumber = int(
                    input("Enter the account number of the account you wish to deposit money to: "))
                # Breaks out of loop when int value added
                break
            except ValueError:
                print("Enter only int values")
        print("*" * 79)
        print()
        # accountHolder = (clients.loc[clients['Account Number'] == accountNumber])

        # While loop while condition is true
        while True:
            # Trys to find account holder with user input
            try:
                accountHolder = (clients.loc[clients['Account Number'] == accountNumber])
                # If Data set is empty(Client can't be found)
                if accountHolder.empty == True:
                    raise Exception
                break
                # Catches exception to allow research
            except:
                print("No account found, would you like to try again?\n"
                      "1: Yes\n"
                      "2: Return to menu")
                try:
                    option = int(input("Enter your choice: "))
                except:
                    print("Enter int values only")
                if option == 1:
                    Functions.depositMoney(self)
                elif option == 2:
                    Menu.menu(self)
                    break

        print(accountHolder)
        print()
        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the desired deposit amount
                deposit = int(input("Enter the amount you wish to deposit: "))
                if deposit < 0:
                    print("Positive values only")
                elif deposit > 0:
                    # Breaks out of loop when correct int value added
                    break
            except ValueError:
                print("Enter only int values")
        print("*" * 48)
        print()
        # Locates the row of the account number that matches input from user and edits balance from users input
        clients.loc[clients['Account Number'] == accountNumber, ['Account balance']] = clients[
                                                                                           'Account balance'] + deposit

        updatedAmount = (clients.loc[clients['Account Number'] == accountNumber])
        # prints clients details with updated deposit amount
        print()
        print('*' * 107)
        print()
        print(updatedAmount)
        print("*" * 107)
        print("                                         Clients money deposited                                     ")
        print("*" * 107)

        clients.to_csv("data/client_data.csv", index=False)
        Functions.returnToMenu(self)

    def withdrawMoney(self):
        """This function withdraws money from a clients account"""
        from menu import Menu
        # Reads CSV file
        clients = pd.read_csv("data/client_data.csv")
        # Fee variable to charge for overdraft
        fee = 5
        print("*" * 48)
        print()

        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the user to enter the account number to add money to
                accountNumber = int(
                    input("Enter the account number of the account you wish to withdraw money from: "))
                # Breaks out of loop when int used
                break
            except ValueError:
                print("Enter only int values")

        # While loop while condition is true
        while True:
            # Trys to find account holder with user input
            try:
                accountHolder = (clients.loc[clients['Account Number'] == accountNumber])

                # If Data set is empty(Client can't be found)
                if accountHolder.empty == True:
                    raise Exception
                break
                # Catches exception to allow research
            except:
                print("No account found, would you like to try again?\n"
                      "1: Yes\n"
                      "2: Return to menu")
                try:
                    option = int(input("Enter your choice: "))
                except:
                    print("Enter int values only")
                if option == 1:
                    Functions.withdrawMoney(self)
                elif option == 2:
                    Menu.menu(self)
                    break
        print("*" * 48)
        print()
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print(client)
        # While loop until user enters int values
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the desired deposit amount
                withdraw = int(input("Enter the amount you wish to withdraw: "))
                if withdraw < 0:
                    print("Positive integers only")
                elif withdraw > 0:
                    # Breaks out of loop when int used
                    break
            except ValueError:
                print("Enter only int values")

        # Locates the row of the account number that matches input from user and edits balance from users input
        clients.loc[clients['Account Number'] == accountNumber, ['Account balance']] = clients[
                                                                                           'Account balance'] - withdraw
        # Adds £5 fee if the client goes over their overdraft limit
        clients.loc[clients['overdraft limit'] > clients['Account balance'], 'Account balance'] -= fee
        # Writes to CSV file with updated data
        clients.to_csv("data/client_data.csv", index=False)

        updatedAmount = (clients.loc[clients['Account Number'] == accountNumber])
        # prints clients details with updated withdrawn amount
        print()
        print('*' * 107)
        print()
        print(updatedAmount)
        print("*" * 107)
        print("                                         Clients money withdrawn                                     ")
        print("*" * 107)

        Functions.returnToMenu(self)

    def accountSearch(self):
        """This function searches data of a specific client using name and date of birth"""
        from menu import Menu
        default = 0
        self.clients = clients = pd.read_csv("data/client_data.csv")
        print()
        # while loop when condition is true
        while True:
            firstName = input("Input first name: ")
            # if statement which rejects anything other than characters
            if not firstName.isalpha():
                print('Enter only letters')
                continue
            else:
                # loop breaks when condition is met
                break
        # while loop when condition is true
        while True:
            lastName = input("Input second name: ")
            # if statement which rejects anything other than characters
            if not lastName.isalpha():
                print('Enter only letters')
                continue
            else:
                # loop breaks when condition is met
                break
        while True:
            dateOfBirth = re.compile(r'[a-zA-Z]*$')
            if (dateOfBirth.match(input("Input date of birth mm/dd/yyyy: "))):
                print('Only D.O.B allowed, try again')
                continue
            else:
                break

        while True:
            try:
                # Searches the columns with matching info. Not case-sensitive
                accountHolder = (clients.loc[clients['First name'].str.contains(firstName, case=False) & (
                    clients['Last name'].str.contains(lastName, case=False)) & (
                                                 clients['Date of birth'].str.contains(dateOfBirth))])
                if accountHolder.empty == True:
                    raise Exception
                break
            except:
                print("No account found, would you like to try again?\n"
                      "1: Yes\n"
                      "2: Return to menu")
            try:
                option = int(input("Enter your choice: "))
            except:
                print("Enter int values only")
            if option == 1:
                Functions.accountSearch(self)
            elif option == 2:
                Menu.menu(self)
                break

        print(accountHolder)
        print("*********************************************")
        Functions.returnToMenu(self)

    def returnToMenu(self):
        '''Function that returns user back to the menu or exits the program'''
        from menu import Menu

        """Function that returns user back to the menu"""
        default = 0
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
                Menu.returnToMenu(self)
        # Menu options
        if option == 1:
            Menu.menu(self)
        elif option == 2:
            exit()
        elif option != default:
            Menu.returnToMenu(self)

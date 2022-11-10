import random
import pandas as pd
import re
import people as people




# Sets the column and row display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

clients = pd.read_csv("data/client_data.csv")
default = 0



class Menu:

    def __init__(self):


        self.menuChoices = {
            "1": self.view_clients,
            "2": self.remove_client,
            "3": self.add_client,
            "4": self.deposit_money,
            "5": self.withdraw_money,
            "6": self.edit_client,
            "7": self.account_search,
            "8": self.negativeBalance,
            "9": self.exit
        }

        self.returnMenuChoices = {
            "1": self.run,
            "2": self.exit
        }


    def menu(self):
        """Creates a menu system with the print function"""

        print("*" * 48)
        print()
        print("             Bank Management Console           ")
        print()
        print("*" * 48)

        print("Select 1 to view all clients\n"
              "Select 2 to remove a client\n"
              "Select 3 to add a client\n"
              "Select 4 to deposit money\n"
              "Select 5 to withdraw money\n"
              "Select 6 to edit a client\n"
              "Select 7 to search for an account\n"
              "Select 8 to see clients with a negative balance\n"
              "Select 9 to exit")
        print("*"*48)

    def run(self):
        """Displays the menu and allows the user to input a choice"""
        while True:
            Menu.menu(self)
            option = input("Enter an option: ")
            select = self.menuChoices.get(option)
            if select:
                # If a user selects a valid option it will run
                select()
            else:
                # Stops the user putting an invalid input
                print("{0} is not a valid choice".format(option))

    def returnToMenu(self):
        '''Function that returns user back to the menu or exits the program'''
        print("Would you like to return to the menu?\n"
              "1: Yes\n"
              "2: Exit")
        while True:
            option = input("Enter an option: ")
            select = self.returnMenuChoices.get(option)
            if select:
                select()
            else:
                print("{0} is not a valid choice\n"
                      "Would you like to return to the menu?\n"
                      "1: Yes\n"
                      "2: Exit".format(option))

    def view_clients(self):
        """Views all clients in the CSV file"""
        print("*" * 140)
        print(
            "                                                                 CLIENTS                                                                    ")
        print("*" * 140)
        All.view_all()
        self.returnToMenu()

    def remove_client(self):

        # option variable set at 0 default
        option = 0

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
                    self.remove_client()
                elif option == 2:
                    self.run()
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
            self.run()
        elif option != default:
            print("Not a valid input, aborted deletion")
            self.run()
        clients.to_csv("data/client_data.csv", index=False)
        print('*' * 107)
        print("                                            Client deleted                                  ")
        print('*' * 107)
        self.run()

    def add_client(self):
        """Adds a new client to the CSV file/Bank"""
        print("****************************************\n"
              "           Add Client Details               \n"
              "****************************************")
        # User inputs when adding a new client
        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        title = input("Enter Title: ")
        pronoun = input("Enter pronoun: ")
        occupation = input("Enter Occupation: ")
        accountNumber = random.randint(4000, 4999)
        # While loop until user enters right format
        while True:
            # Try except when user enters wrong values
            try:
                dateOfBirth = input("Enter Birthday in this format mm/dd/yyyy: ")

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

        # Adds data based on what was inputted
        clients.loc[len(clients)] = [firstName, lastName, title, pronoun, accountNumber, dateOfBirth, occupation,
                                     accountBalance,
                                     overDraftLimit]
        clients.to_csv("data/client_data.csv", index=False)
        print(clients)
        print("****************************************\n"
              "        Successfully Added Client               \n"
              "****************************************")
        self.returnToMenu()

    def deposit_money(self):
        """This function deposits money to a clients account"""
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
                    self.deposit_money()
                elif option == 2:
                    self.returnToMenu()
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
        print(
            "                                         Clients money deposited                                     ")
        print("*" * 107)

        clients.to_csv("data/client_data.csv", index=False)
        self.returnToMenu()

    def withdraw_money(self):
        """This function withdraws money from a clients account"""

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
                    self.withdraw_money()
                elif option == 2:
                    self.run()
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
                print("*" *24, "WARNING", "*"*24 )
                print("£5 charge for account going over withdraw limit")
                print("*"*57)
                withdraw = int(input("Enter the amount you wish to withdraw: "))
                if withdraw < 0:
                    print("Positive integers only")
                elif withdraw > 0:
                    # Breaks out of loop when int used
                    break
            except ValueError:
                print("Enter only int values")

        # Locates the row of the account number that matches input from user and edits balance from users input
        clients.loc[clients['Account Number'] == accountNumber, ['Account balance']] = clients['Account balance'] - withdraw
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

        self.returnToMenu()

    def account_search(self):
        """This function searches data of a specific client using name and date of birth"""

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
                self.account_search()
            elif option == 2:
                self.run()
                break

        print(accountHolder)
        print("*********************************************")
        self.returnToMenu()

    def returnToMenu(self):
        '''Function that returns user back to the menu or exits the program'''

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

        # Menu options
        if option == 1:
            self.run()
        elif option == 2:
            exit()
        elif option != default:
            self.run()

    def edit_client(self):

        print("What would you like to edit? \n"
              "Select 1 for first name\n"
              "Select 2 for last name\n"
              "Select 3 for title\n"
              "Select 4 for occupation")
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
            self.edit_name()
        elif option == 2:
            self.edit_last_name()
        elif option == 3:
            self.edit_title()
        elif option == 4:
            self.edit_occupation()
        elif option != default:
            self.edit_client()
        elif option == 5:
            self.run()

    def exit(self):
        exit()

    def negativeBalance(self):
        """

        This function returns a list of clients with a negative balance in their account

        """
        print("*"*107)
        print(
            "                                         Clients with negative balance                                     ")
        print("*"*107)
        All.view_negative()
        self.returnToMenu()

    def edit_name(self):
        from menu import Menu
        """Allows the clients name to be edited"""
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the user to enter the account number to add money to
                accountNumber = int(
                    input("Enter the account number of the account you wish to edit: "))
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
                    self.edit_name()
                elif option == 2:
                    self.menu()
                    break
        # Finds the client with the inputted account number
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*' * 107)
        print(client)
        print("*" * 107)
        # newName variable set as an input for the new name of the client
        newName = input("Enter the name you want to change to: ")
        # Updates the clients name
        clients.loc[(clients['Account Number'] == accountNumber), 'First name'] = newName
        # Gets an updated list of the client
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*" * 107)
        # Prints updated client details
        print(updatedClient)
        print("*" * 107)
        # Writes updated client details
        clients.to_csv("data/client_data.csv", index=False)
        print('*' * 107)
        print(
            "                                         Clients information updated                                     ")
        print('*' * 107)

        self.run()

    def edit_last_name(self):
        """Allows the clients last name to be edited"""
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the user to enter the account number to add money to
                accountNumber = int(
                    input("Enter the account number of the account you wish to edit: "))
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
                    self.edit_last_name()
                elif option == 2:
                    self.menu()
                    break
        # Finds the account associated with the account number inputted
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*' * 107)
        # Prints the client with old details
        print(client)
        print("*" * 107)
        # newName variable set to an input for the uer to input the new name
        newName = input("Enter the last name you want to change to: ")
        # Updates the account with the new name inputted
        clients.loc[(clients['Account Number'] == accountNumber), 'Last name'] = newName
        # Gets an updated list of the client
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*" * 107)
        # Prints updated client details
        print(updatedClient)
        print("*" * 107)
        # Writes updated client details to CSV file
        clients.to_csv("data/client_data.csv", index=False)
        print('*' * 107)
        print(
            "                                         Clients information updated                                     ")
        print('*' * 107)
        self.run()

    def edit_title(self):
        """Edits the clients title"""
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the user to enter the account number to add money to
                accountNumber = int(
                    input("Enter the account number of the account you wish to edit: "))
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
                    self.edit_title()
                elif option == 2:
                    self.menu()
                    break
        # Client is matched with the account number inputted
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*' * 107)
        print(client)
        print("*" * 107)
        # newTitle varible set for the user to enter the new title for the client
        newTitle = input("Enter the title you want to change to: ")
        # Updates the clients title
        clients.loc[(clients['Account Number'] == accountNumber), 'Title'] = newTitle
        # Retrieves an updated list of clients
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*" * 107)
        # Prints updated clients details
        print(updatedClient)
        print("*" * 107)
        # Writes the updated list to the CSV file
        clients.to_csv("data/client_data.csv", index=False)
        print('*' * 107)
        print(
            "                                         Clients information updated                                     ")
        print('*' * 107)
        self.run()

    def edit_occupation(self):
        """Allows the clients occupation to be edited"""
        while True:
            # Try except when user enters wrong value in input
            try:
                # Input for the user to enter the account number to add money to
                accountNumber = int(
                    input("Enter the account number of the account you wish to edit: "))
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
                    self.edit_occupation()
                elif option == 2:
                    self.menu()
                    break
        # Clients account is equal to the account number inputted
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*' * 107)
        print(client)
        print("*" * 107)
        # newOccupation variable set to an input from the user to change to
        newOccupation = input("Enter the occupation you want to change to: ")
        # Updated the clients details with the new inputted occupation
        clients.loc[(clients['Account Number'] == accountNumber), 'Occupation'] = newOccupation
        # updatedClient variable to fetch the updated list with the new client details
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*" * 107)
        print(updatedClient)
        print("*" * 107)
        # Saves the new updated information to a CSV file
        clients.to_csv("data/client_data.csv", index=False)
        print('*' * 107)
        print(
            "                                         Clients information updated                                     ")
        print('*' * 107)
        self.returnToMenu()



All = people.AllClients()
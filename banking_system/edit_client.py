from self import self
import pandas as pd
clients = pd.read_csv("../data/client_data.csv")
class edit_client():

    def __init__(self):
        pass

    def edit_name(self):
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
                    self.withdraw_money()
                elif option == 2:
                    self.run()
                    break
        # Finds the client with the inputted account number
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*'*107)
        print(client)
        print("*"*107)
        # newName variable set as an input for the new name of the client
        newName = input("Enter the name you want ot change to: ")
        # Updates the clients name
        clients.loc[(clients['Account Number'] == accountNumber),'First name'] = newName
        # Gets an updated list of the client
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*"*107)
        # Prints updated client details
        print(updatedClient)
        print("*"*107)
        # Writes updated client details
        clients.to_csv("../data/client_data.csv", index=False)
        print('*'*107)
        print("                                         Clients information updated                                     ")
        print('*'*107)

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
                    self.withdraw_money()
                elif option == 2:
                    self.run()
                    break
        # Finds the account associated with the account number inputted
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*'*107)
        # Prints the client with old details
        print(client)
        print("*"*107)
        # newName variable set to an input for the uer to input the new name
        newName = input("Enter the last name you want ot change to: ")
        # Updates the account with the new name inputted
        clients.loc[(clients['Account Number'] == accountNumber),'Last name'] = newName
        # Gets an updated list of the client
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*"*107)
        # Prints updated client details
        print(updatedClient)
        print("*"*107)
        # Writes updated client details to CSV file
        clients.to_csv("../data/client_data.csv", index=False)
        print('*'*107)
        print("                                         Clients information updated                                     ")
        print('*'*107)

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
                    self.withdraw_money()
                elif option == 2:
                    self.run()
                    break
        # Client is matched with the account number inputted
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*' * 107)
        print(client)
        print("*" * 107)
        # newTitle varible set for the user to enter the new title for the client
        newTitle = input("Enter the last name you want ot change to: ")
        # Updates the clients title
        clients.loc[(clients['Account Number'] == accountNumber), 'Title'] = newTitle
        # Retrieves an updated list of clients
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*" * 107)
        # Prints updated clients details
        print(updatedClient)
        print("*" * 107)
        # Writes the updated list to the CSV file
        clients.to_csv("../data/client_data.csv", index=False)
        print('*' * 107)
        print(
            "                                         Clients information updated                                     ")
        print('*' * 107)

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
                    self.withdraw_money()
                elif option == 2:
                    self.run()
                    break
        # Clients account is equal to the account number inputted
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*' * 107)
        print(client)
        print("*" * 107)
        # newOccupation variable set to an input from the user to change to
        newOccupation = input("Enter the last name you want ot change to: ")
        # Updated the clients details with the new inputted occupation
        clients.loc[(clients['Account Number'] == accountNumber), 'Occupation'] = newOccupation
        # updatedClient variable to fetch the updated list with the new client details
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*" * 107)
        print(updatedClient)
        print("*" * 107)
        # Saves the new updated information to a CSV file
        clients.to_csv("../data/client_data.csv", index=False)
        print('*' * 107)
        print(
            "                                         Clients information updated                                     ")
        print('*' * 107)










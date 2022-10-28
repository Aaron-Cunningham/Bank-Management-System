from self import self
import pandas as pd



clients = pd.read_csv("../data/client_data.csv")

class edit_client:
    def __init__(self):
        pass

    def edit_name(self):
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
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*'*107)
        print(client)
        print("*"*107)
        newName = input("Enter the name you want ot change to: ")
        clients.loc[(clients['Account Number'] == accountNumber),'First name'] = newName
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*"*107)
        print(updatedClient)
        print("*"*107)
        clients.to_csv("../data/client_data.csv", index=False)
        print('*'*107)
        print("                                         Clients information updated                                     ")
        print('*'*107)


    def edit_last_name(self):
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
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*'*107)
        print(client)
        print("*"*107)
        newName = input("Enter the last name you want ot change to: ")
        clients.loc[(clients['Account Number'] == accountNumber),'Last name'] = newName
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*"*107)
        print(updatedClient)
        print("*"*107)
        clients.to_csv("../data/client_data.csv", index=False)
        print('*'*107)
        print("                                         Clients information updated                                     ")
        print('*'*107)

    def edit_title(self):
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
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*' * 107)
        print(client)
        print("*" * 107)
        newTitle = input("Enter the last name you want ot change to: ")
        clients.loc[(clients['Account Number'] == accountNumber), 'Title'] = newTitle
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*" * 107)
        print(updatedClient)
        print("*" * 107)
        clients.to_csv("../data/client_data.csv", index=False)
        print('*' * 107)
        print(
            "                                         Clients information updated                                     ")
        print('*' * 107)

    def edit_occupation(self):
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
        client = (clients.loc[clients['Account Number'] == accountNumber])
        print('*' * 107)
        print(client)
        print("*" * 107)
        newTitle = input("Enter the last name you want ot change to: ")
        clients.loc[(clients['Account Number'] == accountNumber), 'Occupation'] = newTitle
        updatedClient = (clients.loc[clients['Account Number'] == accountNumber])
        print("*" * 107)
        print(updatedClient)
        print("*" * 107)
        clients.to_csv("../data/client_data.csv", index=False)
        print('*' * 107)
        print(
            "                                         Clients information updated                                     ")
        print('*' * 107)










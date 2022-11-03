import pandas as pd
import typer


# Class definition
class Users():

    # constructor/initialiser
    def __init__(self, users):
        # Users properties and attribute
        self.__users = users
        # Fee that is changeable
        self.__fee = 5
        # List of clients in the bank
        self.__client = pd.read_csv("../data/client_data.csv")

    def view_all(self):
        """
        This method searches for all the clients in the CSV file and then prints them out

        """
        # Prints all the clients from the bank
        print(f"{self.__client}")

    def search(self, account):

        """
        This method searches for an account using the account number, then it prints the account.
        """
        account = Users(self.__client.loc[self.__client['Account Number'] == account])

        print(f"{account.__users}")

    def search_by_name(self, first_name, last_name, date_of_birth):
        """
        This method search the clients of the bank by name and date of birth.

        It is not case-sensitive.

        """
        # While loop while condition is true
        while True:
            # Trys to find the account
            try:
                __accountHolder = Users(
                    self.__client.loc[self.__client['First name'].str.contains(first_name, case=False) & (
                        self.__client['Last name'].str.contains(last_name, case=False)) & (
                                          self.__client['Date of birth'].str.contains(date_of_birth))])
                if __accountHolder.__users.empty:
                    raise Exception

                # Catches exception
            except:
                print("No account found, please try again")
                # Breaks out of while loop when this condition is met
                break
            else:
                # If account is found it will print it
                print(f"{__accountHolder.__users}")
                # Breaks out of while loop when condition is met
                break

    def add_client(self, first_name, last_name, title, account_number, date_of_birth, occupation, account_balance,
                   overdraft_limit):
        """This method allows a client to be added to the bank.

        It takes the users first name, last name, title, account number, date of birth, occupation,
        account balance, and overdraft limit.

        String values are only allowed for the first name, last name, title, and occupation.
        """
        # Only allows first name to be a string
        if first_name.isalpha() == False:
            print("First name takes string values only")
            exit()
        # Only allows last name to be a string
        elif last_name.isalpha() == False:
            print("Last name takes string values only")
            exit()
        # Only allows title to be a string
        elif title.isalpha() == False:
            print("Title takes string values only")
            exit()
        # Only allows date of birth to be int/special char values
        elif date_of_birth.isalpha() == True:
            print("Please fill out the date of birth in this order MM/DD/YYYY")
            exit()
        # Only allows for string values
        elif occupation.isalpha() == False:
            print("Occupation takes string values only")
            exit()
        # Only allows account balance to be positive
        elif account_balance < 0:
            print("No negative balances for account balance")
            exit()
            # Only allows overdraft limit to be negative
            exit()
        elif overdraft_limit > 0:
            print("No positive values for overdraft limit")
            exit()

        # Trys to run this code snippet
        try:
            self.__client.loc[len(self.__client)] = [first_name, last_name, title, account_number, date_of_birth,
                                                     occupation,
                                                     account_balance,
                                                     overdraft_limit]
        # If there is an error it will except it and print this message and close exit the method
        except:
            print("Something went wrong, please try again")
            exit()

        __accountHolder = Users(self.__client.loc[self.__client['Account Number'] == account_number])

        self.__client.to_csv("../data/client_data.csv", index=False)
        print("You just added the account:")
        print()
        print(f"{__accountHolder.__users}")

    def edit_first_name(self, account, new_name):

        __account = Users(self.__client.loc[self.__client['Account Number'] == account])
        print('*' * 107)
        print(f"{__account.__users}")
        print("*" * 107)
        # newName variable set as an input for the new name of the client

        # Updates the clients name
        self.__client.loc[(self.__client['Account Number'] == account), 'First name'] = new_name
        # Gets an updated list of the client
        __account.__users = (self.__client.loc[self.__client['Account Number'] == account])
        print("Updated Account:")
        print(f"{__account.__users}")
        self.__client.to_csv("../data/client_data.csv", index=False)

    def withdraw(self, account, withdraw):
        # While loop while condition is true
        while True:
            # Trys to find the account
            try:
                __account = Users(self.__client.loc[self.__client['Account Number'] == account])
                if __account.__users.empty:
                    raise Exception

                # Catches exception
            except:
                print("No account found, please try again")
                # Breaks out of while loop when this condition is met
                exit()
            else:
                # If account is found it will print it
                print("Old account balance")
                print(f"{__account.__users}")
                # Breaks out of while loop when condition is met
                break

        # Locates the row of the account number that matches input from user and edits balance from users input
        self.__client.loc[self.__client['Account Number'] == account, ['Account balance']] = self.__client['Account balance'] - withdraw
        # Adds £5 fee if the client goes over their overdraft limit
        self.__client.loc[self.__client['overdraft limit'] > self.__client['Account balance'], 'Account balance'] -= self.__fee
        self.__client.to_csv("../data/client_data.csv", index=False)

        updatedAccount = Users(self.__client.loc[self.__client['Account Number'] == account])

        print()
        print("Updated account balance: ")
        print(f"{updatedAccount.__users}")

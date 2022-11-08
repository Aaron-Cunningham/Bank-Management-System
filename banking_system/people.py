import pandas as pd


# Class definition
class Users():

    # constructor/initialiser
    def __init__(self, users):
        # Users properties
        self.__users = users
        # Fee that is changeable
        self.__fee = 5
        # List of clients in the bank
        self.__client = pd.read_csv("data/client_data.csv")

    def view_all(self):
        """
        This method searches for all the clients in the CSV file and then prints them out

        """
        # Prints all the clients from the bank
        print(f"{self.__client}")

    def search(self, account):
        if not isinstance(account, int):
            raise TypeError("Integer number only")
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
        self.__client.loc[self.__client['Account Number'] == account, ['Account balance']] = self.__client[
                                                                                                 'Account balance'] - withdraw
        # Adds £5 fee if the client goes over their overdraft limit

        self.__client.loc[
            self.__client['overdraft limit'] > self.__client['Account balance'], 'Account balance'] -= self.__fee

        self.__client.to_csv("data/client_data.csv", index=False)

        updatedAccount = Users(self.__client.loc[self.__client['Account Number'] == account])

        print()
        print("Updated account balance: ")
        print(f"{updatedAccount.__users}")

    def deposit(self, account, deposit):
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
                print()
                # Breaks out of while loop when condition is met
                break

        # Locates the row of the account number that matches input from user and edits balance from users input
        self.__client.loc[self.__client['Account Number'] == account, ['Account balance']] = self.__client[
                                                                                                 'Account balance'] + deposit

        updatedAccount = Users(self.__client.loc[self.__client['Account Number'] == account])
        self.__client.to_csv("data/client_data.csv", index=False)
        print()

        print("Updated account balance")

        print(updatedAccount.__users)

    def remove(self, account):

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
                print("Account: ")
                print(f"{__account.__users}")
                # Breaks out of while loop when condition is met
                break
        # Removes client from csv file
        self.__client.drop(self.__client[self.__client['Account Number'] == account].index, inplace=True)
        # writes to csv
        self.__client.to_csv("data/client_data.csv", index=False)
        print("Client Deleted")

    def negative_balance(self):

        account = (self.__client.loc[self.__client['Account balance'] < 0])

        if account.empty:
            print("No negative accounts")
            exit()

        print(f"{account}")

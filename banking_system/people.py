import pandas as pd


# Class definition
class Users:


    def __init__(self, first_name, last_name, date_of_birth):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__client = pd.read_csv("data/client_data.csv")
        self.__fee = 5


    @property
    def account_check(self):
        """This checks that an account exists before proceeding with methods"""
        try:
            self.get_account_details
            if self.get_account_details.empty:
                raise Exception
        except:
            print("*" * 35)
            print("No account found, please try again")
            print("*" * 35)
            exit()


    @property
    def get_account_details(self):
        """Gets the account of the clients account number"""

        return self.__client.loc[self.__client['First name'].str.contains(self.__first_name, case=False) & (
            self.__client['Last name'].str.contains(self.__last_name, case=False)) & (
                              self.__client['Date of birth'].str.contains(self.__date_of_birth, case=False))]

    def account_search(self):
        self.account_check
        print("*" * 117)
        print(self.get_account_details)
        print("*" * 117)

    def withdraw(self, withdraw):
        self.account_check
        print("Old account balance: ")
        print(self.get_account_details)

        # Locates the row of the account that matches input from user and edits balance from users input
        self.__client.loc[(self.__client['First name'] == self.__first_name) & (self.__client['Last name'] == self.__last_name) &
                          (self.__client ['Date of birth'] == self.__date_of_birth), ['Account balance']] = self.__client[
                                                                                                 'Account balance'] - withdraw
        # Adds £5 fee if the client goes over their overdraft limit
        self.__client.loc[
            self.__client['overdraft limit'] > self.__client['Account balance'], 'Account balance'] -= self.__fee

        print(self.get_account_details)

        self.__client.to_csv("data/client_data.csv", index=False)

    def deposit(self, deposit):
        self.account_check
        print("Old account balance: ")
        print(self.get_account_details)
        # Locates the row of the account that matches input from user and edits balance from users input
        self.__client.loc[
            (self.__client['First name'] == self.__first_name) & (self.__client['Last name'] == self.__last_name) &
            (self.__client['Date of birth'] == self.__date_of_birth), ['Account balance']] = self.__client[
                                                                                                 'Account balance'] + deposit
        print(self.get_account_details)

        self.__client.to_csv("data/client_data.csv", index=False)

    def remove_client(self):
        """Removes client from CSV file"""
        self.account_check
        print("*"*117)
        print(f"{self.get_account_details}")
        self.__client.drop(self.get_account_details.index, inplace=True)
        # Updates CSV file
        print()
        print("Has now been removed")
        print("*"*117)
        # Updates CSV file
        self.__client.to_csv("data/client_data.csv", index=False)


    def negative_balance(self):
        account = (self.__client.loc[self.__client['Account balance'] < 0])
        if account.empty:
            print("No negative accounts")
            exit()

        print(f"{account}")


class All_Clients:
    def __init__(self):
        self.__client = pd.read_csv("data/client_data.csv")

    def view_all(self):
        """
        This method searches for all the clients in the CSV file and then prints them out

        """
        # Prints all the clients from the bank
        print(f"{self.__client}")

    def view_negative(self):

        self.__client = (self.__client.loc[self.__client['Account balance'] < 0])

        if self.__client.empty:
            print("No negative accounts")
            exit()


        print(self.__client)


import pandas as pd


# Class definition
class Users:


    def __init__(self, first_name, last_name, date_of_birth):

        # Instance variables set as private
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
        # Trys to match an account with the details provided
        # Adapted from
        # https://www.plus2net.com/python/pandas-str-contains.php
        return self.__client.loc[self.__client['First name'].str.contains(self.__first_name, case=False) & (
            self.__client['Last name'].str.contains(self.__last_name, case=False)) & (
                              self.__client['Date of birth'].str.contains(self.__date_of_birth, case=False))]

    def account_search(self):
        """Searches for an account based on first name, last name and date of birth"""
        # Checks account exists
        self.account_check
        print("*" * 117)
        # Prints out account
        print(self.get_account_details)
        print("*" * 117)

    def withdraw(self, withdraw):
        """Method created to withdraw money from a clients account"""
        # Exception with type errors if wrong information is inputted on the object
        if not isinstance(withdraw, int):
            raise TypeError("Withdrawal amounts should be a integer")
        # If statement to only allow positive integers for withdrawals
        if withdraw < 0:
            print("Withdrawals are positive integers only")
            exit()
        # Checks account exists
        self.account_check
        print("Old account balance: ")
        # Prints out the old account balance
        print(self.get_account_details)

        # Locates the row of the account that matches input from user and edits balance from users input
        # Adapted from
        # https://stackoverflow.com/questions/57054946/how-to-match-multiple-columns-and-find-specific-column-value-in-pandas
        self.__client.loc[(self.__client['First name'] == self.__first_name) & (self.__client['Last name'] == self.__last_name) &
                          (self.__client['Date of birth'] == self.__date_of_birth), ['Account balance']] = self.__client[
                                                                                                 'Account balance'].subtract(withdraw)
        # Checks to see if client went over their overdraft limit and adds £5 if they did
        # Adapted from
        # https://www.geeksforgeeks.org/ways-to-apply-an-if-condition-in-pandas-dataframe/
        self.__client.loc[
            self.__client['overdraft limit'] > self.__client['Account balance'], 'Account balance'] -= self.__fee

        print()
        print("New account balance: ")
        # Prints new account balance
        print(self.get_account_details)
        # Updates CSV with new balance
        self.__client.to_csv("data/client_data.csv", index=False)

    def deposit(self, deposit):
        """This method deposits money into an account"""
        # Exception with type errors if wrong information is inputted on the object
        if not isinstance(deposit, int):
            raise TypeError("Deposit amount should be a integer")
        # If statement to only allow positive integers for deposits
        if deposit < 0:
            print("Deposits are positive integers only")
            exit()
        # Checks the account exists
        self.account_check
        print("Old account balance: ")
        # Prints out the old balance
        print(self.get_account_details)

        # Locates the row of the account that matches input from user and edits balance from users input
        # Adapted from
        # https://stackoverflow.com/questions/57054946/how-to-match-multiple-columns-and-find-specific-column-value-in-pandas
        self.__client.loc[
            (self.__client['First name'] == self.__first_name) & (self.__client['Last name'] == self.__last_name) &
            (self.__client['Date of birth'] == self.__date_of_birth), ['Account balance']] = self.__client[
                                                                                                          'Account balance'].add(deposit)
        print()
        print("New account balance: ")
        # Returns new account balance
        print(self.get_account_details)
        # Updates the CSV with the new information
        self.__client.to_csv("data/client_data.csv", index=False)

    def remove_client(self):
        """Removes client from CSV file"""
        # Check account exists
        self.account_check
        print("*"*117)
        # Prints out the account that's getting deleted
        print(f"{self.get_account_details}")
        # Removes the client from the CSV file
        self.__client.drop(self.get_account_details.index, inplace=True)
        print()
        print("Has now been removed")
        print("*"*117)
        # Updates CSV file
        self.__client.to_csv("data/client_data.csv", index=False)


class AllClients:
    def __init__(self):
        self.__client = pd.read_csv("data/client_data.csv")

    def view_all(self):
        """
        This method searches for all the clients in the CSV file and then prints them out

        """
        # Prints all the clients from the bank
        print(f"{self.__client}")

    def view_negative(self):
        """View all accounts with a negative balance"""
        try:
        # Sets self.__client = to accounts only with negative balance
            self.__client = self.__client.loc[self.__client['Account balance'] < 0]
        # If there are no negative accounts this if statement will run
            if self.__client.empty:
                raise Exception
        except:
            print("No accounts with negative balance")

        # Prints the accounts with negative balance
        print(self.__client)

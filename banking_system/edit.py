import pandas as pd


class Edit:
    """This class is used to edit clients details"""

    def __init__(self, account):
        # Instance variables set private
        self.__account = account
        self.__client = pd.read_csv("data/client_data.csv")

    @property
    def account_check(self):
        """This checks that an account exists before proceeding with methods to change details"""
        try:
            self.get_account
            if self.get_account.empty:
                raise Exception
        except:
            print("*" * 35)
            print("No account found, please try again")
            print("*" * 35)
            exit()

    @property
    def get_account(self):
        """Gets the account of the clients account number"""

        return self.__client.loc[self.__client['Account Number'] == self.__account]

    def set_first_name(self, new_name):
        self.account_check
        print("*" * 108)
        print("Old account details account details: \n"
              "\n", self.get_account)
        print()
        self.__client.loc[(self.__client['Account Number'] == self.__account), 'First name'] = new_name
        self.__client.to_csv("data/client_data.csv", index=False)
        print("New account details: \n"
              "\n", self.get_account)
        print("*" * 108)

    def set_last_name(self, new_name):
        self.account_check
        print("*" * 108)
        print("Old account details account details: \n"
              "\n", self.get_account)
        print()
        self.__client.loc[(self.__client['Account Number'] == self.__account), 'Last name'] = new_name
        self.__client.to_csv("data/client_data.csv", index=False)
        print("New account details: \n"
              "\n", self.get_account)
        print("*" * 108)

    def set_occupation(self, new_occupation):
        """Changes the occupation of an existing client"""
        self.account_check
        print("*" * 108)
        print("Old account details account details: \n"
              "\n", self.get_account)
        print()
        self.__client.loc[(self.__client['Account Number'] == self.__account), 'Occupation'] = new_occupation
        self.__client.to_csv("data/client_data.csv", index=False)
        print("New account details: \n"
              "\n", self.get_account)
        print("*" * 108)

    def negative(self):
        """This method only shows clients with a negative balance"""
        neg = self.__client < 0
        # If there are no clients with negative balance this print will run
        if neg.empty:
            print("No clients with negative balance")


class Add:

    def __init__(self, first_name, last_name, title, pronoun, account_number, date_of_birth, occupation, account_balance,
                 overdraft_limit):

        # Exceptions with type errors if wrong information is inputted on the object
        if not isinstance(first_name, str):
            raise TypeError("First name should be a string")
        if not isinstance(last_name, str):
            raise TypeError("Last name should be a string")
        if not isinstance(title, str):
            raise TypeError("Title should be a string")
        if not isinstance(pronoun, str):
            raise TypeError("Pronoun must be a string")
        if not isinstance(account_number, int):
            raise TypeError("Account number should be an integer")
        if not isinstance(date_of_birth, str):
            raise TypeError("Date of birth should be a string")
        if not isinstance(occupation, str):
            raise TypeError("Occupation should be a string")
        if not isinstance(account_balance, int):
            raise TypeError("Account balance should be an Integer")
        if not isinstance(overdraft_limit, int):
            raise TypeError("Overdraft limit should be an Negative Integer")
        # Properties for the new client
        self.__first_name = first_name
        self.__last_name = last_name
        self.__title = title
        self.__pronoun = pronoun
        self.__account_number = account_number
        self.__date_of_birth = date_of_birth
        self.__occupation = occupation
        self.__account_balance = account_balance
        self.__overdraft_limit = overdraft_limit
        self.__client = pd.read_csv("data/client_data.csv")

    def add_account(self):
        """Method to add users to the bank"""
        # Prevents the user from entering wrong values
        if self.__account_balance < 0:
            print("No negative integers for account balance")
            exit()
        elif self.__overdraft_limit > 0:
            print("No positive integers for overdraft limits")
            exit()

        # Uses the properties listed above to add the client to the CSV files.
        self.__client.loc[len(self.__client)] = [self.__first_name, self.__last_name, self.__title, self.__pronoun,
                                                 self.__account_number, self.__date_of_birth,
                                                 self.__occupation,
                                                 self.__account_balance,
                                                 self.__overdraft_limit]

        print("*" * 108)
        print("You just added the account:")
        # Prints out the new account holder
        print(
            f"{self.__first_name}   {self.__last_name}   {self.__title}    {self.__pronoun}    {self.__account_number}   {self.__date_of_birth}    {self.__occupation}     {self.__account_balance}    {self.__overdraft_limit}")
        print("*" * 108)

        self.__client.to_csv("data/client_data.csv", index=False)







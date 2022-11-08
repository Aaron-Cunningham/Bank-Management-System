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
        # Trys to find the account
        try:
            self.get_account
            # If the account doesn't exist it will raise an Exception
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
        # Only allows Strings for the new name or will raise TypeError
        if not isinstance(new_name, str):
            raise TypeError("First name should be a string")
        # Checks an account exists
        self.account_check
        print("*" * 108)
        # Returns old account details
        print("Old account details account details: \n"
              "\n", self.get_account)
        print()
        # Updates first name with the new_name
        self.__client.loc[(self.__client['Account Number'] == self.__account), 'First name'] = new_name
        # Updates the CSV file
        self.__client.to_csv("data/client_data.csv", index=False)
        # Prints out new account details
        print("New account details: \n"
              "\n", self.get_account)
        print("*" * 108)

    def set_last_name(self, new_name):
        """Updates the name of an existing client"""
        # Only allows Strings for the new name or will raise TypeError
        if not isinstance(new_name, str):
            raise TypeError("Last name should be a string")
        # Check account exists
        self.account_check
        print("*" * 108)
        # Prints out the old account details
        print("Old account details account details: \n"
              "\n", self.get_account)
        print()
        # Updates with the new name
        self.__client.loc[(self.__client['Account Number'] == self.__account), 'Last name'] = new_name
        # Writes to the CSV file
        self.__client.to_csv("data/client_data.csv", index=False)
        # Returns the new account details
        print("New account details: \n"
              "\n", self.get_account)
        print("*" * 108)

    def set_occupation(self, new_occupation):
        """Changes the occupation of an existing client"""
        # Will only accept new_occupation as a String otherwise will return a TypeError
        if not isinstance(new_occupation, str):
            raise TypeError("Occupation should be a string")
        # Checks account exists
        self.account_check
        print("*" * 108)
        # Prints account deatils
        print("Old account details account details: \n"
              "\n", self.get_account)
        print()
        # Updates occupation with new_occupation
        self.__client.loc[(self.__client['Account Number'] == self.__account), 'Occupation'] = new_occupation
        # Writes to CSV file
        self.__client.to_csv("data/client_data.csv", index=False)
        # Returns new account details
        print("New account details: \n"
              "\n", self.get_account)
        print("*" * 108)


class Add:

    def __init__(self, first_name, last_name, title, pronoun, account_number, date_of_birth, occupation, account_balance,
                 overdraft_limit):
        """
           This method allows a new client to be added to the CSV file.
           It takes First name, last name, title, pronoun, account number,
           date of birth, occupation, account balance, and overdraft limit.
        """

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
        # Instance variables set for the new client
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
        # Updates CSV file
        self.__client.to_csv("data/client_data.csv", index=False)







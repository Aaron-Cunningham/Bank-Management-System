import pandas as pd
import typer


app = typer.Typer()



# Class definition
class Users():


    # constructor/initialiser
    def __init__(self, users):
        # Users properties and attribute
        self.__users = users



    def view_all(self):
        """
        This method searches for all the clients in the CSV file and then prints them out

        """
        # Prints all the clients from the bank
        print(f"{clients.__users}")


    def search(self, account):

        """
        This method searches for an account using the account number, then it prints the account.
        """
        account = Users(people.loc[people['Account Number'] == account])

        print(f"{account.__users}")

    def search_by_name(self, firstName, lastName, dateOfBirth):
        """
        This method search the clients of the bank by name and date of birth.

        It is not case-sensitive.

        """

        __accountHolder = Users(people.loc[people['First name'].str.contains(firstName, case=False) & (
            people['Last name'].str.contains(lastName, case=False)) & (
                                               people['Date of birth'].str.contains(dateOfBirth))])

        print(f"{__accountHolder.__users}")

    def add_client(self, firstName, lastName, title, accountNumber, dateOfBirth, occupation, accountBalance,
                  overdraftLimit):
        """This method allows a client to be added to the bank.

        It takes the users first name, last name, title, account number, date of birth, occupation,
        account balance, and overdraft limit.

        String values are only allowed for the first name, last name, title, and occupation.
        """
        # Only allows first name to be a string
        if firstName.isalpha() == False:
            print("First name takes string values only")
            exit()
        # Only allows last name to be a string
        elif lastName.isalpha() == False:
            print("Last name takes string values only")
            exit()
        # Only allows title to be a string
        elif title.isalpha() == False:
            print("Title takes string values only")
            exit()
        # Only allows date of birth to be int/special char values
        elif dateOfBirth.isalpha() == True:
            print("Please fill out the date of birth in this order MM/DD/YYYY")
            exit()
        # Only allows for string values
        elif occupation.isalpha() == False:
            print("Occupation takes string values only")
            exit()
        # Only allows account balance to be positive
        elif accountBalance < 0:
            print("No negative balances for account balance")
            exit()
            # Only allows overdraft limit to be negative
            exit()
        elif overdraftLimit > 0:
            print("No positive values for overdraft limit")
            exit()

        # Trys to run this code snippet
        try:
            people.loc[len(people)] = [firstName, lastName, title, accountNumber, dateOfBirth, occupation,
                                       accountBalance,
                                       overdraftLimit]
        # If there is an error it will except it and print this message and close exit the method
        except:
            print("Something went wrong, please try again")
            exit()

        __accountHolder = Users(people.loc[people['Account Number'] == accountNumber])

        people.to_csv("../data/client_data.csv", index=False)
        print("You just added the account:")
        print()
        print(f"{__accountHolder.__users}")


    def edit_first_name(self, account, newName):

        __account = Users(people.loc[people['Account Number'] == account])
        print('*' * 107)
        print(f"{__account.__users}")
        print("*" * 107)
        # newName variable set as an input for the new name of the client

        # Updates the clients name
        people.loc[(people['Account Number'] == account), 'First name'] = newName
        # Gets an updated list of the client
        __account.__users = (people.loc[people['Account Number'] == account])
        print("Updated Account:")
        print(f"{__account.__users}")
        people.to_csv("../data/client_data.csv", index=False)

    def withdraw(self, account, withdraw, fee=5):
        __account = Users(people.loc[people['Account Number'] == account])

        print(f"{__account.__users}")

        # Locates the row of the account number that matches input from user and edits balance from users input
        people.loc[people['Account Number'] == account, ['Account balance']] = people['Account balance'] - withdraw
        # Adds £5 fee if the client goes over their overdraft limit
        people.loc[people['overdraft limit'] > people['Account balance'], 'Account balance'] -= fee
        people.to_csv("../data/client_data.csv", index=False)

        updatedAccount = Users(people.loc[people['Account Number'] == account])
        print(f"{updatedAccount.__users}")




# Create clients object
people = pd.read_csv("../data/client_data.csv")
clients = Users(pd.read_csv("../data/client_data.csv"))

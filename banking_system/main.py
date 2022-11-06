import sys
from menu import Menu
import pandas as pd
import edit as people
from people import Users


# Sets the column and row display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


menu = Menu()
s = Users(Users)

# Created person object
client = people.Edit(account=4999)

# Created a client to add object
clinet_to_add = people.Add("Tony", "Hawk", "mr", 5500, "05/12/1968", "Skate-border", 200, -200)





# Runs the UI interface
#Menu().run()
# Views all users
# s.view_all()

# Searches for account with the account number =  5000
#s.search(account=4999)

# Search for client based on name, and date of birth. This is not case-sensitive
# s.search_by_name(first_name="aaro", last_name="cunningham", date_of_birth="01/29/1999")

# Adds a client, this is case-sensitive and requires correct input
#s.add_client(first_name="Tony", last_name="Hawk", title="Mr", account_number="5540", date_of_birth="05/12/1968", occupation="Skateborder", account_balance=2, overdraft_limit=-200)

# Allows the user to withdraw money from an account, adds £5 fee for going over withdraw limit
#s.withdraw(account=5000, withdraw=500)

# Allows the user to deposit money into the account
# s.deposit(account=4999, deposit=500)

# Removes client from the list
# s.remove(account=5000)

# View accounts with negative balance
# s.negative_balance()

# Allows the user to edit a name of a client
#s.edit_first_name(account=4999, new_name="Aaron")

# Allows user to edit last name of a client
# s.edit_last_name(account=4999, new_name="Cunningham")

# Allows a user to edit a title of a client
# s.edit_title_name(account=4999, new_title="mr")


# Allows a user to edit the occupation of a user
# s.edit_occupation_name(account=4999, new_occupation="Job")



def remove():
    """This remove the client 5000 from the dataframe"""
    # 0 - Account Number
    s.remove(5000)

def edit_first_name():
    """Edits first name of client object"""

    # Client object name can be edited
    client.set_first_name("Aaron")
def edit_last_name():
    """Edits last name of client object"""
    # Client object last name can be edited
    client.set_last_name("Cunningham")
def edit_occupation():
    """Edits occupation of client object"""
    # Client object occupation can be edited
    client.set_occupation("Programmer")
def menu():
    """Runs the UI version of the program"""
    Menu().run()

def add_account():
    """Adds client to add object to the database"""
    clinet_to_add.add_account()



if __name__ == '__main__':

    globals()[sys.argv[1]]()



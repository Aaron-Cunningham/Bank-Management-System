import sys
from menu import Menu
import pandas as pd
import edit as clients
import people as people


# Sets the column and row display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


menu = Menu()

"""Created client to be edited object"""
client_to_be_edited = clients.Edit(account=1898)


"""Created a client to add object"""
# 0 - First name
# 1 - Last name
# 2 - Title
# 3 - Pronoun
# 4 - Account number
# 5 - Date of birth
# 6 - Occupation
# 7 - Account balance
# 8 - Overdraft limit
Jeff_Bazos = clients.Add("Jeff", "Bezos", "Mr", "Male", 5500, "01/12/1964", "CEO of Amazon", 6857489, -40000)
Elon_Musk = clients.Add("Elon", "Musk", "Mr", "Male", 5501, "01/28/1971", "Scientist", 44456743, -45000)

"""Known user and unknown object created"""
# 0 - First name
# 1 - Last name
# 2 - Date of birth
known_user = people.Users("Aaron", "Cunningham", "01/29/1999")
unknown_user = people.Users("Freddie", "Mercury", "09/05/1946")

"""User to delete object"""
# 0 - First name
# 1 - Last name
# 2 - Date of birth
user_to_delete = people.Users("Stephanus", "Illsley", "06/19/2002")

# Object created for all clients
All = people.AllClients()

def search():
    """Searches for object matching name and date of birth"""
    # Returns account that exits
    known_user.account_search()
    # Returns no account found
    unknown_user.account_search()

def withdraw():
    """Withdraws money from known user object account"""
    known_user.withdraw(withdraw=500)

def deposit():
    """Deposits money into known user object account"""
    known_user.deposit(deposit=500)


def view_all():
    """Allows you to see the full list of clients"""
    # Views all users
    All.view_all()


def remove():
    """This remove the client 5000 from the dataframe"""
    # 0 - Account Number
    user_to_delete.remove_client()

def edit_first_name():
    """Edits first name of client object"""

    # Client object name can be edited
    client_to_be_edited.set_first_name(new_first_name="Jason")
def edit_last_name():
    """Edits last name of client object"""
    # Client object last name can be edited
    client_to_be_edited.set_last_name(new_last_name="Berkley")
def edit_occupation():
    """Edits occupation of client object"""
    # Client object occupation can be edited
    client_to_be_edited.set_occupation(new_occupation="Data Engineer")
def menu():
    """Runs the UI version of the program"""
    Menu().run()

def add_account():
    """Adds client to add object to the database"""
    Jeff_Bazos.add_account()

def view_negative():
    """Returns all clients with a negative balance"""
    All.view_negative()


if __name__ == '__main__':

    globals()[sys.argv[1]]()




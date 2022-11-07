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
client = people.Edit(account=499)

# Created a client to add object
clinet_to_add = people.Add("Jeff", "Bezos", "Mr", 5500, "01/12/1964", "CEO of Amazon", 6857489, -40000)





# Runs the UI interface





def view_all():
    """Allows you to see the full list of clients"""
    # Views all users
    s.view_all()

def remove():
    """This remove the client 5000 from the dataframe"""
    # 0 - Account Number
    s.remove(5500)

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

def search():
    """This function is used to search for a client in the csv file"""
    # Search for client based on name, and date of birth. This is not case-sensitive
    s.search_by_name(first_name="aaron", last_name="cunningham", date_of_birth="01/29/1999")

def withdraw():
    """This function withdraws month from an account and
       adds a 5 pound charge when going over overdraft limit
    """
    # 0 - Account number
    # 1 - Amount to withdraw
    s.withdraw(account=4999, withdraw=500)

def view_negative():
    """This function allows you to see all users with negative balance"""
    s.negative_balance()

def deposit():
    """This function allows you to depost money into a users account"""
    # 0 - Account
    # 1 = Amount to deposit
    s.deposit(account=4999, deposit=500)

def search_by_name():
    """This function allows you to search for a user by their name"""
    # 0 - First name
    # 1 - Last name
    # 2 - Date of birth
    s.search_by_name(first_name="aaron", last_name="cunningham", date_of_birth="01/29/1999")

def search_by_account():
    """This function allows you to search for a client based on their account number"""
    # 0 - Account
    s.search(account=4999)

if __name__ == '__main__':

    globals()[sys.argv[1]]()



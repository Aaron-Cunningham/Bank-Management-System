import pandas as pd
import sys
from people import Users


# Sets the column and row display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Runs the UI interface
# Menu().run()
# Views all users
s = Users(Users)

# s.view_all()
# Searches for account with the account number =  5000
# s.search(account=5000)

# Search for client based on name, and date of birth. This is not case-sensitive
# s.search_by_name(firstName="aaron", lastName="cunningham", dateOfBirth="01/29/1999")

# Adds a client, this is case-sensitive and requires correct input
# s.add_client(firstName="Tony", lastName="Hawk", title="Mr", accountNumber="5540", dateOfBirth="05/12/1968", occupation="Skateborder", accountBalance=2, overdraftLimit=-200)

# Allows the user to edit a name of a client
# s.edit_first_name(account=4999, newName="Aaron")

# Allows the user to withdraw money from an account
# s.withdraw(account=5000, withdraw=500)





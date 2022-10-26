import pandas as pd
from pathlib import Path
from self import self
from menu_funtions import Functions
#
#

# Creates functions object to use functions from functions
functions = Functions()



class Menu:

    # Sets the column and row display options
    clients = Path(__file__).parent / "data/client_data.csv"
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    def menu(self):
        """Creates a menu system with the print function"""

        print("*" * 48)
        print()
        print("             Bank Management Console           ")
        print()
        print("*" * 48)
        default = 0
        print("Select 1 to view all clients\n"
              "Select 2 to remove account holders\n"
              "Select 3 to add a new account\n"
              "Select 4 to add money to an account\n"
              "Select 5 to withdraw money from an account\n"
              "Select 6 to edit a clients deatils\n"
              "Select 7 to search for a specific client\n"
              "Select 8 to exit the program"
              "\n"
              "************************************************")
        # Exception so only users can input ints
        try:
            option = int(input("Enter your choice: "))
        except:
            print("Enter int values only")
            Menu.menu(self)

        # Menu option buttons
        if option == 1:
            print(
                "********************************************************************************************************************************************\n"
                "                                                                 CLIENTS                                                                    \n"
                "********************************************************************************************************************************************")
            Functions.viewClients(self)
        elif option == 2:
            Functions.removeClient(self)
        elif option == 3:
            Functions.addClient(self)
        elif option == 4:
            Functions.depositMoney(self)
        elif option == 5:
            Functions.withdrawMoney(self)
        elif option == 7:
            Functions.accountSearch(self)
        elif option == 8:
            exit()
        elif option != default:
            print("Only input a number specified")
            Menu.menu(self)


from pathlib import Path
import pandas as pd
from datetime import datetime


class menu:
    clients = Path(__file__).parent / "data/client_data.csv"
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)

    def menu():
        print("************************************************")
        print()
        print("             Bank Management Console           ")
        print()
        print("************************************************\n"
              )

        print("Select 1 to view all clients\n"
              "Select 2 to remove account holders\n"
              "Select 3 to add a new account\n"
              "Select 4 to add money to an account\n"
              "Select 5 to remove money to an account\n"
              "Select 6 to edit a clients deatils\n"
              "\n"
              "************************************************")
        option = int(input("Enter your choice: "))
        if option == 1:
            print("********************************************************************************************************************************************\n"
                  "                                                                 CLIENTS                                                                    \n"
                  "********************************************************************************************************************************************")
            menu.viewClients()
        elif option == 2:
            menu.remove()

    def viewClients():
        clients = pd.read_csv("data/client_data.csv")
        print(clients)

    def remove():
        clients = pd.read_csv("data/client_data.csv")

        print(clients)

        AccountNumber = int(input("Enter the account number of the account you wish to delete"))
        clients.drop(clients[clients['Account Number'] == AccountNumber].index, inplace=True)
        clients.to_csv("data/client_data.csv")
        print(clients)
        print("Would you like to return to the menu?\n"
              "1: Yes\n"
              "2: Exit")
        option = int(input('Enter your option: '))
        if option == 1:
            menu.menu()
        elif option == 2:
            exit()


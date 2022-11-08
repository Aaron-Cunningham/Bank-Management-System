Banking application
===================
This is a terminal based banking application that uses the Pandas Data Analysis Library. 
This app has a vast amount of functionality such as been able to see all clients of 
the bank, deposit/withdraw money from a clients account, search for specific clients
in the bank, and add a client to the bank. This was created as part of my ***Programming 
portfolio 2*** assessment at Newcastle University. This projected used an OOP approach by 
creating objects and arguments to run in command line. A Menu UI has also been implemented for
better user experience.

Getting started with the banking app
====================================
Inorder to use this app you need to make sure you have the requirements installed from the
requirements folder. Furthermore, if needed, use pip commands `pip install pandas` and `pip install self`.

1) Download the file by clicking ***code*** and ***download zip***.
2) Make sure all the requirements are installed and a venv library is installed.
3) Use the terminal to input the arguments.
4) depending on which version of python your using write `python` for python version 2 or `python3`
for python3 in commands line arguments


Command line arguments
=========
To run the code you can use these command line arguments.

1) `python banking_system\main.py view_all` - This argument shows all the clients in the database.
2) `python banking_system\main.py remove` - This argument runs the remove method using an account number
which is in position 0. To change the account you wish to remove change the account number.
3) `python banking_system\main.py edit_first_name` - Edits the first name of the client object.
4) `python banking_system\main.py edit_last_name` - Edits the last name of the client object.
5) `python banking_system\main.py edit_occupation` - Edits the occupation of the client object.
6) `python banking_system\main.py menu` - Shows a menu UI within the terminal with functions included in the spec.
7) `python banking_system\main.py add_account` - Adds the account of client_to_add object.
8) `python banking_system\main.py search` - Searches for an account based on First name, Last name and date of birth.
9) `python banking_system\main.py withdraw` - Withdraws money from account with £5 charge added for going over overdraft.
10) `python banking_system\main.py deposit` - Deposits money into an account.
11) `python banking_system\main.py view_negative` - Views all the accounts with a negative balance.

Assumptions
===========
This will include all the assumptions I've made for my project.
1) When using search_by_name, I've made the assumption that it isn't ***Case sensitive***. So when inputting
the first name it can be either 'john' or 'John'.
2) When using withdraw, a £5 will be added to the account if they go over their overdraft limit.
3) For methods in the Edit class I've searched for account by account number to mix it up.
4) Within my edit.py I've implemented a method called account checker that checks if an account exits.
5) edit.py file has classes inside it that refers to editing a client, from first name, last name, occupation
and adding a client.
6) I've assumed that ***overdraft limits*** will be negative integers and ***account balance*** will be 
positive integers.
7) The Menu UI took a functional approach mostly.
8) My file got corrupted during my project, so I had to delete it and retrieve it from GitHub which might show why my commits are missing.

test commit
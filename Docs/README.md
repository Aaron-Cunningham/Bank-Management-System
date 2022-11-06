Banking application
=
This is a terminal based banking application that uses the Pandas Data Analysis Library. 
This app has a vast amount of functionality such as been able to see all clients of 
the bank, deposit/withdraw money from a clients account, search for specific clients
in the bank, and add a client to the bank. This was created as part of my ***Programming 
portfolio 2*** assessment at Newcastle University. This projected used an OOP approach by 
creating objects such as 'menu' and 'functions' in order to call functions and run functions
from other classes


`pip install pandas`



Getting started with the banking app
=
Inorder to use this app you need to make sure you have the requirements installed from the
requirements folder. Once this is done you can continue.

1) Open the file ```menu.py``` and press run in the top right corner and you will be presented
with a banking application in the terminal section 
2) To access a function in the menu system simply input the number of the function you want to
use and 
3) Carry on using the input feature when asked to do so to add or access more features


Breakdown of the functions
=

### Functions in menu_functions.py

```viewClients()```

This function allows the user to view all the clients in the CVS file.
The assumptions I made about this function include, the user having access
to all the information CSV file. Very simple but powerful function.

```removeClient()```

This function takes advantage of plenty of the exception handing tool 'try-except'.
The assumptions I made about this function is the account number added 
when prompt to input it needs to be a 1-to-1 match of the clients actual 
account number or the user will be issued with message saying account not found.
This function shows the account details of the client before deletion and 
checks if the user is sure they want to delete it. The deletion will be applied
with the pd.read_csv module.

```addClient()```

This function allows the user to add a client to the CSV file. It prompts the 
user to add a first name, last name, title, occupation, date of birth, account
balance, and overdraft limit. The account number is generated randomly with a value
inbetween 4000 and 4999. The assumptions I've made about this function is that
the date is inputted as a String, only a negative number can be inputted into the 
overdraft limit otherwise the while loop will continue to run. All the input
variables will be added to the CSV file with the pd.read.csv module.

```depositMoney()```

This function deposits money into an account on the CSV file. It does
this by asking the user for an account number of which they wish to deposit 
money into. If a wrong account number is inputted then the user will be
presented with a chance to re-enter the account number or return to the menu.
The account number is matched up with one on the CSV file, it then shows the
user the account file (which include the balance) before the deposit. After this,
it will ask for the user input for the deposit amount. Only positive integers can
be deposited otherwise the user will be prompted to add a positive integer.
After, the deposit input variable will be applied to the account which was 
inputted at the beginning. I've assumed the user knows account numbers and 
knows what a positive integer is.

```withdrawMoney()```

Similar to the deposit money function this one does the opposite with some
added functionalities. It has a fee variable set at 5, this is used to add a fee
to the bank account once it's over the limit of their overdraft. I chose to use
a variable for this so the fee can be easily changed. The account the user
wants to withdraw money from is found using a user input that searches for 
an account using the account number that matches it. Like the previous functions,
if the account number is wrong there is exception handing, and a while loop
in place for the user to re-search for the account or return to the menu 
if the search returns an empty data frame. Once the correct account number
is inputted, the account file will show with the current balance. After this,
the program will prompt the user to input a withdrawal amount which can only be
a positive integer otherwise you will be stuck in a while loop(The program
gives the user a hint to input a positive int). Following on, once a withdrawal 
amount is inputted the program will withdraw it from the account and check
the account hasn't gone over their withdrawal limit. If the account has gone over 
its withdrawal limit a £5 fee will be added. Once this check is done the data
will be updated with the pd.read_csv module and an updated account file will
be shown. I've assumed that the user knows the account number of the account they
want to access, I've assumed the £5 fee will be added after the overdraft limit
has been breached.

```accountSearch()```

This function searches for specific clients by first name, last name, and date 
of birth. I've assumed that first names and last names are ***case-insensitive***.
It starts off by asking the user to input the details specified above. 
The CSV file will then be searched with data that matches these inputs. 
If an account can't be found the details are incorrect and will tell the 
user that no account was found and will ask them to try again or return to the 
menu. If an account is found it will bring up the accounts details. Once the 
user has looked at the data they will be prompted to either exit the program or
return-back to the menu.

```returnToMenu()```

This function was created to create less lines in other functions which make it 
easier to read. It gives a message to the user to either return back to the 
menu or exit the program. The user can input which option they would like to do.
It has exception handing inside if users enter the wrong input.

### Breakdown of the functions in menu.py

```menu()```

This function was created to be the 'home screen' of my banking application.
This function allows the user to access all the other functions created 
with a user input. I used a variable ```option``` where the user option
will be saved and executed whichever option they choose. 
Banking application
===================
This is a terminal based banking application that uses the Pandas Data Analysis Library.
This application required me to research pandas and how to edit data within the CSV file.
I did this by using various reliable sources such as Geeksforgeeks and Stackoverflow
This app has a vast amount of functionality such as been able to see all clients of 
the bank, deposit/withdraw money from a clients account, search for specific clients
in the bank, and add a client to the bank. This was created as part of my ***Programming 
portfolio 2*** assessment at Newcastle University. This projected used an OOP approach by 
creating objects and arguments to run in command line. A Menu UI has also been implemented for
better user experience.

Getting started with the banking app
====================================
Inorder to use this app you need to make sure you have the requirements installed from the
requirements folder. Furthermore, if needed, use pip commands:
````
pip install pandas
pip install self
pip install datatest
pip install pytest
```` 


1) Download the file by clicking ***code*** and ***download zip***.
2) Make sure all the requirements are installed.
3) Use the terminal to input the arguments in the command line arguments section.
4) depending on which version of python you're using, write `python` for python version 2 or `python3`
for python version 3 at the beginning of the command line arguments.

Note: You can change the values in the methods to whatever values you desire for example:
````

````

I've commented in the code which information goes in which 
position within the main above the desired method.


Testing banking application
==========================
To document my tests I used a Word document that was then converted into a PDF, this can be found in the testing folder. Furthermore, I used datatest and pytest. 
Testing was relatively easy for this application. Some of the tests that I carried out, turned out to be very useful which led me to fix the problem.
For example, the view_negative method had a bug that resulted in all my data in the CSV file changing to just clients with negative balances. 
This bug was quickly rectified, and the test was re-run and updated in the testing Word document. Other tests I carried out included checking for
TypeErrors, checking methods ran as expected, and results were updated in the CSV file. Without testing, I would've never of noticed the big within
the view_negative balance with would've resulted in loosing all clients with a positive balance within the bank. To run test suite use:
````
python -m pytest
````

Objects
=======
Within my main I have created some objects so the user of this application can run it without any input.
The add client data includes `Jeff_Bazos` and `Elon_Musk`, these are used in the add account method, 
the default client is `Jeff_Bazos`. I've also created objects called `known_user` and `unknown_user`. 
These were added to use the search method, deposit method, and withdraw method. Furthermore, I've 
created an object called `client_to_be_edited` this object is used for the methods that includes editing
a clients details such as first name, last name, and occupation. `user_to_delete` was an object created
for the remove method. Lastly, `All` is an object created to user the view all and view negative methods.


Command line arguments
==================================
To run the code you can use these command line arguments.
1) `python banking_system/main.py view_all` - This argument shows all the clients in the database.
2) `python banking_system/main.py remove` - This argument runs the remove method using an account number
which is in position 0. To change the account you wish to remove change the account number.
3) `python banking_system/main.py edit_first_name` - Edits the first name of the client object.
4) `python banking_system/main.py edit_last_name` - Edits the last name of the client object.
5) `python banking_system/main.py edit_occupation` - Edits the occupation of the client object.
6) `python banking_system/main.py menu` - Shows a menu UI within the terminal with functions included in the spec.
7) `python banking_system/main.py add_elon_musk` - Adds the account Elon_musk to the CSV.
8) `python banking_system/main.py add_jeff_bazos` - Adds the account Jeff_Bazos to the CSV.
9) `python banking_system/main.py add_cristiano_ronaldo` - Adds the account Cristiano_Ronaldo to the CSV.
8) `python banking_system/main.py search` - Searches for an account based on First name, Last name and date of birth.
9) `python banking_system/main.py withdraw` - Withdraws money from account with £5 charge added for going over overdraft.
10) `python banking_system/main.py deposit` - Deposits money into an account.
11) `python banking_system/main.py view_negative` - Views all the accounts with a negative balance.
12) `python banking_system/main.py search_unknown` - Returns no account found.

Assumptions
===========
This will include all the assumptions I've made for my project.
1) When using search, I've made the assumption that it isn't ***Case sensitive***. So when inputting
the first name it can be either 'john' or 'John'.
2) When using withdraw, a £5 will be added to the account if they go ***over*** their overdraft limit.
3) For methods in the Edit class I've searched for an account by account number to mix it up.
4) Within my edit.py I've implemented a method called account checker that checks if an account exits.
5) edit.py file has classes inside it that refers to editing a client, from first name, last name, occupation
and adding a client.
6) I've assumed that ***overdraft limits*** will be negative integers and ***account balance*** will be 
positive integers.
7) The Menu UI took a functional approach mostly.
8) Withdrawal and deposits are positive integers only (A check is inplace).
9) I haven't used the user input function in my methods as I assumed as part of the spec was to create the backend of the bank 
management system which demonstrates good use of OOP. However, there is user input in the Menu UI.
10) Date of birth is stored as a String value instead of using the date and time.
11) Account numbers will be stored as positive integers.


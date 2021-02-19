# Test-Password-Locker

### Author
Irene Wairimu Mungai


## SetUp Dependencies
> Install these first:
* Python3.8
* pip
* pyperclip

## User stories
The user would like to.... :

1. To create an account for the application or log into the application.
1. Store my existing acounts login details for various accounts that i have registered for.
1. Generate new password for an account that i haven't registered for and store it with the account name.
1. Delete stored account login details that i do now want anymore.
1. Copy my credentials to the clipboard


## Technologies used
* Python3.8


| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Use the short codes Dispoyed | **In your  terminal: $./run.py** | Welcome to password locker  choose an option: ca-Create  an account, log-Log In, ex-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your user_name, and  a password |
| Display prompt for login in | **Enter: log** | Enter your user_name and password |
| Display codes for credentials | **Login Successful** | Choose an option: cc - Create Credential, 
del-Delete Credentials ,dc - Display Credentials, fc - Find Credential copy  ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the user_name, account and password |
|Display prompt for deleting  a credential| **Enter: del** |Enter the account deletes credentials of that account|
| Display a list of credentials | **Enter: dc** | Prints a list of  the user's saved credentials |
| Display prompt for finding a  credential | **Enter: fc** | Enter the account of the credential you wish to copy. |
| Exit the  application | **Enter: ex** | Exit navigation |


## Cloning
* In your terminal:
        
        $ git clone https://github.com/nimowairimu/Test-Password-Locker.git``
        $ cd Test_Pass
>1. ` git clone git remote add origin https://github.com/nimowairimu/Test-Password-Locker.git`
>2. ``cd Test_Pass`
>3. To run the app enter  the following commands in terminal `` python3.8 .py ` or `./run.py`


## Running the Application
* To run the application, in your terminal:

        $ chmod +x run.py
        $ ./run.py
        

## License
> MIT License 2021 Wairimu Mungai



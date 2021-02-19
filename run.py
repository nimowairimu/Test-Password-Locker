#!/usr/bin/env python3.6
from credentials import User, Credential

def create_user(user_name,password):
    '''
    Function to create a new contact
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save contact
    '''
    user.save_user()

def login_user(user_name,password):
    """
    function that checks whether a user exist and then login the user in.
    """
  
    check_user = Credential.verify_user(user_name,password)
    return check_user

def generate_password():
	'''
	Function to generate a password for a user
	'''
	generate_password = Credential.generate_password()
	return generate_password

def create_credential(user_name,account,password):
	'''
	Function to create a new credential
	'''
	new_credential = Credential(user_name,account,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a new  created  user credential
	'''
	Credential.save_credential(credential)

def delete_credentials(credential):
    '''
    function to delete a credential
    '''
    credential.delete_credentials()

def find_credential(account):
    '''
    Function that finds a credential by account and returns the credential
    '''
    return Credential.find_by_account(account)

def check_existing_credentials(account):
    '''
    Function that check if a credential exists with that accoun and return a Boolean
    '''
    return Credential.credential_exist(account)



def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)

def copy_credential(password):
	'''
	Function to copy a credentials details to the clipboard using pyperclip
	'''
	return Credential.copy_credential(password)

def main():
    print('*'*20)
    print("Having trouble remembering all your account log in details \n Don't worry  Password Locker got you!")
    print ('*'*20)
    while True:
        print("Use these short codes to continue : \n ca - create account \n log -to log in \n ex - To exit ")
        short_code = input()
        if short_code == "ex":
            break
        elif short_code == "ca":
            print("Create account")
            print("-"*20)
            user_name = input('Enter a username: ')
            password = input ('Enter a password:   ')
            save_user(create_user(user_name,password))
            print('*'*5)
            print(f"A new account has been successfuly created under username :{user_name} with password set as{password}")
            print('PLease go ahead and log in ')
            print('*'*20)
        elif short_code == "log":
            print('Enter your details to log in ')
            user_name = input('Enter your user_name:  ')
            password = input ('Enter your password:    ')
            user_exists = login_user(user_name,password)
            print ('*'* 5)
            print (f"Welcome back  {user_name}!,Choose an option to continue")
            while True:
                print ('*'*20)
                print("Choose an option")
                print(" Use these short codes : \n cc - create a new credential \n del - delete credential \n dc -display credential \n fc- find a credential \n ex - exit the credentials list")
                short_code = input('')
                if short_code == "cc":
                    print(" Add New credentials")
                    print("-"* 10)

                    print("User_name .....")
                    user_name = input('')

                    print("Account ....")
                    account = input('')

                    print("Password .....")
                    option = input("Do you want us to generate a password for you? y/n")
                    if option.lower() == "y":
                        password = generate_password()
                    else:
                        password = input()

                    save_credential(create_credential(user_name,account ,password))
                    print ('\n')
                    print(f"New Credential {user_name} {account} created")
                    print ('*'*20)

                elif short_code == 'dc':
                    if display_credentials(user_name):
                        print("Here is a list of all your credentials")
                        print('\n')
                        for credential in display_credentials(user_name):
                            print(f" user_name:{credential.user_name} account: {credential.account} password:.{credential.password}")
                            print('\n')
                    else :
                        print ("Sorry you don't seem to have any credentials saved yet")
                        print('*'*20)
                        break

                elif short_code == 'fc':
                    print('*'*20)
                    print("Enter the  you account  want to search for  ")
                    search_account = input()
                    if check_existing_credentials(search_account):
                        search_credential = find_credential(search_account)
                        print(f"{search_credential.username_name} {search_credential.password}")
                        print('*' * 20)
                        print('\n')
                        option = input  ('Would you like to copy your credentials?  y/n')
                        if option.lower() == "y":
                            search_credential.copy_credential()
                            print('Credential copied to clipboard')
                        else:
                            break 
                    else:
                        print("We cannot find your credentials ")
                        print('*'*20)
                        break

                elif short_code == "del":
                    print("Enter the account you would like to delete ")
                    choice = input()
                    search_account = find_credential(choice)
                    search_account.delete_credentials

                elif short_code == "exit":
                    print("Bye ....")
                    print("*"*30)
                    break
                else:
                    print("Sorry i didn't quite get that,please choose an valid option")

if __name__ == '__main__':
    main()

        




                



        

    








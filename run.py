#!/usr/bin/env python3.6
from credentials import User, Credential

def create_user(user_name,password):
    '''
    Function to create a new contact
    '''
    new_user = Credential(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save contact
    '''
    user.save_user()

def authenticate_user(user_name,password):
    '''
    Function that check if user log in details are correct 
    '''
    authenticate_user = Credential.check_user(user_name,password)
    return authenticate_user

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

def delete_credential(credential):
    '''
    function to delete a credential
    '''
    credential.delete_credential()

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
        print("Use these short codes to continue : ca - create account log -to log in ,ex - To exit ")

        
        short_code = input().lower()

        if short_code == exit:
            break

        elif short_code == "ca":
            print("Create account")
            print("-"*20)
            user_name = input('Enter a username: ')
            password = input ('Enter a password:   ')
            save_user(create_user(user_name,password))
            print('\n')
            print(f"A new account has been successfuly created under username :{user_name} with password set as{password}")
            print('PLease go ahead and log in ')

        elif short_code == "log":
            print('Enter your details to log in ')
            user_name = input('Enter your user_name:  ')
            password = input ('Enter your password:    ')
            returning_exists = authenticate_user(user_name,password)
            if returning_exists == user_name:
                print (f"Welcome back {user_name}!,Choose an option to continue")
        else:
            print("PLease enter a valid option")

               while True:
                   print("Choose an option")
                   print(" Use these short codes : cc - create a new credential,del - delete credential , dc -display credential ,fc- find a credential ,ex - exit the credentials list")

                   if short_code == "cc":
                       print("New credential")
                       print("-"* 10)

                       print("User_name .....")
                       User_name = input()

                       print("Account ....")
                       account = input()

                       print("Password .....")
                       password = input()

                       save_credential(create_credential(user_name,password))
                       print ('\n')
                       print(f"New Credential {user_name} {account} created")
                       print ('\n')
        
                     elif short_code == 'dc':

                         if display_credentials():
                         print("Here is a list of all your credentials")
                         print('\n')

                         for credential in display_credentials():
                         print(f"{credential.user_name} {credential.account} .....{credential.password}")
                         print('\n')
                         else :
                             print ("Sorry you don't seem to have any credentials saved yet")
                             print('\n')

                     elif short_code == 'fc':
                          print("Enter the  you account  want to search for  ")
                          search_account = input()
                          if check_existing_credential(search_account):
                search_credential = find_credential(search_account)
                print(f"{search_credential.username_name} {search_credential.password}")
                print('-' * 20)
                print('\n')
                option = input  ('Would you like to copy your credentials?  y/n')
                if option.lower() == "y":
                    search_credential.copy_credential()
                    print('Credential copied to clipboard')
                else:
                    break 
        elif short_code == "del":
            print("Enter the account you would like to delete ")
            delete = input()
            delete.delete_credentials()
        elif short_code == "exit":
            print("Bye ....")
            break
        else:
            print("Sorry i didn't quite get that,please choose an valid option")

if __name__ == '__main__':

    main()

        




                



        

    








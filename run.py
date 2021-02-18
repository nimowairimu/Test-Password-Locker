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
    print("Having trouble remembering all your account log in details \n Don't worry  Password Locker got you!")
    print ("Enter a username ")

    user_name = input()
    print(f"Hey {user_name}.What would you like to do ?")
    print ('\n')

    while True:
        print("Use these short codes :ca - create account ,log - to log in ,cc - create a new credential, dc -display credential ,fc- find a credential ,ex - exit the credentials list")
        
        short_code = input().lower()

        if short_code == "ca"
        print("Create account")
        print("-"*20)
        user_name = input('Enter a username: ').strip()
        password = input ('Enter a password:   ').strip()
        save_user(create_user(user_name,password))
        print('\n')
        print{f'A new account has been successfuly created under username :{user_name} with passwors set as: {password}'}
        print{'PLease go ahead and log in '}

        elif short_code == "log"
        print{'Enter your details to log in '}
        user_name = input('Enter your user_name :  ')
        password = input ('Enter your password:    ')


        elif short_code == "cc"
        print("New credential")
        print("-"* 10)

        print("User_name .....")
        User_name = input()

        print("Account ....")
        account = input()

        print("Password .....")
        password = input()

        save_credential()




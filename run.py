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
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

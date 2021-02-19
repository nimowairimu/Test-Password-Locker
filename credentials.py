import pyperclip

class User:
    """
    Class that generates new instances of a user
    """
    
    users_list = []
    pass

    def __init__(self,user_name,password):
         '''
         __init__ method that helps us define properties for our objects.
         '''
         self.user_name = user_name
         self.password = password

    def save_user(self):
        '''
        save_user method saves contact objects into contact_list
        '''

        User.users_list.append(self)


class Credential:
    '''
    Class that generates new instance of user credentials 
    '''
    credentials_list = []
    @classmethod
    def verify_user(cls,user_name, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.users_list:
            if(user.user_name == user_name and user.password == password):
                    a_user == user.user_name
        return a_user

    def __init__(self,user_name,account,password):
        '''
        __init__ method that helps us define properties for our user credentials 
        '''
        self.user_name = user_name
        self.account = account
        self.password = password
    
    def save_credential(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credential.credentials_list.append(self)

    def delete_credentials(self):

        '''
        delete_credential method deletes a saved credentials from the list
        '''

        Credential.credentials_list.remove(self)
    
    @classmethod
    def find_by_account(cls,account):
        '''
        Method that takes in a user account and returns a account password that matches that account.
        '''

        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    
    @classmethod
    def credential_exist(cls,account):
        '''
        Method that checks if a credential exists from the list.
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                    return True

        return False

    @classmethod
    def display_credentials(cls,user_name):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list
    
    @classmethod
    def copy_password(cls,account):
        credential_found = Credential.find_by_account(account)
        pyperclip.copy(credential_found.password)

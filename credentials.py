
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
    def __init__(self,user_name,account,password):
        '''
        __init__ method that helps us define properties for our user credentials 
        '''
        self.user_name = user_name
        self.account = account
        self.password = password
    
    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentails_list.append(self)


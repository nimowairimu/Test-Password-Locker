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
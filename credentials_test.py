import unittest # Importing the unittest module
from credentials  import User


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("James","Muriuki") 


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"James")
        self.assertEqual(self.new_user.password,"Muriuki")
        
    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
        the contact list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.users_list),1)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.users_list = [] 

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users
        objects to our user_list
        '''
        self.new_user.save_user()
        Lucy = User("lucywamessi","kadesho65") # new user
        Lucy.save_user()
        self.assertEqual(len(User.users_list),2)

if __name__ ==  '__main__':
    unittest.main()

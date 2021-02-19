import unittest # Importing the unittest module
from credentials  import User,Credential
import pyperclip


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('nims','52522')
		self.new_user.save_user()
		New_user = User('lucy','45456')
		New_user.save_user()

		for user in User.users_list:
			if user.user_name == New_user.user_name and user.password == New_user.password:
				other_user = user.user_name
		return other_user

		self.assertEqual(other_user,Credential.check_user(New_user.password,New_user.user_name))

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
        test_save_contact test case to test if the user object is saved into
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

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        set up method to run before each test case 
        '''
        self.new_credential = Credential("nimowairimu","Instagram","nims")

    

    def test_init(self):
        '''
        test case to test if the object is initialized correctly
        '''
        self.assertEqual(self.new_credential.user_name,"nimowairimu")
        self.assertEqual(self.new_credential.account,"Instagram")
        self.assertEqual(self.new_credential.password,"nims")


    def test_save_credential(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
        the credentials list
        '''
        self.new_credential.save_credential() 
        self.assertEqual(len(Credential.credentials_list),1)
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credentials_list = []
    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credentials to check if we can save multiple
            in our  credentials_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","Snapchat","1234") 
            test_credential.save_credential()
            self.assertEqual(len(Credential.credentials_list),2)

    
    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credential from our  list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","Twitter","1234") 
            test_credential.save_credential()

            self.new_credential.delete_credentials()
            self.assertEqual(len(Credential.credentials_list),1)

    def test_find_contact_by_account(self):
        '''
        test to check if we can find a credential by account
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","Facebook","2525") 
        test_credential.save_credential()

        found_credential = Credential.find_by_account("Facebook")

        self.assertEqual(found_credential.password,test_credential.password)
    
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","Gmail","M5252")
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Gmail")

        self.assertTrue(credential_exists)
    
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credentials_list)
    
    def test_copy_password(self):
        '''
        Test to confirm that we are copying the password address from a found credential
        '''

        self.new_credential.save_credential()
        Credential.copy_password("Instagram")

        self.assertEqual(self.new_credential.password,pyperclip.paste())



     


if __name__ ==  '__main__':
    unittest.main()
 
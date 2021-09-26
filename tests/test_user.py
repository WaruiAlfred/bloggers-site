import unittest 
from app.models import User 

class UserModelTest(unittest.TestCase): 
  
  def setUp(self):
    '''
    method that creates an instance of User class password
    '''
    self.new_user = User(password = 'jumanji')
    
  def test_password_setter(self): 
    '''
    this ascertains that when password is being hashed and the pass_secure contains a value
    '''
    self.assertTrue(self.new_user.user_password is not None)
    
  def test_no_access_password(self): 
    '''
    taste case confirms that an attribute error is raised when the password value is being accessed
    '''
    with self.assertRaises(AttributeError): 
      self.new_user.password
    
  def test_password_verification(self): 
    '''
    test confirms that  password_hash can be verified when a correct password is passed in
    '''
    self.assertTrue(self.new_user.verify_password('jumanji'))
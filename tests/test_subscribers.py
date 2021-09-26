import unittest
from app.models import Subscribers 
from app import db

class SubscribersTest(unittest.TestCase): 
  """
  Test class to test subscribers model behaviour
  """
  def setUp(self):
    '''Test function to run before every test'''
    self.update_subscriber = Subscribers(email="abc@gmail.com")
    
  def tearDown(self):
    '''Function to clear instance after every test'''
    Subscribers.query.delete()
  
  def test_instance(self):
    '''Function to confirm that the created object exists in the class''' 
    self.assertTrue(isinstance(self.update_subscriber,Subscribers))
    
  def test_init(self):
    '''Function that ensures proper instances of class objects'''
    self.assertEquals(self.update_subscriber.email,"abc@gmail.com")
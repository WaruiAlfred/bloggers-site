import unittest
from app.models import Quotes 

class QuotesTest(unittest.TestCase): 
  """
  class to test Quotes model behaviour
  """
  def setUp(self):
    '''Test function to run before every test'''
    self.new_quote = Quotes("Albert Einstein","Imagination is more important than knowledge")
    
  def test_init(self): 
    '''Test function to assert that class objects are instantiated properly'''
    self.assertEqual(self.new_quote.author,"Albert Einstein")
    self.assertEqual(self.new_quote.quote,"Imagination is more important than knowledge")
import unittest 
from app.models import Blogs
 
class BlogsTest(unittest.TestCase): 
  '''
  Test class to test the behaviour of the Blogs class
  '''
  
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_blog = Blogs(title="Travel Guide",blog="For safe travels make sure to plan ahead.",user_id = 1 )
  
  def test_instance(self): 
    '''Function that confirms that the instance object exists in the model class'''
    self.assertTrue(isinstance(self.new_blog,Blogs))
    
  def test_check_instance_variables(self):
    '''Function to confirm that the class object is instantiated properly'''
    self.assertEquals(self.new_blog.title,"Travel Guide")
    self.assertEquals(self.new_blog.blog,"For safe travels make sure to plan ahead.")
    self.assertEquals(self.new_blog.user_id,1)
    
  def test_save_blog(self):
    '''Function to confirm proper saving'''
    self.new_blog.save_blog()
    self.assertTrue(len(Blogs.query.all())>0)
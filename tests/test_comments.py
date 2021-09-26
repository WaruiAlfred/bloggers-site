import unittest 
from app.models import Comments
 
class CommentsTest(unittest.TestCase): 
  '''
  Test class to test the behaviour of the Comments class
  '''
  
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_comment = Comments(comment="That's great work man!!",user_id = 1,blog_id=1 )
  
  def test_instance(self): 
    '''Function that confirms that the instance object exists in the model class'''
    self.assertTrue(isinstance(self.new_comment,Comments))
    
  def test_check_instance_variables(self):
    '''Function to confirm that the class object is instantiated properly'''
    self.assertEquals(self.new_comment.comment,"That's great work man!!")
    self.assertEquals(self.new_comment.user_id,1)
    self.assertEquals(self.new_comment.blog_id,1)
    
  def test_save_comment(self):
    '''Function to confirm proper saving'''
    self.new_comment.save_comment()
    self.assertTrue(len(Comments.query.all())>0)
    
  def test_get_comment(self):
    '''Function to confirm that a comment is retrieved for a particular blog'''
    found_comment=self.new_comment.get_comments(1)
    self.assertTrue(found_comment is not None)
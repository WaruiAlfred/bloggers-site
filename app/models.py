from sqlalchemy.orm import backref
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id): 
  return User.query.get(int(user_id))

# User model
class User(UserMixin,db.Model): 
  __tablename__ = 'users' 
  
  id = db.Column(db.Integer,primary_key = True)
  username = db.Column(db.String(255),unique = True)
  user_email = db.Column(db.String(255),unique = True,index = True)
  biodata = db.Column(db.String)
  profile_pic_path = db.Column(db.String)
  user_password = db.Column(db.String(255))
  
  blogs = db.relationship('Blogs',backref = 'user', lazy = "dynamic")
  comments = db.relationship('Comments',backref = 'user', lazy = "dynamic")
  
  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self,password): #Generating a hashed password
    self.user_password = generate_password_hash(password)
    
  def verify_password(self,password):#verify password while logging in
    return check_password_hash(self.user_password,password)
  
  def __repr__(self): 
    return f'User {self.username}'
  
# Pitches model
class Blogs(db.Model): 
  __tablename__ = 'blogs' 
  
  id = db.Column(db.Integer,primary_key = True)
  title = db.Column(db.String(50))
  blog = db.Column(db.String) 
  submitted = db.Column(db.DateTime,default=datetime.utcnow)
  
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  comments = db.relationship('Comments', backref = 'blog', lazy = "dynamic")
  upvote = db.relationship('Upvote', backref='blog', lazy='dynamic')
  downvote = db.relationship('Downvote', backref='blog', lazy='dynamic')
    
  def save_blog(self):
    '''Method to save  blogs'''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_blogs(self):
    '''Method to retrieve blogs'''
    blogs = Blogs.query.all()
    return blogs
  
  def __repr__(self): 
    return f'Blog {self.id} > {self.blog}'
  
# Comments model
class Comments(db.Model): 
  __tablename__ = 'comments' 
  
  id = db.Column(db.Integer,primary_key = True)
  comment = db.Column(db.String)
  submitted = db.Column(db.DateTime,default=datetime.utcnow)
  
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
  
  def save_comment(self):
    '''Method to save  submitted comments'''
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    '''Method to retrieve comments '''
    comments_by_id = Comments.query.filter_by(blog_id = id).all()
    return comments_by_id
  
  def __repr__(self): 
    return f'Comment {self.blog_id} > {self.comment}'
  
#votes
  
class Upvote(db.Model):
  __tablename__ = 'upvotes'

  id = db.Column(db.Integer, primary_key=True)
  blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'),nullable = False)

  def save(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_upvotes(cls,id):
    upvote = Upvote.query.filter_by(blog_id=id).all()

    return upvote

  def __repr__(self):
    return f'Blog id:{self.blog_id}'

class Downvote(db.Model):
  __tablename__ = 'downvotes'

  id = db.Column(db.Integer, primary_key=True)
  blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'),nullable = False)

  def save(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_downvotes(cls,id):
    downvote = Downvote.query.filter_by(blog_id=id).all()

    return downvote

  def __repr__(self):
    return f'Blog id:{self.blog_id}'
  
class Quotes: 
  '''Class to display random quotes'''
  def __init__(self,author,quote):
    self.author = author
    self.quote = quote
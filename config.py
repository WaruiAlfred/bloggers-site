from pathlib import Path
from dotenv import load_dotenv
import os

#Dotenv Configuration
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

class Config: 
  '''
  General configuration class
  '''
  SECRET_KEY = os.getenv("SECRET_KEY") #secret key for wtf forms
  UPLOADED_PHOTOS_DEST = 'app/static/photos' #storage location of uploaded photos in the app
  
#  app email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.getenv("MAIL_USERNAME")
  MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

class ProdConfig(Config): 
  '''
  Test configuration child class
  '''
  SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

class TestConfig(Config): 
  '''
  Production configuration child class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://toshiba:@localhost/blogs_test'

class DevConfig(Config): 
  '''
  Development configuration child class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://toshiba:@localhost/blogs'
  DEBUG = True
  
config_options = {
  'development':DevConfig,
  'production': ProdConfig,
  'test':TestConfig
}
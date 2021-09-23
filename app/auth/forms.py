from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo,Length
from ..models import User
from wtforms import ValidationError

#Registration form
class RegistrationForm(FlaskForm): 
  email = StringField('Enter your email address',validators=[Required(),Email()])
  username = StringField('Enter your preffered username',validators = [Required()])
  password = PasswordField('Password',validators = [Required(), EqualTo('confirm_password',message = 'Passwords must match')])
  confirm_password = PasswordField('Confirm Password',validators = [Required(),Length(min=8,max=20)])
  submit = SubmitField('Sign Up')
  
  #Custom email validations
  def validate_user_email(self,data_field): #making sure an email address is used once
    if User.query.filter_by(user_email = data_field.data).first(): 
      raise ValidationError('There is an account already created with that email.')
    
  
  def validate_username(self,data_field):#making sure a username is used by only one user
    if User.query.filter_by(username = data_field.data).first():
      raise ValidationError('That username is already in use.')
    
#Login Form after registration
class LoginForm(FlaskForm):
  email = StringField('Enter your Email Address',validators=[Required(),Email()])
  password = PasswordField('Password',validators =[Required()])
  remember = BooleanField('Remember me')
  submit = SubmitField('Login')
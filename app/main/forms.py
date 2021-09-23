from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm): #update profile form
  bio = TextAreaField('Tell us about yourself.',validators=[Required()])
  submit = SubmitField('Submit')
  
class BlogForm(FlaskForm): #form for submitting pitches
  title = StringField('Blog title',validators=[Required()])
  blog = TextAreaField('Type in your blog.',validators=[Required()])
  submit = SubmitField('Submit')
  
class CommentsForm(FlaskForm): #form for submitting comments for different pitches
  comment = TextAreaField('Leave a comment.',validators=[Required()])
  submit = SubmitField('Submit')
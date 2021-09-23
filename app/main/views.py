import re
from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Blogs,Comments
from flask_login import login_required,current_user
from .forms import UpdateProfile,BlogForm,CommentsForm
from .. import db,photos
from ..quotes import get_quotes


# Views functions
@main.route('/',methods = ["GET"])
def  index():
  '''
  Function that returns the home page
  '''
  blogs_found = Blogs.get_blogs()
  quotes = get_quotes()
  title = ""
  return render_template('index.html',title = title, blogs = blogs_found, quotes = quotes)
  
@main.route('/user/<uname>')
def profile(uname): 
  user = User.query.filter_by(username = uname).first()
  
  if user is None: 
    abort(404)
   
  blogs = Blogs.query.filter_by(user_id = user.id) 
  return render_template("profile/profile.html",user = user,blogs = blogs)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname): 
  user = User.query.filter_by(username = uname).first()
  if user is None: 
    abort(404)
    
  form = UpdateProfile()
  
  if form.validate_on_submit(): 
    user.biodata = form.bio.data
    
    db.session.add(user)
    db.session.commit()
    
    return redirect(url_for('.profile',uname = user.username))
  
  return render_template('profile/update.html',form = form)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname): 
  user = User.query.filter_by(username = uname).first()
  if 'photo' in request.files: 
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path 
    db.session.commit()
  return redirect(url_for('main.profile',uname = uname))
  
@main.route('/newblog',methods = ["GET","POST"])
@login_required
def new_blog(): 
  '''Function that collects new blog template's data'''
  form = BlogForm()
  if form.validate_on_submit(): 
    new_blog = Blogs(title = form.title.data,blog = form.blog.data,user = current_user)
    new_blog.save_blog()
    return redirect(url_for('.index'))
  
  title="Blog input"
  return render_template('new_blog.html',title = title, form = form)

@main.route('/comments/<int:id>',methods = ['GET','POST'])
def new_comment(id): 
  form = CommentsForm()
  blog = Blogs.query.filter_by(id = id).first()
  if blog is None: 
    abort(404) 
  print(blog)
  
  if form.validate_on_submit(): 
    
    # Updated comment instance
    new_comment = Comments(comment = form.comment.data,user=current_user,blog_id = id)
    new_comment.save_comment()
  
  comments_found = Comments.get_comments(id)
  title = 'Comments'
  return render_template('comments.html', title = title, comments_form = form, blog = blog,comments_found = comments_found)

@main.route('/deletecomment/<int:id>',methods = ['GET','POST'])
@login_required
def delete_comment(id): 
  '''Function to delete a comment'''
  comment = Comments.query.filter_by(id = id).first()
  if comment: 
    db.session.delete(comment)
    db.session.commit()
  else: 
    abort(404)
  return redirect(url_for('.new_comment', id = comment.blog_id))

@main.route('/deleteblog/<int:id>',methods = ['GET','POST'])
@login_required
def delete_blog(id): 
  '''Function to delete a blog'''
  blogs = Blogs.query.filter_by(id = id).first()
  if blogs: 
    db.session.delete(blogs)
    db.session.commit()
  else: 
    abort(404)
  return redirect(url_for('.profile', uname = blogs.user.username))

# @main.route('/like/<int:id>', methods = ['POST', 'GET'])
# def like(id):
#     get_pitches = Upvote.get_upvotes(id)
#     for pitch in get_pitches:
#       continue
#     new_vote = Upvote( pitch_id=id)
#     new_vote.save()     
#     return redirect(url_for('main.index'))    

# @main.route('/dislike/<int:id>', methods = ['POST','GET'])
# def dislike(id):
#     get_pitch = Downvote.get_downvotes(id)
#     for pitch in get_pitch:
#       continue
#     new_downvote = Downvote(pitch_id=id)
#     new_downvote.save()     
#     return redirect(url_for('main.index'))  
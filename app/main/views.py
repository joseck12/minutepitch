from flask import render_template,redirect,url_for,flash,request
from . import main
from flask_login import login_required,current_user
from .. import db
from ..models import User,Pitch,Comments
from flask_login import login_user
from .forms import Pitch,Comment

@main.route('/home', methods=['GET','POST'])
@login_required
def index():
   pitch_form = Pitch()
   comment_form = Comment()
   title = 'Home'
   if pitch_form.validate_on_submit():

      # Updated review instance
      pitch = Pitch(pitch = pitch_form.pitch.data, category = pitch_form.category.data, user=current_user)

      if pitch is not None:
         pitch.save_pitch()   
      else:
         flash('You must enter a pitch')
      flash('Your pitch was published')
      
   return render_template('home.html', title= title, pitch = pitch_form, comment = comment_form) 

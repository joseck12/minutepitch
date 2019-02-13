from flask import render_template,redirect,url_for,flash,request
from . import main
from flask_login import login_required,current_user
from .. import db
from ..models import User
from flask_login import login_required
from .forms import Pitch

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
         flash('A pitch is required')
      flash('The pitch has been successfully published')

   return render_template('index.html', title= title, pitch = pitch_form, comment = comment_form)

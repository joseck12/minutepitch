from flask import render_template
from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import RegistrationForm,LoginForm,PitchForm
from .. import db
from flask_login import login_user,logout_user,login_required
from . import auth
from ..email import mail_message


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to minute-pitch","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)


@auth.route('/login', methods=['GET','POST'])
def login():
         log_in = LogIn()
     title = 'Login'
     if log_in.validate_on_submit():
          user = User.query.filter_by(username = log_in.username.data).first()
          if user is not None and bcrypt.check_password_hash(user.password, log_in.password.data):
               login_user(user,log_in.remember_me.data)
               return redirect(request.args.get('next') or url_for('main.index'))

          flash('The username or password you entered is incorrect.')

     return render_template('auth/login.html', login = log_in, title = title)


     @auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index")) 

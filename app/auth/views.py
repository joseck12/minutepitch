from flask import render_template,redirect,url_for,flash,request
from . import auth

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

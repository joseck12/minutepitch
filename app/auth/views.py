from flask import render_template,redirect,url_for,flash,request
from . import auth

@auth.route('/login', methods=['GET','POST'])
def login():

     return render_template('auth/login.html', login = log_in, title = title)

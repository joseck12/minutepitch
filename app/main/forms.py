from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,RadioField
from wtforms.validators import DataRequired,Length,Email,EqualTo
from ..models import User

class Pitch(FlaskForm):
   '''
   Creates pitch form
   '''
   pitch = StringField('Pitch', validators=[DataRequired()])
   category = RadioField('Category', choices=[('product','#product'),('pickup','#pickup'),('project','#project'),('politics','#politics'),('misc','#misc')], default='misc')
   submit = SubmitField('Post')
class LoginForm(FlaskForm):
    # email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

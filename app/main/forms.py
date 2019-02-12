from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,RadioField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class Pitch(FlaskForm):
   '''
   Creates pitch form
   '''
   pitch = StringField('Pitch', validators=[DataRequired()])
   category = TextAreaField('Category', validators=[Required()])
   submit = SubmitField('Post')

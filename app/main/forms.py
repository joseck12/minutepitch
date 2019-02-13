from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,RadioField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class Pitch(FlaskForm):
   '''
   Creates pitch form
   '''
   category = RadioField('Category', choices=[('product','#product'),('pickup','#pickup'),('project','#project'),('politics','#politics'),('misc','#misc')], default='misc')
   pitch = StringField('Pitch', validators=[DataRequired()])
   submit = SubmitField('Post')

class Comment(FlaskForm):
   pitch_comment = StringField('Pitch', validators=[DataRequired()]), render_kw={"placeholder": "Add comment"})
    submit = SubmitField('Post')

from . import db,login_manager
from datetime import datetime
from flask_login import UserMixin

class User(db.Model):
   '''
   Creates table to hold user data
   '''

   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(30), unique=True, nullable=False)
   email = db.Column(db.String(100), unique=True, nullable=False)
   password = db.Column(db.String(300), nullable=False)
   avatar = db.Column(db.String(30), default='default.jpg')
   pitches = db.relationship('Pitch', backref='author', lazy=True)
   comment = db.relationship('Comments', backref='commenter', lazy=True)
   bio = db.Column(db.String(140))


   def __repr__(self):
      return f"User('{self.username}', '{self.email}')"

class Pitch(db.Model):
   '''
   Creates table to hold user posts
   '''
   id = db.Column(db.Integer, primary_key=True)
   pitch = db.Column(db.String(140))
   time_posted = db.Column(db.String, nullable=False, default=datetime.utcnow)
   upvotes = db.Column(db.Integer, default=0, nullable=False)
   downvotes = db.Column(db.Integer, default=0, nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   comments = db.relationship('Comments', backref='comments', lazy=True)

   def __repr__(self):
      return f"Pitch('{self.pitch}', '{self.time_posted}', '{self.upvotes}', '{self.downvotes}', '{self.user_id}')"

   def save_pitch(self):
      db.session.add(self)
      db.session.commit()

   @classmethod
   def get_pitches(cls,cat):
      pitches = Pitch.query.filter_by(category=cat).all()
      return pitches

class Comments(db.Model):
   '''
   Creates table to hold comments on pitches
   '''
   id = db.Column(db.Integer, primary_key=True)
   comment = db.Column(db.String(140))
   time_posted = db.Column(db.String, nullable=False, default=datetime.utcnow)
   category = db.Column(db.String(15), nullable=False)
   pitch_id = db.Column(db.Integer, db.ForeignKey('pitch.id'), nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

   def __repr__(self):
      return f"Comments('{self.comment}', '{self.time_posted}', '{self.pitch_id}', '{self.user_id}')"

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))

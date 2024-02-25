from .database import db

class Users(db.Model):
    __tablename__='users'
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String,nullable=False,unique=True)
    name = db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False,unique=True)


class User_details(db.Model):
    __tablename__='user_details'
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id',ondelete='CASCADE'),unique=True,primary_key=True)
    bio = db.Column(db.String,nullable=False)
    age = db.Column(db.Integer,nullable=False)
    gender = db.Column(db.String,nullable=False)
    ph_no = db.Column(db.Integer,nullable=False)
    photo = db.Column(db.BLOB,nullable=False  )
    login_streak = db.Column(db.Integer,nullable=False)
    email = db.Column(db.String,nullable=False)
    last_login_date = db.Column(db.String,nullable=False)

class Posts(db.Model):
    __tablename__ = 'posts'
    post_id= db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    content = db.Column(db.BLOB, nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id',ondelete='CASCADE'),unique=True)
    
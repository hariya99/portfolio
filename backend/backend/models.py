# from flask import current_app
from flask_login import UserMixin
# from itsdangerous import URLSafeTimedSerializer as Serializer

from backend import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # hash of 20 chars
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # hash of 60 chars 
    # password = db.Column(db.String(60), nullable=False)
    details = db.relationship('UserDetails', backref='author', lazy=True)

    # def get_reset_token(self):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     return s.dumps({'user_id' : self.id})

    # @staticmethod
    # def verify_reset_token(token, max_age=900):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token, max_age=max_age)
    #     except:
    #         None
    #     # return the user with the user_id
    #     return User.query.get(user_id) 

    def __repr__(self) -> str:
        return f"User({self.username}, {self.email})"

class UserDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    about = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self) -> str:
        return f"UserDetails({self.first_name}, {self.last_name}, {self.about})"


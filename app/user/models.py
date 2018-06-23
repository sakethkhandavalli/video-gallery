from flask_sqlalchemy import SQLAlchemy
from app import db
import re
from werkzeug.security import generate_password_hash, check_password_hash
from app.playlist.models import *

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    #myplaylists = db.relationship('Playlist', backref='myuser', cascade="all, delete-orphan", lazy='dynamic')
    no_playlists = db.Column(db.Integer)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.no_playlists = 3
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def to_dict(self):
        return {'user_id' : self.user_id, 'name': self.name, 'email': self.email}

    def __repr__(self):
        return "User<%d> %s" % (self.user_id, self.name)

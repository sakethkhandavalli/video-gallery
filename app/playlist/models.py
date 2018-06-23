from flask_sqlalchemy import SQLAlchemy
from app import db
from app.user.models import *

class Playlist(db.Model):
    __tablename__ = 'playlists'
    playlist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __init__(self, title, user_id):
        self.title = title
        self.user_id = user_id

    def to_dict(self):
        return {'playlist_id': self.playlist_id,'title':self.title,'user_id':self.user_id}
	
    def __repr__(self):
        return "Playlist<%d> %s %d" % (self.playlist_id, self.title, self.user_id)

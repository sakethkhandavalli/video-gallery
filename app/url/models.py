import datetime 
from flask_sqlalchemy import SQLAlchemy
from app import *
from app.playlist.models import *

class Url(db.Model):
    __tablename__ = 'urls'
    url_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(2000),nullable = False)
    name = db.Column(db.String(200),nullable = False)
    time = db.Column(db.DateTime)
#    favorite = db.Column(db.Boolean)
 #   watch_later = db.Column(db.Boolean)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.playlist_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
        
#    def __init__(self,url,favorite,watch_later,playlist):
    def __init__(self, url, name ,playlist_id, user_id):
        self.url = url
        self.name = name
        self.time = datetime.datetime.utcnow()
  #      self.favorite = favorite
   #     self.watch_later = watch_later
        self.playlist_id = playlist_id
        self.user_id = user_id

    def to_dict(self):
        return {'url': self.url, 'name':self.name, 'playlist_id': self.playlist_id}

    def __repr__(self):
        return "url<%s> %s %s %s" % (self.url, self.name, self.time, self.playlist_id)

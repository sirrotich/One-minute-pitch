from . import db

class User(db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.author}'

        

class new_pitch:
    def __init__(title,pitch,author,):
        self.title = title
        self.pitch = pitch
        self.author = author
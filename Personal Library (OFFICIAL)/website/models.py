from . import db
from flask_login import UserMixin, current_user
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_cover = db.Column(db.String(10000))
    mobilebg = db.Column(db.String(10000))
    introbg = db.Column(db.String(10000))
    fontcolor = db.Column(db.String(10000))
    autore = db.Column(db.String(150))
    titolo = db.Column(db.String(150))
    genere = db.Column(db.String(150))
    trama = db.Column(db.String(10000))
    date_start = db.Column(db.String(150))
    date_end = db.Column(db.String(150))
    valutazione = db.Column(db.Integer)
    spicy = db.Column(db.Integer)
    lacrime = db.Column(db.Integer)
    favourite_Charac = db.Column(db.String(150))
    hated_Charac = db.Column(db.String(150))
    favourite_Scene = db.Column(db.String(10000))
    best_Phrase = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Wish_List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_cover = db.Column(db.String(10000))
    autore = db.Column(db.String(150))
    titolo = db.Column(db.String(150))
    costo = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color_primary = db.Column(db.String(10000))
    color_secondary = db.Column(db.String(10000))
    color_accent = db.Column(db.String(10000))
    font_color = db.Column(db.String(10000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    wish_list = db.relationship('Wish_List')
    color = db.relationship('Color')
    

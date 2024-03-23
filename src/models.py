

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False, default=True)

    favorite_planet = db.relationship('Favorite_Planet', backref='user', lazy=True) 
    favorite_character = db.relationship('Favorite_Character', backref='user', lazy=True) 


    def __repr__(self):
        return '<User: %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }
    

class Favorite_Character(db.Model):
    __tablename__ = "favorite_character"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("character.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "item_id": self.item_id, 
        }
class Favorite_Planet(db.Model):
    __tablename__ = "favorite_planet"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "item_id": self.item_id, 
        }


class Character(db.Model):
    __tablename__ = "character"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    birth_year = db.Column(db.String(50), unique=False, nullable=False)
    gender = db.Column(db.String(50), unique=False, nullable=False)
    height = db.Column(db.Float, unique=False, nullable=False)
    eye_color = db.Column(db.String(50), unique=False, nullable=False)
    hair_color = db.Column(db.String(50), unique=False, nullable=False)
    skin_color = db.Column(db.String(50), unique=False, nullable=False)
    item_type = db.Column(db.String(50), unique=False, nullable=False)
    
    favorite_character = db.relationship('Favorite_Character', backref='character', lazy=True)

    def __repr__(self):
        return '<Character: %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height": self.height,
            "eye_color": self.eye_color,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "item_type": self.item_type
        }


class Planet(db.Model):
    __tablename__ = "planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    population = db.Column(db.Float, unique=False, nullable=False)
    terrain = db.Column(db.String(50), unique=False, nullable=False)
    diameter = db.Column(db.Float, unique=False, nullable=False)
    climate = db.Column(db.String(50), unique=False, nullable=False)
    rotation_period = db.Column(db.Float, unique=False, nullable=False)
    item_type = db.Column(db.String(50), unique=False, nullable=False)
    
    favorite_planet = db.relationship('Favorite_Planet', backref='planet', lazy=True)
    

    def __repr__(self):
        return '<Planet: %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "diameter": self.diameter,
            "climate": self.climate,
            "rotation_period": self.rotation_period,
            "item_type": self.item_type
        }
    

    
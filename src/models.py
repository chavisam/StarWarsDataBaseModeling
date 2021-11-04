import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,DateTime , Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(Integer)
    email = Column(String(200),unique=True)
    character_favorites = relationship('Character_favorites', backref='User', lazy=True)
    planet_favorites = relationship('Planet_favorites', backref='User', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True) 
    character_name = Column(String(250),nullable=False)
    hair_color = Column(String(100))
    eye_color = Column(String(100))
    skin_color = Column(String(100))
    gender = Column(String(100))
    yob = Column(DateTime)
    height = Column(Integer)
    weight = Column(Integer)
    description = Column(Text(400))
    homeworld = Column(String(250))
    character_favorites = relationship('Character_favorites', backref='Character', lazy=True)




class Planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(200))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    Orbital_period = Column(Integer)
    gravity = Column(String(200))
    population = Column(Integer)
    climate = Column(String(200))
    terrain = Column(String(200))
    description = Column(Text(400))
    url = Column(String(200))
    planet_favorites = relationship('Planet_favorites', backref='Planet', lazy=True)



class Starship(Base):
    __tablename__ = 'starship'
    starship_id = Column(Integer,primary_key=True)
    model = Column(String(200))
    class_type = Column(String(200))
    manufacturer = Column(String(200))
    cost = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    speed = Column(Integer)
    

class Character_favorites(Base):
    __tablename__ = 'character_favorites'
    favorites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    character_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    

class Planet_favorites(Base):
    __tablename__ = 'planet_favorites'
    favorites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    planet_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)


    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
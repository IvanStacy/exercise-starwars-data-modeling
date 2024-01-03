import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.sql import func

# db = SQLAlchemy(app)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    registration_date = Column(DateTime, server_default=func.now())
    favorites = relationship('Favorites', back_populates='user')


class Character(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    species = Column(String(50))
    homeworld = Column(String(100))
    affiliation = Column(String(100))
    description = Column(String(500))
    favorites = relationship('Favorites', back_populates='character')

class Planet(Base):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))
    population = Column(Integer)
    description = Column(String(500))

    # Relationship to Favorite Model
    favorites = relationship('Favorites', back_populates='planet')

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer, nullable=False)
    model = Column(String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="Starships")


class Favorites(Base):
    __tablename__ = 'favorites'
    favorite_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.character_id'))
    planet_id = Column(Integer, ForeignKey('planets.planet_id'))
    starships_id = Column(Integer, ForeignKey("starships.id"))
    favorite_date = Column(DateTime, server_default=func.now())

    # Relationships to User, Character, and Planet Models
    user = relationship('User', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    starships = relationship("Starships", back_populates="Favorites")
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

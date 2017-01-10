import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    room_code = Column(Integer, nullable=False)
    current_question = Column(String(250))
    winner = Column(Integer)

class Users(Base):
    __tablename__ = 'users'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    points = Column(Integer)

    game_id = Column(Integer, ForeignKey('game.id'))
    game = relationship(Game)

class Answers(Base):
    __tablename__ = 'answers'

    answer_id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'))
    game = relationship(Game)
    user_id = Column(Integer), ForeignKey('users.id')
    users = relationship(Users)

engine = create_engine('sqlite:///witsandwagers.db')

Base.metadata.create_all(engine)
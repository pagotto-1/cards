from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/cards_db')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    status_delete = Column(Boolean, default=True)

class Deck(Base):
    __tablename__ = 'decks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('usuarios.id'), ondelete='SET NULL')
    name = Column(String(100), nullable=False)
    topic = Column(String(100))
    description = Column(String)
    status_delete = Column(Boolean, default=True)

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, autoincrement=True)
    deck_id = Column(Integer, ForeignKey('baralhos.id'))
    question = Column(String)
    answer = Column(String)
    status_delete = Column(Boolean, default=True)
from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/cards_db')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)
    criado_em = Column(DateTime, nullable=False, server_default=func.now())
    atualizado_em = Column(DateTime, nullable=False, server_default=func.now())
    status_delete = Column(Boolean, default=True)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

class Deck(Base):
    __tablename__ = 'decks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'))
    name = Column(String(100), nullable=False)
    topic = Column(String(100))
    description = Column(String)
    status_delete = Column(Boolean, default=True)

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, autoincrement=True)
    deck_id = Column(Integer, ForeignKey('decks.id', ondelete='SET NULL'))
    question = Column(String)
    answer = Column(String)
    status_delete = Column(Boolean, default=True)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
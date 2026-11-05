from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

engine = create_engine('mysql+pymysql://root:senaisp@localhost:3306/cards_db')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha_hash = Column(String(255), nullable=False)
    status_delete = Column(Boolean, default=True)

class Baralho(Base):
    __tablename__ = 'baralhos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), ondelete='SET NULL')
    nome = Column(String(100), nullable=False)
    topico = Column(String(100))
    descricao = Column(String)
    status_delete = Column(Boolean, default=True)

class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True, autoincrement=True)
    baralho_id = Column(Integer, ForeignKey('baralhos.id'))
    pergunta = Column(String)
    resposta = Column(String)
    status_delete = Column(Boolean, default=True)
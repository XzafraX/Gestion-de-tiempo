from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///PGestion.db', echo = True)

#Usuario
class Usuario(Base):
    """Modelo de usuarios"""
    __tablename__ = 'USUARIOS'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    email = Column(String(50), unique= True, nullable=False)
    password = Column(String(50),nullable=False)

    tareas = relationship("Tarea", back_populates="usuario")
    
    def __repr__(self):
        """Representación en string del objeto Usuario"""
        return f"<Usuario(nombre='{self.name}', email='{self.email}')>"
    
#Tareas
class Tarea(Base):
    """Modelo de Tareas"""
    __tablename__= 'TAREAS'
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    description = Column(String(200))
    fecha = Column(DateTime,default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey('USUARIOS.id'))

    usuario = relationship("Usuario",back_populates="tareas")
    def __repr__(self):
        """Representación en string del objeto Tarea"""
        return f"<Tarea(titulo='{self.name}', usuario_id={self.usuario_id})>"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
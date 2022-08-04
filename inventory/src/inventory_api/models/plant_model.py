from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from helpers.database import Base
from sqlalchemy import Boolean, Column, ForeignKey


class DbPlant(Base):
    __tablename__='plants'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    is_public = Column(Boolean)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('DbUser', back_populates='plants')
    events = relationship('DbEvent', back_populates='plant')

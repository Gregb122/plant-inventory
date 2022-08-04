from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.orm import relationship
from helpers.database import Base
from sqlalchemy import Column, ForeignKey


class DbEvent(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    is_public = Column(Boolean)
    plant_id = Column(Integer, ForeignKey('plants.id'))
    plant = relationship('DbPlant', back_populates='events')

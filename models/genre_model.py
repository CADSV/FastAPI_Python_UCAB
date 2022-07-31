# Project imports
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import relationship
from config_db import Base

# Genre Model: Genre Table
class GenreModel(Base):

    __tablename__ = 'genres'

    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)
    Tracks = relationship('TrackModel', back_populates='GenreModel', lazy='joined')
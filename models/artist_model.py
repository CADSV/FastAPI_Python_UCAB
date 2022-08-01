# Project import
from sqlalchemy import  Column, Integer, String 
from sqlalchemy.orm import relationship
from config_db import Base


# Album Model: Album Table
class ArtistModel(Base):

    __tablename__ = 'artists'

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    Albums = relationship('AlbumModel', back_populates='Artist', lazy='joined')
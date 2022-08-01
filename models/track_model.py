# Project Imports
from sqlalchemy import Column, Integer, String , Float, ForeignKey
from sqlalchemy.orm import relationship
from config_db import Base


# Track Model: Track Table
class TrackModel(Base):

    __tablename__ = "tracks"
    
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('albums.AlbumId'))
    Album = relationship('AlbumModel', back_populates='Tracks', lazy='joined')
    MediaTypeId = Column(Integer, ForeignKey('media_types.MediaTypeId'))
    MediaType = relationship('MediaTypeModel', back_populates='Tracks', lazy='joined')
    GenreId = Column(Integer, ForeignKey('genres.GenreId'))
    Genre = relationship('GenreModel', back_populates='Tracks', lazy='joined')
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)
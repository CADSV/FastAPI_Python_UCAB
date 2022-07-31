# Project Imports
from sqlalchemy import Column, Integer, String , Float, ForeignKey
from sqlalchemy.orm import relationship
from config_db import Base


# Track Model: Track Table
class TrackModel(Base):

    __tablename__ = "tracks"
    
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey('Album.AlbumId'))
    Album = relationship('AlbumModel', back_populates='TrackModel', lazy='joined')
    MediaTypeId = Column(Integer, ForeignKey('media_type.MediaTypeId'))
    MediaType = relationship('MediaTypeModel', back_populates='TrackModel', lazy='joined')
    GenreId = Column(Integer, ForeignKey('Genre.GenreId'))
    Genre = relationship('GenreModel', back_populates='TrackModel', lazy='joined')
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)
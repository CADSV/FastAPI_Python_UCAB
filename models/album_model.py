# Project imports
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config_db import Base


# Album Model: Album Table
class AlbumModel(Base):

    __tablename__ = 'albums'

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey('artists.ArtistId'))
    Artist = relationship('ArtistModel', back_populates='Albums', lazy='joined')
    Tracks = relationship('TrackModel', back_populates='Album', lazy='joined')
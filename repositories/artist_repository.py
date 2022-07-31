# Project Imports
from typing import List
from sqlalchemy.orm import Session
from models.album_model import AlbumModel
from models.artist_model import ArtistModel
from models.track_model import TrackModel
from schemas.album_schema import AlbumSchema
from schemas.artist_schema import ArtistSchema 
from schemas.track_schema import TrackSchema


# Artist Repository: Use for the Artist Repository
class ArtistRepository:


    # Get all artists from the database
    def get_all_artists(self, db: Session) -> List[ArtistSchema]:

        artist_list: List[ArtistSchema] = db.query(ArtistModel).all()

        return artist_list



    # Get all the almbus of a specific artist
    def get_all_artist_albums(self, db: Session, artist_id: int) -> List[AlbumSchema]:

        artist_albums: List[AlbumSchema] = db.query(AlbumModel).filter(AlbumModel.ArtistId == artist_id).all()

        return artist_albums


    # Get all the songs of a specific artist
    def get_all_artist_tracks(self, db: Session, artist_id: int) -> List[TrackSchema]:
        artist_tracks: List[TrackSchema] = db.query(TrackModel).join(AlbumModel, AlbumModel.AlbumId == TrackModel.AlbumId).join(ArtistModel, ArtistModel.ArtistId == AlbumModel.ArtistId).filter(ArtistModel.ArtistId == artist_id).all()
        return artist_tracks
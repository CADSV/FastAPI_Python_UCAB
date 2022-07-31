from typing import List

from sqlalchemy.orm import Session
from schemas.album_schema import TrackSchema
from models.album_model import Album
from models.track_model import Track


# Album Repository: Use for the Album Repository
class AlbumRepository:

    # Get all songs from a specific album
    def get_all_album_songs(self, db: Session, album_id: int) -> List[TrackSchema]:
        
        track_list: List[TrackSchema] = db.query(Track).filter(Track.AlbumId == album_id).all()

        return track_list
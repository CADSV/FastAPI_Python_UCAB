# Project Imports
from sqlalchemy.orm import Session
from models.genre_model import GenreModel
from models.track_model import TrackModel
from models.media_type_model import MediaTypeModel
from schemas.track_schema import TrackSchema


# Track Repository: Use for the Track Repository
class TrackRepository:

    # Get all data from a specific track
    def get_track_detail(self, db: Session, track_id: int) -> TrackSchema:
        
        track_detail: TrackSchema = db.query(TrackModel).join(GenreModel,GenreModel.GenreId == TrackModel.GenreId, isouter = True).join(
        MediaTypeModel,MediaTypeModel.MediaTypeId == TrackModel.MediaTypeId, isouter =True).filter(TrackModel.TrackId == track_id).first()
        
        return track_detail
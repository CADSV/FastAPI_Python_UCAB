from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session

from config_db import get_db
from repositories.track_repository import TrackRepository
from schemas.track_schema import TrackSchema

router = APIRouter(
    tags=["Tracks"]
)

@router.get("/song/{id}/", response_model=TrackSchema, status_code=status.HTTP_200_OK)
def get_track_detail(
    id: int,
    db: Session = Depends(get_db),
    track_repo: TrackRepository = Depends(TrackRepository)
    ) -> TrackSchema:
    
    return track_repo.get_track_detail(db = db, track_id = id)
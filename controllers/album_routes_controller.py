# Project Import
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List
from config_db import get_db
from repositories.album_repository import AlbumRepository
from schemas.track_schema import TrackSchema


router = APIRouter(
    tags=["Albums"]
)

# To get the list of songs from a specific album
@router.get("/albums/{id}/", response_model=List[TrackSchema], status_code=status.HTTP_200_OK)
def get_track_list(
    id: int,
    db: Session = Depends(get_db),
    album_repo: AlbumRepository = Depends(AlbumRepository)
    ) -> List[TrackSchema]:
    
    return album_repo.get_all_album_songs(db = db, album_id = id)

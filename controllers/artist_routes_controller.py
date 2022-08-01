# Project Imports
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List
from config_db import get_db
from repositories.artist_repository import ArtistRepository
from schemas.album_schema import AlbumSchema
from schemas.artist_schema import ArtistSchema
from schemas.track_schema import TrackSchema

router = APIRouter(
    tags=["Artist"]
)

@router.get("/singers/", response_model=List[ArtistSchema], status_code=status.HTTP_200_OK)
def get_artist_list(db: Session = Depends(get_db),
    artist_repo: ArtistRepository = Depends(ArtistRepository)
    ) -> List[ArtistSchema]:
    
    return artist_repo.get_all_artists(db=db)

@router.get("/singers/{id}/", response_model=List[AlbumSchema], status_code=status.HTTP_200_OK)
def get_artist_album(
    id: int,
    db: Session = Depends(get_db),
    artist_repo: ArtistRepository = Depends(ArtistRepository)
    ) -> List[ArtistSchema]:
    
    return artist_repo.get_all_artist_albums(db = db, artist_id = id)

@router.get("/singer/{id}", response_model=List[TrackSchema], status_code=status.HTTP_200_OK)
def get_artist_tracks(
    id: int,
    db: Session = Depends(get_db),
    artist_repo: ArtistRepository = Depends(ArtistRepository)
    ) -> List[TrackSchema]:
    
    return artist_repo.get_all_artist_tracks(db = db, artist_id = id)
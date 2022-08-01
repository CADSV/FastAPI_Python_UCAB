# Project imports
from typing import Optional
from pydantic import BaseModel
from schemas.artist_schema import ArtistSchema


# Album Schema: Use for the Album data
class AlbumSchema(BaseModel):

    AlbumId: int
    Title: Optional[str]
    ArtistId: Optional[int]
    Artist: Optional[ArtistSchema]

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "AlbumId": 1,
                "Title": "The 20/20 Experience",
                "ArtistId": 1,
                "Artist": {
                    "ArtistId": 1,
                    "Name": "Justin Timberlake"
                }
            }
        }

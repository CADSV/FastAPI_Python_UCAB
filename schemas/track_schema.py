from typing import Optional
from pydantic import BaseModel
from schemas.album_schema import AlbumSchema
from schemas.gender_schema import GenreSchema
from schemas.media_type_shcema import MediaTypeSchema


# Track Schema: Use for the Track data
class TrackSchema(BaseModel):

    TrackId: int
    Name: str
    AlbumId: Optional[int]
    Album: Optional[AlbumSchema]
    MediaTypeId: int
    MediaType: Optional[MediaTypeSchema]
    GenreId: Optional[int]
    Genre: Optional[GenreSchema]
    Composer: Optional[str]
    Milliseconds: int
    Bytes: Optional[int]
    UnitPrice: float

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "TrackId": 1,
                "Name": "Mirrors",
                "AlbumId": 1,
                "MediaTypeId": 1,
                "GenreId": 1,
                "Composer": "Justin timberlake",
                "Milliseconds": 1543,
                "Bytes": 1024,
                "UnitPrice": 2.99
            }
        }

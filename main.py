# Project Imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config_db import Base, engine
from controllers.album_routes_controller import router as album_router
from controllers.artist_routes_controller import router as artist_router
from controllers.track_routes_controller import router as track_router


# get_application: returns a FastAPI application
def get_application()  -> FastAPI:
    
    # To create the Database 
    Base.metadata.create_all(bind=engine)

    # To create a FastAPI application
    app = FastAPI(
        title="API Music Store - Chinook",
        description="Python Project made by Carlos Doffiny S-V",
        version="1.0.0",
        openapi_url="/api/openapi.json",
        docs_url="/docs/",
        redoc_url="/redoc/",
    )

    # add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # add the routes

    app.include_router(artist_router, prefix="/music-store/api/v1")
    app.include_router(album_router, prefix="/music-store/api/v1")
    app.include_router(track_router, prefix="/music-store/api/v1")

    return app

# main: runs the application
app = get_application()


# Initial get request to check if the server is running
@app.get("/")
def home() -> dict:
	return {"message": "Bienvenido a la API de la tienda de música de Carlos Doffiny S-V"}
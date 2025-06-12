from fastapi import FastAPI, HTTPException, Depends, Request, Form, UploadFile
from fastapi.responses import HTMLResponse
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession

from app.flights_operations import FlightsOperations
from app.pets_models import *
from app.pets_operations import PetsOperations
from app.users_models import *
from app.users_operations import UsersOperations
from database.connection_db import get_session
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(
    title="Parcial Final Sigmotoa flights",
    description="API para gestionar la empresa de vuelos con mascotas.",
    version="1.0.0"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "..", "templates"))

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/users/", response_model=List[UsersResponse])
async def get_all_user():
    async for session in get_session():
        return await UsersOperations.find_all_users(session)

@app.get("/pets/", response_model=List[PetsResponse])
async def get_all_pets():
    async for session in get_session():
        return await PetsOperations.find_all_pets(session)

@app.get("/users/", response_model=List[UsersResponse])
async def get_all_flights():
    async for session in get_session():
        return await FlightsOperations.find_all_flights(session)

@app.post("/cosmetics", response_model=CosmeticColabResponse, tags=["Maquillaje"])
async def create_cosmetic_endpoint(cosmetic: CosmeticColabCreate, session: AsyncSession = Depends(get_session)):
    return await CosmeticOperations.create_cosmetic(session, cosmetic.model_dump())

@app.put("/cosmetics/{cosmetic_id}", response_model=CosmeticColabResponse, tags=["Maquillaje"])
async def update_cosmetic_endpoint(
        cosmetic_id: int,
        marca_maquillaje: str = Form(None),
        videojuego: str = Form(None),
        fecha_colaboracion: str = Form(None),
        tipo_colaboracion: str = Form(None),
        incremento_ventas_maquillaje: str = Form(None),
        image_file: UploadFile = None,
        session: AsyncSession = Depends(get_session)
):
    """
    Actualiza un registro de colaboración de maquillaje.
    Solo los campos enviados en la solicitud serán actualizados.
    """
    update_data = {}

    # Recopilar campos no nulos
    if marca_maquillaje: update_data["marca_maquillaje"] = marca_maquillaje
    if videojuego: update_data["videojuego"] = videojuego
    if fecha_colaboracion: update_data["fecha_colaboracion"] = fecha_colaboracion
    if tipo_colaboracion: update_data["tipo_colaboracion"] = tipo_colaboracion
    if incremento_ventas_maquillaje: update_data["incremento_ventas_maquillaje"] = incremento_ventas_maquillaje

    # Si hay una nueva imagen, procesarla
    if image_file and image_file.filename:
        image_url = await save_file(image_file)
        if isinstance(image_url, dict) and "error" in image_url:
            raise HTTPException(status_code=400, detail=image_url["error"])
        update_data["image_url"] = image_url

    updated = await CosmeticOperations.update_cosmetic(session, cosmetic_id, update_data)
    if not updated:
        raise HTTPException(status_code=404, detail="La colaboración no fue actualizada")
    return updated

@app.post("/cosmetics/delete", tags=["Maquillaje"])
async def delete_cosmetic_by_id(
    request: Request,
    id: int = Form(...),
    session: AsyncSession = Depends(get_session)
):
    deleted = await CosmeticOperations.delete_cosmetic(session, id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="El registro de cosmético no fue encontrado"
        )
    return {"message": "Registro de cosmético eliminado con éxito"}


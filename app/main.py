from fastapi import FastAPI, HTTPException, Depends, Request, Form, UploadFile
from fastapi.responses import HTMLResponse
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
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
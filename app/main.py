from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm.session import Session
from starlette.concurrency import run_in_threadpool

import app.crud as crud 
from app.database import SessionLocal, engine, get_db
import app.models as models
import app.utils as utils
import app.schemas as schemas




models.Base.metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="./templates")
db = get_db()

# Configure CORS middleware
origins = [
    "http://localhost",
    "http://0.0.0.0",
    "http://0.0.0.0:8000",
    "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    
@app.post("/generate")
async def generate_content(payload: schemas.GeneratePayload, db: Session = Depends(get_db)):
    generated_text = await run_in_threadpool(utils.generate_content, db, payload.topic)
    return {"generated_text": generated_text}
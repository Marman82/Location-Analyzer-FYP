from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, Form, UploadFile
from typing import Annotated
from CNNinference import *
from io import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadfile")
async def create_file(
    file: Annotated[bytes, File()],
):
    savePath = "./predict.jpg"
    image = Image.open(BytesIO(file))
    image.save(savePath)
    [lat, lon] = prediction(savePath)
    return {
        "lon": str(lon),
        "lat": str(lat)
    }

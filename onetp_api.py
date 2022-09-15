from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import StreamingResponse 
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/tobi")
def tobi():
    return "hola tobi"
        

@api.post("/update")
def update(audio: UploadFile, area: str = Form()):
    # TODO: super inseguro
    with open(area+".mp3", "wb") as f:
        f.write(audio.file.read())

@api.get("/area/{area}")
def area(area: str):
    def iterfile():
        with open(area+".mp3", mode="rb") as f: 
            yield from f 

    return StreamingResponse(iterfile(), media_type="video/3gpp")
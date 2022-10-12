# import fastapi
from fastapi import FastAPI
from starlette.responses import StreamingResponse
from diffusers import StableDiffusionPipeline
import io
from matplotlib.pyplot import imsave
import numpy as np

# instantiate the app
app = FastAPI()

# run on startup
@app.on_event("startup")
async def startup_event():
    print("Starting up...")
    # load the model
    global pipe
    pipe = StableDiffusionPipeline.from_pretrained("../models/stable-diffusion-v1-4")
    pipe = pipe.to("cpu")
    print('Started!')

# create a route
@app.get("/")
def index():
    return {"text" : "We're running!"}

# create a text2img route
@app.post("/text2img")
def text2img(text: str):
    # generate an image
    img = pipe(text).images[0]
    img = np.array(img)
    buffer = io.BytesIO()
    imsave(buffer, img)
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="image/png")

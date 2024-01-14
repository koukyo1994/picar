import base64

import cv2
import uvicorn
from fastapi import FastAPI

import camera

app = FastAPI()


@app.get("/image")
def get_image():
    """Return the current camera frame as a base64 encoded string."""
    frame = camera.get_frame()
    _, buffer = cv2.imencode(".jpg", frame)
    img_str = base64.b64encode(buffer).decode("utf-8")
    return {"img_str": img_str}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")

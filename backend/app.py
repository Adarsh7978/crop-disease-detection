from fastapi import FastAPI, UploadFile, File
import uvicorn
from model.predict import predict_image

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    result = await predict_image(file)
    return {"prediction": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

model=pickle.load(open("model.pkl","rb"))

app=FastAPI()
class InputData(BaseModel):
	features:list[float]

@app.get("/")
def home():
	return {"message":"API working sucessfully."}

@app.post("/predict")
def predict(data:InputData):
	features_array=np.array(data.features).reshape(1,-1)
	prediction=model.predict(features_array)
	return {"Prediction":prediction[0]}
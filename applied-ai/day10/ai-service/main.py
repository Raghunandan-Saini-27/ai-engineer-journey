from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import numpy as np
from database import add_prediction_to_db,create_table,return_all_pred

create_table()
model=pickle.load(open("model.pkl","rb"))
app=FastAPI()
class InputData(BaseModel):
	features:list[int]

@app.get("/")
def home():
	return {"message":"API working sucessfully."}

@app.post("/predict")
def predict(data:InputData):
	inp_array = np.array(data.features).reshape(1, -1)
	prediction=model.predict(inp_array)
	db_input = str(data.features)
	db_output = prediction[0].item()
	s_data = [(db_input, db_output)]
	add_prediction_to_db(s_data)
	return {"Prediction":prediction[0]}

@app.get("/predictions")
def predictions():
	all_pred=return_all_pred()
	if not all_pred:
		return {"message": "No predictions found", "data": []}
	results = [dict(row) for row in all_pred]
	return {"predictions": results}
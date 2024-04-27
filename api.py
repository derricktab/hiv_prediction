from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from joblib import load

app = FastAPI()

# Replace with your actual model and scaler path
MODEL_PATH = 'best_model.h5'
SCALER_PATH = 'scaler.joblib'

# Load the trained model and the scaler
model = load_model(MODEL_PATH)
scaler = load(SCALER_PATH)

# Define a request body for the API
class SequenceData(BaseModel):
    sequence: str

# Helper function to preprocess input data
def preprocess_data(sequence):
    # Assuming the same preprocessing as during model training
    encoded_sequence = np.array([ord(x) - ord('A') + 1 if x != '-' else 0 for x in sequence])
    scaled_sequence = scaler.transform([encoded_sequence])
    return scaled_sequence[..., np.newaxis]  # Add channel dimension

# Define the prediction endpoint
@app.post("/predict/")
async def predict_resistance(data: SequenceData):
    try:
        # Preprocess the input data
        preprocessed_data = preprocess_data(data.sequence)
        
        # Generate prediction
        prediction = model.predict(preprocessed_data)
        resistance = int(prediction[0][0] > 0.5)
        return {"resistance": resistance}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

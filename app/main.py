import joblib
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
from app.api.api_v1.functions.classify_message import classify_message
from app.api.api_v1.functions.get_model import get_model
from app.api.api_v1.api import router as api_router
from mangum import Mangum

app = FastAPI()
#handling the requests for our REST API for different URI

model = get_model()

@app.get('/')
def get_root():

	return {'message': 'Welcome to the spam detection API'}


app.include_router(api_router,prefix="/api/v1")

handler = Mangum(app)
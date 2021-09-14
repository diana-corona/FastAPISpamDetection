import joblib
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
from classify_message import classify_message

app = FastAPI()
#handling the requests for our REST API for different URI

model = joblib.load('spam_classifier.joblib')

@app.get('/')
def get_root():

	return {'message': 'Welcome to the spam detection API'}


@app.get('/spam_detection_query/')
async def detect_spam_query(message: str):
	return classify_message(model, message)
#query parameters are part of the URL string and are prefixed by a “?
#/spam_detection_query/?message=’message’

@app.get('/spam_detection_path/{message}')
async def detect_spam_path(message: str):
	return classify_message(model, message)
#the input data is passed to the API as a path in the URL
#/spam_detection_query/message
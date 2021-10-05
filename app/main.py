from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
from classify_message import classify_message
from load_model import load_model

app = FastAPI()
#handling the requests for our REST API for different URI

@app.get('/')
def get_root():
	return {'message': 'Welcome to the spam detection API'}


@app.get('/spam_detection_query/MLPClassifier/')
async def detect_spam_query(message: str):
	sel_model = load_model('MLPClassifier');
	return classify_message(sel_model, message)

@app.get('/spam_detection_query/KNeighbors/')
async def detect_spam_query(message: str):
	sel_model = load_model('KNeighbors');
	return classify_message(sel_model, message)

@app.get('/spam_detection_query/DecisionTree/')
async def detect_spam_query(message: str):
	sel_model = load_model('DecisionTree');
	return classify_message(sel_model, message)

@app.get('/spam_detection_query/RandomForest/')
async def detect_spam_query(message: str):
	sel_model = load_model('RandomForest');
	return classify_message(sel_model, message)



#query parameters are part of the URL string and are prefixed by a “?
#/spam_detection_query/?message=’message’

#@app.get('/spam_detection_path/{message}')
#async def detect_spam_path(message: str, model:str):
#	sel_model = load_model(model);
#	return classify_message(sel_model, message)
#the input data is passed to the API as a path in the URL
#/spam_detection_query/message
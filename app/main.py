from fastapi import FastAPI
from classify_message import classify_message
from load_model import load_model

app = FastAPI()
#handling the requests for our REST API for different URI

@app.get('/')
def get_root():
	return {'message': 'Welcome to the spam detection API'}

@app.get('/Mlpclassifiers/')
async def Mlpclassifiers(message: str):
	sel_model = load_model('MLPClassifier');
	return classify_message(sel_model, message)

@app.get('/Kneighbors/')
async def Kneighbors(message: str):
	sel_model = load_model('KNeighbors');
	return classify_message(sel_model, message)

@app.get('/Decisiontrees/')
async def Decisiontrees(message: str):
	sel_model = load_model('DecisionTree');
	return classify_message(sel_model, message)

@app.get('/Randomforests/')
async def Randomforests(message: str):
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
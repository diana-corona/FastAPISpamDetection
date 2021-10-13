import os
from fastapi import FastAPI
from mangum import Mangum
from preprocessor import preprocessor
from classify_message import classify_message
from load_model import load_model

#to make accesible the autogenerated documentation
stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"
app = FastAPI(title="lambda_fastapi_spam_detection_api", openapi_prefix=openapi_prefix) # Here is the magic


#handling the requests for our REST API for different URI
@app.get('/')
def get_root():
	return {'message': 'Welcome to the spam detection API'}


@app.get('/mlpclassifiers/')
async def mlpclassifier(message: str):
	message=preprocessor(message)
	sel_model = load_model('MLPClassifier');
	return classify_message(sel_model, message)

@app.get('/kneighbors/')
async def kneighbor(message: str):
	message=preprocessor(message)
	sel_model = load_model('KNeighbors');
	return classify_message(sel_model, message)

@app.get('/decisiontrees/')
async def decisiontree(message: str):
	message=preprocessor(message)
	sel_model = load_model('DecisionTree');
	return classify_message(sel_model, message)

@app.get('/randomforests/')
async def randomforest(message: str):
	message=preprocessor(message)
	sel_model = load_model('RandomForest');
	return classify_message(sel_model, message)

handler = Mangum(app)


#query parameters are part of the URL string and are prefixed by a “?
#/?message=’message’

#@app.get('/spam_detection_path/{message}')
#async def detect_spam_path(message: str, model:str):
#	sel_model = load_model(model);
#	return classify_message(sel_model, message)
#the input data is passed to the API as a path in the URL
#/message
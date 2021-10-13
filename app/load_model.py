import boto3 
from io import BytesIO
import joblib
import json 

def load_model(model):
	with BytesIO() as f:
		if model == '/mlpclassifiers':
			boto3.client("s3").download_fileobj(Bucket="serverless-spam-detection", Key="model/spam_classifier_MLPClassifier.joblib", Fileobj=f)
			f.seek(0)
			model = joblib.load(f)
		elif model == '/kneighbors':
			boto3.client("s3").download_fileobj(Bucket="serverless-spam-detection", Key="model/spam_classifier_KNeighbors.joblib", Fileobj=f)
			f.seek(0)
			model = joblib.load(f)
		elif model == '/decisiontrees':
			boto3.client("s3").download_fileobj(Bucket="serverless-spam-detection", Key="model/spam_classifier_DecisionTree.joblib", Fileobj=f)
			f.seek(0)
			model = joblib.load(f)
		elif model == '/randomforests':
			boto3.client("s3").download_fileobj(Bucket="serverless-spam-detection", Key="model/spam_classifier_RandomForest.joblib", Fileobj=f)
			f.seek(0)
			model = joblib.load(f)
		else:
			boto3.client("s3").download_fileobj(Bucket="serverless-spam-detection", Key="model/spam_classifier_MLPClassifier.joblib", Fileobj=f)
			f.seek(0)
			model = joblib.load(f)	
	return model

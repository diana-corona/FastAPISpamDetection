import joblib

def get_model():
	return joblib.load('app/api/api_v1/model/spam_classifier.joblib')

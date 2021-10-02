import joblib
from preprocessor import preprocessor

def classify_message(model, message):
	message = preprocessor(message)
	#preprocess message like during the training
	label = model.predict([message])[0]
	#predict
	spam_prob = model.predict_proba([message])
	#calculate probability
	return {'label': label, 'spam_probability': spam_prob[0][1]}
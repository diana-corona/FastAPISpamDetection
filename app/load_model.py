import joblib

def load_model(model):
	sel_model = None
	if model == "MLPClassifier":
		sel_model = joblib.load('models/spam_classifier_MLPClassifier.joblib')
	elif model == "KNeighbors":
		sel_model = joblib.load('models/spam_classifier_KNeighbors.joblib')
	elif model == "DecisionTree":
		sel_model = joblib.load('models/spam_classifier_DecisionTree.joblib')
	elif model == "RandomForest":
		sel_model = joblib.load('models/spam_classifier_RandomForest.joblib')
	else:
		sel_model = joblib.load('models/spam_classifier_MLPClassifier.joblib')

	return sel_model

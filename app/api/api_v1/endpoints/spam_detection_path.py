import joblib
from fastapi import APIRouter
from app.api.api_v1.functions.classify_message import classify_message
from app.api.api_v1.functions.get_model import get_model


router = APIRouter ()

model = get_model()

@router.get('/{message}')
async def detect_spam_path(message: str):
	return classify_message(model, message)
#the input data is passed to the API as a path in the URL
#/spam_detection_path/message
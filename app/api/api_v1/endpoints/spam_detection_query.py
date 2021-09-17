import joblib
from fastapi import APIRouter
from app.api.api_v1.functions.classify_message import classify_message
from app.api.api_v1.functions.get_model import get_model

router = APIRouter ()
model = get_model()

@router.get('/')
async def detect_spam_query(message: str):
	return classify_message(model, message)
#query parameters are part of the URL string and are prefixed by a “?
#/spam_detection_query/?message=’message’


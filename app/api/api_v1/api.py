from fastapi import APIRouter
from .endpoints import spam_detection_query
from .endpoints import spam_detection_path

router = APIRouter ()
router.include_router(spam_detection_query.router,prefix="/spam_detection_query",tags=["spam_detection_query"])
router.include_router(spam_detection_path.router,prefix="/spam_detection_path",tags=["spam_detection_path"])
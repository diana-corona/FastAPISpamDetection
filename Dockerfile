
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

WORKDIR /app

RUN pip3 install -r requirements.txt 
RUN python training/train_spam_detector_MLPClassifier.py
RUN python training/train_spam_detector_KNeighborsClassifier.py
RUN python training/train_spam_detector_DecisionTreeClassifier.py
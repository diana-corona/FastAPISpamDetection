
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

WORKDIR /app

RUN pip3 install -r requirements.txt 
RUN python train_spam_detector.py

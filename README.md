# FastAPISpamDetection

### Spam Text Message Classification Data
Obtained from

https://www.kaggle.com/team-ai/spam-text-message-classification


### Using the model on Jupyter notebooks
A Jupiter notebook demo is available in FastAPISpamDetection_demo.ipynb

### Deploying the App on Docker
The docker file:
1. Pulls the FastAPI docker image.
1. Copies the app directory to the docker image.
1. Set the app directory as the working directory.
1. Install requirements listed in requirements.txt
1. Call train_spam_detector.py to train the model

To build the docker image run (this will train the model)
```
docker build -t spam-detection .
```
To run the docker image run (this will deploy the API)
```
docker run -d --name spam-detection -p 80:80 spam-detection
```

### API Automatically Generated Documentation
The API documentation is generated automatically by FASTAPI, 
To access the API documentation go to 

http://localhost/docs

### Query Parameters
Query parameters are part of the URL string and are prefixed by a “?”

For example:

http://localhost/spam_detection_query/?message=WINNER

### Path Variables
In Path Variables, the input data is passed to the API as a path in the URL

For example:

http://localhost/spam_detection_path/Hi
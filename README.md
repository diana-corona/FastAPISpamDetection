# FastAPISpamDetection

### Spam Text Message Classification Data
Obtained from

https://www.kaggle.com/team-ai/spam-text-message-classification

### Virtual eviroment

To create a virtual eviroment run
```
virtualenv -p python3.7 env 
```
To activate a virtual eviroment run
```
source ./env/bin/activate
```
To install dependencies
```
 pip3 install -r requirements.txt
```

### Test

To run tests run:
```
pytest
```

### Github workflow
The Github workflow:
1. Activates when push on branch Venv-Github-workflow
1. Setup python version to 3.7
1. Install python Virtual ENV
1. Activate Virtual ENV
1. Run Tests
1. Zip dependencies
1. Add API files to zipped dependencies files


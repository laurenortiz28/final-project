### Quick Start - How to run locally


Use this command to install your dependencies from the requirements.txt:
```
cd into the API folder 

cd API
```
pip install -r requirements.txt
```

Run this app with:
```
uvicorn main:app --reload
```
That's it. The app is now running locally. 
It's an API, so you can use Postman or a similar program to hit the endpoints it is serving.

to run the create database python code you will need to open terminal
```
python create_db.py
python insertdata.py
```
then make sure to type in 
```
uvicorn main:app --reload
```
before you continue to work on the code
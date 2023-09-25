# -*- coding: utf-8 -*-
"""
Need to install flask-ngrok, pyngrok to run Flask in google colab.
ngrok will tunnel localhost  127.0.0.0 -> external url
pip install flask-ngrok
pip install pyngrok
pip install flask_cors


Step 7 - Deployment **


model exported during earlier step will be loaded and entegagred with web framework (we will use Python Flask as an integration framework)
</font>

"""

from flask import Flask, jsonify, request
#from flask_ngrok import run_with_ngrok
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#below step is required only when application is hosted in google colab
#run_with_ngrok(app)

with open('../model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def home():
    return '<p>Hello World</p>'


@app.route("/predict", methods=['POST'])
def predict():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        age = json.get('age')
        distance = json.get('distance')
        nos = json.get('nos')
        price = model.predict([[age, distance, nos]])
        return f"{price}"
    else:
        return 'Content-Type not supported!'


if __name__ == "__main__":
    app.run()

"""
Testing API
curl -d '{ "age": 15, "distance": 500, "nos": 10 }' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/predict 
"""
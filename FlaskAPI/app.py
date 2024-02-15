import flask
from flask import Flask, jsonify, request
import json
from data_input import data_in
import numpy as np
import pickle
# .........................................................................................................................................
# .........................................................................................................................................
def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

# .........................................................................................................................................

app = Flask(__name__)
@app.route('/predict', methods=['GET'])
def predict():
    response = json.dumps({'response': 'yahhhh!'})
    return response, 200
# .........................................................................................................................................
def predict():
    # stub input features
    x = np.array(data_in).reshape(1,-1)
    # load model
    model = load_models()
    prediction = model.predict(x)[0]
    response = json.dumps({'response': prediction})
    return response, 200

# .........................................................................................................................................

if __name__ == '__main__':
    application.run(debug=True)
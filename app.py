from flask import Flask, jsonify, request
from flask import CORS
import joblib
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense , Input , GlobalMaxPooling1D
from tensorflow.keras.layers import LSTM , GRU , SimpleRNN , Embedding
from tensorflow.keras.models import Model
from tensorflow.keras.losses import BinaryCrossentropy , SparseCategoricalCrossentropy

model = joblib.load('Model')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def main():

    if request.method == 'POST':
        output = []
        data = request.get_json().get('tokens')

        for token in data:
            string_preprocess = Tokenizer.texts_to_sequences([token])
            result= model.predict(string_preprocess)
            if result == 'Dark':
                print("Dark Pattern")
            else:
                print("no")

#         dark = [data[i] for i in range(len(output)) if output[i] == 'Dark']
#         for d in dark:
#             print(d)
#         print()
#         print(len(dark))

#         message = '{ \'result\': ' + str(output) + ' }'
#         print(message)

#         json = jsonify(message)

#         return json

# if __name__ == '__main__':
#     app.run(threaded=True, debug=True)


        



            
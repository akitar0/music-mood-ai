from flask import Flask, request, jsonify
from flask_cors import CORS
from src.predict import predict_mood

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def home():
    return "Music Mood API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    result = predict_mood(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run()

@app.route('/clusters', methods=['GET'])
def clusters():
    import pandas as pd
    df = pd.read_csv('data/spotify_tracks.csv')

    # use same features as clustering
    data = df[['energy', 'valence']].head(200)

    return jsonify(data.to_dict(orient='records'))

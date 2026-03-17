import joblib
import numpy as np
import pandas as pd

# ---------------------------
# LOAD MODELS
# ---------------------------
model = joblib.load('models/model.pkl')
scaler = joblib.load('models/scaler.pkl')
encoder = joblib.load('models/encoder.pkl')

# ---------------------------
# LOAD DATASET (FOR PLAYLIST)
# ---------------------------
df_global = pd.read_csv('data/spotify_tracks.csv')


# ---------------------------
# PLAYLIST FUNCTION
# ---------------------------
def get_playlist(mood):
    songs = df_global[df_global['mood'] == mood]

    if len(songs) == 0:
        return ["No songs found"]

    sample = songs.sample(min(5, len(songs)))

    if 'track_name' in sample.columns:
        return sample['track_name'].tolist()
    else:
        return ["Sample Song 1", "Sample Song 2"]


# ---------------------------
# PREDICTION FUNCTION
# ---------------------------
def predict_mood(data):

    # Extract ALL 10 features
    tempo = data['tempo']
    danceability = data['danceability']
    energy = data['energy']
    key = data['key']
    loudness = data['loudness']
    speechiness = data['speechiness']
    acousticness = data['acousticness']
    instrumentalness = data['instrumentalness']
    liveness = data['liveness']
    valence = data['valence']

    # Create feature array
    features = np.array([[
        tempo, danceability, energy, key, loudness,
        speechiness, acousticness, instrumentalness,
        liveness, valence
    ]])

    # Scale
    features = scaler.transform(features)

    # Predict
    pred = model.predict(features)
    mood = encoder.inverse_transform(pred)[0]

    # ---------------------------
    # EXPLANATION (SMARTER)
    # ---------------------------
    if energy > 0.7 and tempo > 120:
        reason = "High energy and fast tempo → energetic mood"
    elif valence > 0.6:
        reason = "Positive valence → happy mood"
    elif acousticness > 0.6:
        reason = "High acoustic content → calm mood"
    elif valence < 0.3:
        reason = "Low valence → sad/angry mood"
    else:
        reason = "Balanced musical features"

    # ---------------------------
    # RECOMMENDATION
    # ---------------------------
    recommendations = {
        "Happy": "Pop / Party Playlist 🎉",
        "Sad": "Lo-fi / Chill Playlist 😔",
        "Energetic": "Workout / EDM Playlist ⚡",
        "Calm": "Meditation / Acoustic Playlist 🌿",
        "Angry": "Rock / Metal Playlist 🔥",
        "Neutral": "Mixed Mood Playlist 🎧"
    }

    # ---------------------------
    # PLAYLIST
    # ---------------------------
    playlist = get_playlist(mood)

    # ---------------------------
    # RETURN RESPONSE
    # ---------------------------
    return {
        "mood": mood,
        "reason": reason,
        "recommendation": recommendations.get(mood, "General Playlist"),
        "playlist": playlist
    }
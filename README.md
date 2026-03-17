# 🎵 Music Mood AI

An AI-powered web application that predicts the **emotional mood of songs** based on audio features and enhances music discovery with intelligent recommendations.

---

## 🚀 Overview

Music Mood AI uses a machine learning model to analyze song attributes like tempo, energy, valence, and more to classify songs into moods such as:

- Happy 😊  
- Sad 😔  
- Energetic ⚡  
- Calm 🌿  
- Angry 🔥  
- Neutral 🎧  

The system also provides **playlist suggestions** and **insights** based on predictions.

---

## 🧠 Features

- 🎯 Real-time mood prediction using ML model  
- 🎧 Mood-based playlist generator  
- 📊 Interactive song cluster visualization  
- 🔍 Insight explanation for each prediction  
- 🌐 Full-stack deployment (Frontend + Backend)  
- ⚡ Fast API response using Flask  

---

## 🛠️ Tech Stack

### 🔹 Backend
- Python  
- Flask  
- Scikit-learn  
- Pandas, NumPy  
- Joblib  

### 🔹 Machine Learning
- Random Forest Classifier  
- Feature Engineering  
- Data Preprocessing & Scaling  
- Model Evaluation (Accuracy, F1-score, Confusion Matrix)  

### 🔹 Frontend
- HTML, CSS, JavaScript  
- Chart.js (for visualization)  

### 🔹 Deployment
- Backend → Render  
- Frontend → Vercel  
- Version Control → GitHub  

---

## 📊 Dataset

- Spotify Tracks Dataset (~20k+ records)  
- Features used:
  - tempo  
  - danceability  
  - energy  
  - loudness  
  - acousticness  
  - instrumentalness  
  - liveness  
  - valence  

---

## ⚙️ How It Works

1. User inputs song features  
2. Data is preprocessed & scaled  
3. ML model predicts mood  
4. Results returned with:
   - Mood  
   - Explanation  
   - Playlist recommendation  

---

## 📈 Model Performance

- Accuracy: ~75–80% (optimized to avoid overfitting)  
- Cross-validation used for robustness  
- Feature importance analysis included  

---

## 🎯 Objectives

- Predict emotional mood of songs  
- Discover patterns in audio features  
- Improve music recommendation experience  

---

## 👨‍💻 Authors

- Akki Bhai & Team  

---

## 🔗 Live Demo

- Frontend: https://music-mood-ai.vercel.app  
- Backend API: https://music-mood-ai.onrender.com  

---

## 💡 Future Improvements

- Spotify API integration  
- Personalized recommendations  
- Deep learning models  
- User-based mood tracking  

---

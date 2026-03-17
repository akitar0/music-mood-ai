import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from preprocessing import load_data, clean_data, create_labels


# ---------------------------
# 1. LOAD & PREPROCESS DATA
# ---------------------------
df = load_data('data/spotify_tracks.csv')
df = clean_data(df)

# Feature Engineering
df['tempo_energy'] = df['tempo'] * df['energy']
df['energy_valence'] = df['energy'] * df['valence']

df.columns = df.columns.str.strip().str.lower()
print("COLUMNS:", df.columns.tolist())


# ---------------------------
# 2. FEATURE ENGINEERING
# ---------------------------
df['tempo_energy'] = df['tempo'] * df['energy']


# ---------------------------
# 3. DEFINE FEATURES
# ---------------------------
features = [
    'tempo',
    'danceability',
    'energy',
    'loudness',
    'acousticness',
    'instrumentalness',
    'tempo_energy',
    'energy_valence'
]

X = df[features]
y = df['mood']


# ---------------------------
# 4. ENCODE LABELS
# ---------------------------
le = LabelEncoder()
y = le.fit_transform(y)


# ---------------------------
# 5. CLUSTERING (UNSUPERVISED)
# ---------------------------
kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

joblib.dump(kmeans, 'models/kmeans.pkl')

# Cluster visualization
plt.figure()
sns.scatterplot(
    x='energy',
    y='valence',
    hue='cluster',
    data=df,
    palette='viridis'
)
plt.title("Music Clusters (Energy vs Valence)")
plt.savefig('models/clusters.png')
plt.close()


# ---------------------------
# 6. TRAIN TEST SPLIT
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ---------------------------
# 7. SCALING
# ---------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# ---------------------------
# 8. MODEL TRAINING
# ---------------------------
model = RandomForestClassifier(
    n_estimators=80,
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    class_weight='balanced',
    random_state=42
)

model.fit(X_train, y_train)


# ---------------------------
# 9. EVALUATION
# ---------------------------
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"\nTest Accuracy: {acc:.4f} ({acc*100:.2f}%)")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ---------------------------
# 10. CONFUSION MATRIX
# ---------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.savefig('models/confusion_matrix.png')
plt.close()


# ---------------------------
# 11. CROSS VALIDATION
# ---------------------------
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print("Cross Validation Accuracy:", scores.mean())


# ---------------------------
# 12. FEATURE IMPORTANCE
# ---------------------------
importance = model.feature_importances_

imp_df = pd.DataFrame({
    'Feature': features,
    'Importance': importance
}).sort_values(by='Importance', ascending=False)

print("\nFeature Importance:")
print(imp_df)

plt.figure()
plt.barh(imp_df['Feature'], imp_df['Importance'])
plt.title("Feature Importance")
plt.savefig('models/feature_importance.png')
plt.close()


# ---------------------------
# 13. SAVE EVERYTHING
# ---------------------------
joblib.dump(model, 'models/model.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(le, 'models/encoder.pkl')

print("\n✅ Model, scaler, encoder saved!")
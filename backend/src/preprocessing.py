import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df.columns = df.columns.str.strip().str.lower()
    return df

def create_labels(df):
    def mood(row):
        energy = row['energy']
        valence = row['valence']
        tempo = row['tempo']
        dance = row['danceability']
        loud = row['loudness']
        speech = row.get('speechiness', 0)
        acoustic = row.get('acousticness', 0)
        instr = row.get('instrumentalness', 0)
        live = row.get('liveness', 0)

        # 🔥 HAPPY
        if energy > 0.6 and valence > 0.6 and dance > 0.6:
            return "Happy"

        # 🔥 ENERGETIC
        elif energy > 0.75 and tempo > 120 and loud > -10:
            return "Energetic"

        # 🔥 ANGRY
        elif energy > 0.8 and valence < 0.3 and loud > -8:
            return "Angry"

        # 🔥 SAD
        elif energy < 0.4 and valence < 0.4 and acoustic > 0.5:
            return "Sad"

        # 🔥 CALM
        elif energy < 0.4 and acoustic > 0.6 and instr > 0.3:
            return "Calm"

        # 🔥 NEUTRAL
        else:
            return "Neutral"

    df['mood'] = df.apply(mood, axis=1)
    return df
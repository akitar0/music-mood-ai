import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df):
    plt.figure()
    sns.countplot(x='mood', data=df)
    plt.title("Mood Distribution")
    plt.savefig("mood_distribution.png")

def correlation_heatmap(df):
    plt.figure()
    sns.heatmap(df.corr(), annot=True)
    plt.title("Feature Correlation")
    plt.savefig("correlation.png")
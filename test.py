import pandas as pd

# Load the dataset
def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00356/winequality-red.csv"  # Correct URL
    data = pd.read_csv(url, sep=';')
    return data

# Example usage
data = load_data()
print(data.head())

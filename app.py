import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
def load_data():
    url = 'https://assets.datacamp.com/production/repositories/488/datasets/013936d2700e2d00207ec42100d448c23692eb6f/winequality-red.csv'#"https://archive.ics.uci.edu/ml/machine-learning-databases/00356/winequality-red.csv"  # Corrected URL
    data = pd.read_csv(url, sep=';')
    return data

# Data Transformation Logic
def transform_data(df):
    # Create quality label (Low if quality <= 5, High if quality > 5)
    df['quality_label'] = df['quality'].apply(lambda x: 'Low' if x <= 5 else 'High')
    
    # Add acidity ratio (fixed acidity / volatile acidity)
    df['acidity_ratio'] = df['fixed acidity'] / df['volatile acidity']
    
    # Add density to alcohol ratio (density / alcohol)
    df['density_to_alcohol_ratio'] = df['density'] / df['alcohol']
    
    return df

# Load and transform the data
data = load_data()
data = transform_data(data)

# Streamlit UI
# Title of the application
st.title("Enhanced Wine Quality Analysis")

# Display the dataset
st.write("## Raw Data")
st.write(data.head())

# Visualization 1: Alcohol Content Distribution
st.write("## Alcohol Content Distribution")
fig, ax = plt.subplots()
data['alcohol'].hist(bins=20, ax=ax)
ax.set_title("Alcohol Content Distribution")
ax.set_xlabel("Alcohol")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Visualization 2: Quality Label Distribution
st.write("## Quality Label Distribution")
quality_counts = data['quality_label'].value_counts()
st.bar_chart(quality_counts)

# Visualization 3: Acidity Ratio Distribution
st.write("## Acidity Ratio Distribution")
fig, ax = plt.subplots()
data['acidity_ratio'].hist(bins=20, ax=ax)
ax.set_title("Acidity Ratio Distribution")
ax.set_xlabel("Acidity Ratio")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Visualization 4: Density to Alcohol Ratio vs. Quality
st.write("## Density to Alcohol Ratio vs. Quality")
fig, ax = plt.subplots()
for label in data['quality_label'].unique():
    subset = data[data['quality_label'] == label]
    ax.scatter(subset['density_to_alcohol_ratio'], subset['quality'], label=label)

ax.set_title("Density to Alcohol Ratio vs. Quality")
ax.set_xlabel("Density to Alcohol Ratio")
ax.set_ylabel("Quality")
ax.legend()
st.pyplot(fig)

# titanic_task.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Title
st.title("Titanic Dataset - Exploratory Data Analysis")

# Load the Titanic dataset
df = sns.load_dataset('titanic')

# Show raw data
st.subheader("Raw Dataset")
st.write(df.head())

# Show basic info
st.subheader("Data Information")
st.write("Shape:", df.shape)
st.write("Columns:", df.columns.tolist())
st.write("Missing values:\n", df.isnull().sum())

# Visualizations
st.subheader("Survival Count")
st.bar_chart(df['survived'].value_counts())

st.subheader("Gender Distribution")
st.bar_chart(df['sex'].value_counts())

st.subheader("Survival by Gender")
st.bar_chart(df.groupby('sex')['survived'].sum())

st.subheader("Survival by Class")
st.bar_chart(df.groupby('pclass')['survived'].sum())

st.subheader("Age Distribution")
st.line_chart(df['age'].dropna().sort_values().reset_index(drop=True))
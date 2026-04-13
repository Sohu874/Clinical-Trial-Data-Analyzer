import streamlit as st
import pandas as pd

st.title("🧠 Clinical Trial Data Analyzer")

st.write("Upload your patient dataset (CSV file)")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("📊 Dataset Preview")
    st.write(df.head())

    st.subheader("📋 Data Info")
    st.write(df.describe())
    st.subheader("📈 Recovery Rate Analysis")

recovery_rate = df.groupby("arm")["outcome"].value_counts(normalize=True) * 100
st.write(recovery_rate)

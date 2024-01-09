import streamlit as st
import pandas as pd 

st.title("Palmers Penguins")

penguins__df = pd.read_csv("penguins.csv")

st.dataframe(penguins__df)

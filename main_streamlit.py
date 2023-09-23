import streamlit as st
import pandas as pd


st.markdown("# Chipotle Data")
st.sidebar.markdown("# Chipotle Data")

@st.cache
def get_data():
    return pd.read_csv("data.csv")
df = get_data()

st.write("# Keyanna Duker Streamlit App")
st.write("## Chipotle Dataset")
st.write(df)
 
st.write("## Filter By Visit Counts") 
## Filter to see locations with more than x visits
x = st.slider("See stores with more than ___ Visit Counts: ", value = 1000, min_value=2, max_value = 6342)
def get_data_by_raw_visit_counts(x):
    min_value = x
    new_data = df[df['raw_visit_counts'] >= min_value]
    new_data = new_data.sort_values("raw_visit_counts", ascending=False)
    return new_data
filtered_data = get_data_by_raw_visit_counts(x)
st.write(filtered_data)
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotnine import *

st.markdown("# Visualizations")
st.sidebar.markdown("# Visualization")

@st.cache
def get_data():
    return pd.read_csv("data.csv")
df = get_data()

st.write("### Spatial Map:")
st.write('#### Search For A Related Brand: ')
st.text_input("Search Brand", key = 'brand')
left_column, right_column = st.columns([1,4])
if left_column.button("Brand by Day"):
    rslt_df = df[df['same_day_brand'] == st.session_state.brand]
    st.map(rslt_df)
if right_column.button("Brand by Month"):
    rslt_df = df[df['same_month_brand'] == st.session_state.brand]
    st.map(rslt_df)

st.write("### Graphs:")
st.write("#### Percent Visits By City")

def draw_graph_day():
        return (
            ggplot(rslt_df1, aes(x = "same_day_brand", y = "same_day_brand_value"))
            + geom_col()
        )

def draw_graph_month():
        return (
            ggplot(rslt_df1, aes(x = "same_month_brand", y = "same_month_brand_value"))
            + geom_col()
        )

st.text_input("Search City", key = 'city')
rslt_df1 = df[df['city'] == st.session_state.city]
rslt_df1 = rslt_df1.head()

left_column, right_column = st.columns([1,3])
if left_column.button("Graph Brand by Day"):
    st.pyplot(draw_graph_day().draw(show = False))

if right_column.button("Graph Brand by Month"):
    key = "same_month_brand"
    value = "same_month_brand_value"
    st.pyplot(draw_graph_month().draw(show = False))
import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Dashboard example", 
    page_icon="🤩",
    )

tab1, tab2, tab3 = st.tabs(["Welcome", "Bubble Chart", "Bar Chart"])

# Sample Data
df = px.data.gapminder()

with tab1:
    st.header("Welcome!")
    st.title("Hello, my friend 👋")
    st.markdown(
        """ 
        **Here I will show you some basic charts using :rainbow[plotly]**
        """
    )
    if st.button("Send balloons!"):
        st.balloons()
with tab2:
    # Filters
    continent = st.selectbox("Select Continent", sorted(df["continent"].unique()), key="continent_tab2")
    year = st.slider("Select Year", int(df["year"].min()), int(df["year"].max()), 2007, key="year_tab2")

    filtered = df[(df["continent"] == continent) & (df["year"] == year)]

    # Chart 1: Scatter Plot

    fig1 = px.scatter(
        filtered,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="country",
        title="GDP vs Life Expectancy",
    )

    st.plotly_chart(fig1)

with tab3:
    # Filters
    continent = st.selectbox("Select Continent", sorted(df["continent"].unique()), key="continent_tab3")
    year = st.slider("Select Year", int(df["year"].min()), int(df["year"].max()), 2007, key="year_tab3")

    filtered = df[(df["continent"] == continent) & (df["year"] == year)]
    # Chart 2: Bar Chart
    
    fig2 = px.bar(
        filtered,
        x="country",
        y="pop",
        title="Population by Country",
    )

    st.plotly_chart(fig2)
  


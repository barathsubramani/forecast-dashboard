import streamlit as st
import plotly.express as px
from backend import get_data

st.set_page_config("Next Forecast!")

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 50px;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">Next Forecast!</h1>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 50px;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h4 class="title">A Minimalistic Weather Forecast Dashboard</h4>', unsafe_allow_html=True)

place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115, caption=dates)

    except KeyError:
        st.write("That place does not exist.")
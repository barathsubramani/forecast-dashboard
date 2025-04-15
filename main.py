import streamlit as st

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

place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days.")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

import streamlit as st

options = [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"]
genre = st.radio(
    "What's your favorite movie genre?",
    options,
    index=0,
)

st.write("You selected:", genre)
selected_index = options.index(genre)
st.write(f"Index of the selected genre is: {selected_index}")
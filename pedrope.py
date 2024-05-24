import streamlit as st


st.title(":beers:|:beer:|:beers::dancer::dancer::dancer::dancer::beers:|:beer:|:beers:")



video_file = open('pedro.webm', 'rb')
video_bytes = video_file.read()

st.video(video_bytes, loop=True, autoplay=True)


st.title(":beers:|:beer:|:beers::dancer::dancer::dancer::dancer::beers:|:beer:|:beers:")


	
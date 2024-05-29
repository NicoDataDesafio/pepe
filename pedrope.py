import streamlit as st
st.set_page_config(layout="wide", page_title="meme", page_icon="img/cropped-Beyond-Education_Horizonatal-color.png")

st.get_option("theme.primaryColor")
st.get_option("theme.secondaryBackgroundColor")
st.get_option("server.enableCORS")
st.get_option("server.enableXsrfProtection")

st.title(":beers:|:beer:|:beers::dancer::dancer::dancer::dancer::beers:|:beer:|:beers:")



video_file = open('pedro.webm', 'rb')
video_bytes = video_file.read()

st.video(video_bytes, loop=True, autoplay=True)


st.title(":beers:|:beer:|:beers::dancer::dancer::dancer::dancer::beers:|:beer:|:beers:")


	
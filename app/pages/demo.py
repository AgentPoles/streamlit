import streamlit as st
from streamlit_elements import elements

st.title("Demo")

with elements("media_player"):

    from streamlit_elements import media

    media.Player(
        url="https://youtu.be/aKVRj2TByAs", controls=True)


import streamlit as st


import joblib
import pandas as pd
from streamlit_elements import elements, mui
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Tell My Rent",
    page_icon="🏠",
)

housing_encoder = joblib.load('./app/model/housing_encoder.pk1')
district_encoder = joblib.load('./app/model/district_encoder.pk1')
model = joblib.load('./app/model/price_model.joblib')

html = 'Illustration by <a href="https://icons8.com/illustrations/author/JTmm71Rqvb2T">Dani Grapevine</a> from <a href="https://icons8.com/illustrations">Ouch!</a>'
st.title('Tell My Rent')
st.markdown(
    '### :blue[Tell My Rent] leverages the XGBoost Regression Algorithm to predict the Annual Rent of a House in Lagos Nigeria')


with open("./app/css/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.image(
        "./app/img/estate.gif", width=400)

    with elements("new_element"):
        st.markdown('<style>{}</style>'.format(f.read()),
                    unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([1, 2, 3, 4])
        with col1:
            st.write("")

        with col2:
            if st.button("Try it Now!"):
                switch_page("finder")

        with col3:
            st.write("")

        with col4:
            if st.button("Watch A Demo"):
                switch_page("demo")


st.markdown(html, unsafe_allow_html=True)

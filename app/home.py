
import streamlit as st


import joblib
import pandas as pd
from streamlit_elements import elements, mui
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Tell My Rent",
    page_icon="🏠",
)

housing_encoder = joblib.load('./model/housing_encoder.pk1')
district_encoder = joblib.load('./model/district_encoder.pk1')
model = joblib.load('./model/price_model.joblib')

html = 'Illustration by <a href="https://icons8.com/illustrations/author/JTmm71Rqvb2T">Dani Grapevine</a> from <a href="https://icons8.com/illustrations">Ouch!</a>'
st.title('Tell My Rent')
st.markdown(
    '### :blue[Tell My Rent] leverages the XGBoost Regression Algorithm to predict the Annual Rent of a House in Lagos Nigeria')


with open("./css/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    st.image(
        "./img/estate.gif", width=400)

    with elements("new_element"):
        st.markdown('<style>{}</style>'.format(f.read()),
                    unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([1, 2, 3, 4])
        with col1:
            st.write("")

        with col2:
            if st.button("Try it Now!"):
                switch_page("finder")

            # mui.Button(
            #     mui.icon.EmojiPeople(onClick=nav_page("finder")),
            #     mui.icon.DoubleArrow,
            #     "Try It Now!",

            # )

        with col3:
            st.write("")

        with col4:
            if st.button("Watch A Demo"):
                switch_page("demo")
            # mui.Button(
            #     mui.icon.AcUnit(onClick=nav_page("demo")),
            #     "Watch A Demo",

            # )


# m = st.markdown("""
# <style>
# div.stButton > button:first-child {
#     background-color: #ce1126;
#     color: white;
#     height: 3em;
#     width: 12em;
#     border-radius:10px;
#     border:3px solid #000000;
#     font-size:20px;
#     font-weight: bold;
#     margin: auto;
#     display: block;
# }

# div.stButton > button:hover {
# 	background:linear-gradient(to bottom, #ce1126 5%, #ff5a5a 100%);
# 	background-color:#ce1126;
# }

# div.stButton > button:active {
# 	position:relative;
# 	top:3px;
# }

# </style>""", unsafe_allow_html=True)


st.markdown(html, unsafe_allow_html=True)

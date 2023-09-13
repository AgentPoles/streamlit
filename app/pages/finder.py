import streamlit as st
import pandas as pd
import math
from home import housing_encoder, district_encoder, model


st.header('Estimate A Rent Price')

st.write('Check what that dream house would cost you before speaking to an agent')

with open("./css/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

with st.form('finder'):
    house_type = st.selectbox('Apartment Type',
                              ('flat / apartment', 'mini flat (room and parlour) ', 'single room',
                               'duplex', 'penthouse', 'building'))
    district = st.selectbox('House District',
                            ('lekki', 'victoria island', 'ojodu', 'yaba', 'surulere', 'ikoyi',
                             'ajah', 'gbagada', 'ikeja', 'ketu ogudu', 'ikeja gra', 'ogba',
                             'oshodi', 'ikotun', 'ketu shangisha', 'oregun', 'igando',
                             'allen avenue', 'agege', 'isolo', 'mushin', 'apapa', 'ketu ikosi',
                             'ikorodu', 'abule egba', 'oshodi ajao', 'ikeja adeniyi jones',
                             'opebi', 'oniru', 'oshodi mafoluku', 'isolo jakande',
                             'isolo ago palace', 'ejigbo', 'maryland', 'iju ishaga', 'festac',
                             'agbara', 'alimosho', 'okota', 'iju  ', 'idimu', 'alagbado',
                             'ketu ojota', 'irepo', 'iya ipaja', 'ijora ebute metta',
                             'lagos island', 'oke afa', 'ifako', 'badagry', 'agbado ijaiye',
                             'satellite town', 'onikan'))

    district_list = ['lekki', 'victoria island', 'ojodu', 'yaba', 'surulere', 'ikoyi',
                     'ajah', 'gbagada', 'ikeja', 'ketu ogudu', 'ikeja gra', 'ogba',
                             'oshodi', 'ikotun', 'ketu shangisha', 'oregun', 'igando',
                             'allen avenue', 'agege', 'isolo', 'mushin', 'apapa', 'ketu ikosi',
                             'ikorodu', 'abule egba', 'oshodi ajao', 'ikeja adeniyi jones',
                             'opebi', 'oniru', 'oshodi mafoluku', 'isolo jakande',
                             'isolo ago palace', 'ejigbo', 'maryland', 'iju ishaga', 'festac',
                             'agbara', 'alimosho', 'okota', 'iju  ', 'idimu', 'alagbado',
                             'ketu ojota', 'irepo', 'iya ipaja', 'ijora ebute metta',
                             'lagos island', 'oke afa', 'ifako', 'badagry', 'agbado ijaiye',
                             'satellite town', 'onikan']

    longitudes = ['6.4698° N', '6.4281° N', '6.6337° N', '6.5095° N']
    latitudes = ['3.5852° E', '3.4219° E', '3.3573° E', '3.3711° E']
    number_of_bedrooms = st.number_input('Number of Bedrooms', 1, 7, 1)
    number_of_bathrooms = st.number_input('Number of Bathrooms', 1, 7, 1)
    number_of_guest_toilet = st.number_input('Guest Toilets?', 1, 5, 1)
    number_of_parking_space = st.number_input('Parking Space?', 1, 4, 1)
    submit = st.form_submit_button('Tell My Rent')


if submit:
    with st.expander("Results"):
        encoded_housing_type = housing_encoder.transform([house_type])
        encoded_district = district_encoder.transform([district])
        new_input = {
            'housing_type': encoded_housing_type[0],
            'bedrooms': number_of_bedrooms,
            'bathrooms': number_of_bathrooms,
            'guest_toilet': number_of_guest_toilet,
            'parking_space': number_of_parking_space,
            'district': encoded_district[0]
        }
        data = pd.DataFrame([new_input])
        prediction = model.predict(data)
        rangeA = math.ceil(1.1 * prediction)
        rangeB = math.ceil(0.9 * prediction)

        df = pd.DataFrame({'minimum budget per year (N)': [rangeB],
                          'maximum budget per year (N)': [rangeA]})
        st.dataframe(df)
        st.bar_chart(df)
        st.map(latitude=6.4550, longitude=3.3841, color='#f345e4')

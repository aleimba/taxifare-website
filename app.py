import streamlit as st
import pandas as pd
import requests

'''
# TaxiFareModel, prediction for NYC
'''

'''
## Customer data input
'''

st.markdown('''Required input for the taxifare prediction''')
datetime_str = st.text_input('Input of date/time in format', '2014-07-06 19:18:00')
pickup_longitude = st.number_input('Insert a float for pickup_longitude, e.g. -73.950655', value=-73.950655)
pickup_latitude = st.number_input('Insert a float for pickuplatitude, e.g. 40.783282', value=40.783282)
dropoff_longitude = st.number_input('Insert a float for dropoff_longitude, e.g. -73.984365', value=-73.984365)
dropoff_latitude = st.number_input('Insert a float for dropoff_latitude, e.g. 40.769802', value=40.769802)
passenger_count = st.number_input('Insert an int for passenger_count, e.g. 2', value=2)
passenger_count = int(passenger_count) # already an int if given correctly, but make sure!
st.markdown(f'''passenger count int: {passenger_count}''')

url = 'https://taxifare.lewagon.ai/predict'

'''
## Taxifare prediction
'''

data = {'pickup_datetime': datetime_str,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
        }

if st.button('Get taxifare pred'):
    # print is visible in the server output, not in the page
    # print('button clicked!') # check for local runs
    st.write('Here\'s your taxifare pred 🎉:')
    st.write('Further clicks are not visible but are executed')
    response = requests.get(url, params=data)

    # print(response.status_code) # check for local runs
    fare_pred = response.json()['fare']
    # print(fare_pred) # check for local runs

    st.markdown(f'API status code: {response.status_code}')

    st.markdown(f'Taxifare prediction **{round(fare_pred, 2)}$** for your route from "red" to "blue" ')

    pickup_dropoff_map = pd.DataFrame({'lat': [pickup_latitude, dropoff_latitude], 'lon': [pickup_longitude, dropoff_longitude], 'color': ['#0044ff', '#FF0000']})
    st.map(pickup_dropoff_map, color='color')

else:
    st.write('☝️ click button for taxifare prediction')

st.error('NYC predictions based on historical data, might not be accurate!')

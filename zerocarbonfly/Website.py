#!/usr/bin/env python
# coding: utf-8


import pandas as pd
df_airport = pd.read_csv(filename_airport)
df_airport.head()


df_aircraft = pd.read_csv(filename_aircraft)
df_aircraft.head()


departure_airport_code = "LAX"
arrival_airport_code = "SFO"
aircraft='Airbus A320'
num_of_pax = 1


import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import kayak
from PIL import Image
import numpy as np
filename_airport = './assets/airports.csv'
filename_aircraft = './assets/aircraft.csv'
output = './assets/output.xlsx'
blank = Image.open('./assets/blank.jpeg')
greenest = Image.open('./assets/planet-earth.png')
cheapest = Image.open('./assets/decrease.png')
shortest = Image.open('./assets/chronometer.png')
bg = Image.open('./assets/background.jpg')
plane = Image.open('./assets/plane.png')

st.title('ZeroCarbonFly')
st.subheader('ZeroCarbonFly is a supporting tool for sustainable travel. Our website guides you to a green flight and visualizes your effort on Zero Carbon action.')
st.info('Climate change has become a crucial issue in contemporary society. The US has pledged to achieve carbon neutrality by 2050, with a 2030 emissions target to be announced shortly. To meet the 2015 Paris Agreement, global greenhouse gas emissions need to be cut by 25– 50% over the next decade. According to the U.S. Greenhouse Gas Emissions and Sinks report by EPA, the primary source of greenhouse gas emissions in the United States is Transportation, which composed 29 percent of 2019 greenhouse gas emissions. Among all the travel patterns, air travel is the fastest-growing source of carbon emissions and emits the largest greenhouse gas. ')
st.image(bg)
airport_code = df_airport['iata_code'].tolist()
airport_code = [x for x in airport_code if pd.isnull(x) == False]
class_list = ['Economy', 'Business', 'Premium', 'First']

st.sidebar.title('Find flights:')
departure_airport_code = st.sidebar.selectbox('Departure Airport', airport_code)
arrival_airport_code = st.sidebar.selectbox('Arrival Airport', airport_code)
date = st.sidebar.date_input('Flight Date')
class_type = st.sidebar.selectbox('Class Type', class_list)
num_of_pax = st.sidebar.slider('Number of Passengers', min_value=1, max_value=10)
carry_on_bag_number = st.sidebar.selectbox('Carry-on Bags', [0,1])
checked_bag_number = st.sidebar.selectbox('Checked Bags', [0,1,2])


date = pd.to_datetime(date)
day = str(date.day)
month= str(date.month)
year= str(date.year)


df = pd.read_excel(output)
df = df.sort_values(by=['price'])
least_cost = df.iloc[0].to_numpy()
df = df.sort_values(by=['carbon'])
least_carbon = df.iloc[0].to_numpy()
df = df.sort_values(by=['duration'])
least_duration = df.iloc[0].to_numpy()


def metrics(array):
    col1.caption('Book Now')
    col2.metric("Carbon (kg)", str(array[16]))
    col3.metric("Price (USD)", str(array[14]))
    col4.metric("Duration (hr, min)", str(array[13]))

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

# LOADING DATA
DATE_TIME = "date/time"
DATA_URL = (
    "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data(100000)

# CREATING FUNCTION FOR MAPS

def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["lon", "lat"],
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ]
    ))
la_guardia= [40.7900, -73.8700]
jfk = [40.6650, -73.7821]
newark = [40.7090, -74.1805]
zoom_level = 12
midpoint = (np.average(data["lat"]), np.average(data["lon"]))



if st.sidebar.button('Submit'):
    with st.spinner('Finding flights...'):
        #df = kayak.kayak_tickets(departure_airport_code,arrival_airport_code,month,day,year,class_type,carry_on_bag_number,checked_bag_number)
        #df = kayak.kayak_tickets("SEA","LAX","12","15","2021","business",1,0)
        st.balloons()
        #st.dataframe(df)
        #st.header('Test')
        st.header('Flight Options')
        st.write('For your flight from SEA to LAX on 12-15-2021 for 1 business class ticket(s) with 1 carry on bag and 0 checked bags:')
        col1, col2, col3, col4 = st.columns(4)
        col1.image(blank, caption=None, width=None, use_column_width='auto')
        col2.image(greenest, caption=None, width=None, use_column_width='auto')
        col3.image(cheapest, caption=None, width=None, use_column_width='auto')
        col4.image(shortest, caption=None, width=None, use_column_width='auto')
        col1.text('\n \n \n \n \n \n \n')
        col1.text('')
        col1.subheader('Greenest')
        #col1.caption('Book Now')
        metrics(least_carbon)
        col1.subheader('Cheapest')
        #col1.caption('Book Now')
        metrics(least_cost)
        col1.subheader('Shortest')
        #col1.caption('Book Now')
        metrics(least_duration)
        st.header('Visualization')
        st.write("**Emissions (kg CO2) by Price ($)**")
        c = alt.Chart(df).mark_circle().encode(
            x='price', y='carbon', size='duration', color='duration', tooltip=['price', 'carbon', 'duration','carrier'])
        st.altair_chart(c, use_container_width=True)
        row2_3, row2_4 = st.columns(2)
        with row2_3:
            st.write("**Arrival Airport**")
            map(data, jfk[0],jfk[1], zoom_level)

        with row2_4:
            st.write("**Destination Airport**")
            map(data, newark[0],newark[1], zoom_level)

       





#!/usr/bin/env python
# coding: utf-8

filename_airport = 'assets/airports.csv'
filename_aircraft = 'assets/aircraft.csv'
output = './output.xlsx'

import pandas as pd
df_airport = pd.read_csv(filename_airport)
df_airport.head()


df_aircraft = pd.read_csv(filename_aircraft)
df_aircraft.head()


def get_airport_lat_long(df,airport_code):
    mask = df['iata_code']==airport_code.upper()
    lat  = df.loc[mask]['latitude_deg'].values[0]
    long = df.loc[mask]['longitude_deg'].values[0]
    return lat,long



def get_aircraft_info(df,aircraft_type):
    mask = df['Model']==aircraft_type
    fuleburn  = float(df.loc[mask]['Fuel burn(kg/km)'].values[0])
    num_of_seats = int(df.loc[mask]['Seats'].values[0])
    return fuleburn,num_of_seats



import math
def get_great_circle_distance(dept_lat,dept_long,arrival_lat, arrival_long):
    x1 = math.radians(dept_lat)
    y1 = math.radians(dept_long)
    x2 = math.radians(arrival_lat)
    y2 = math.radians(arrival_long)
    
    angle = math.degrees(math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)))
    
    # Angel times 60 to get nautical miles, then times 1.852 to get km
    distance = 60 * angle * 1.852
    
    return distance



# ICAO's carbon emissions formula. 
def get_co2_emission(fuel_burn,num_of_seats,distance,num_of_pax):
    # Correction to GCD distance
    if distance < 550:
        distance += 50
    elif distance >= 550 and distance <= 5500:
        distance += 100
    else:
        distance += 125
    pax_load_factor =  0.80
    pax_to_freight_factor = 0.85
    # fuel burn: kg/km
    total_fuel = fuel_burn/1000 * distance
    
    co2_per_pax = 3.16 * ( total_fuel * pax_to_freight_factor)/(num_of_seats * pax_load_factor)
    emission = co2_per_pax * num_of_pax
    return emission



departure_airport_code = "LAX"
arrival_airport_code = "SFO"
aircraft='Airbus A320'
num_of_pax = 1

d_lat, d_long= get_airport_lat_long(df_airport,departure_airport_code)
a_lat, a_long= get_airport_lat_long(df_airport,arrival_airport_code)
distance = get_great_circle_distance(d_lat,d_long,a_lat,a_long)

fuel_burn, num_of_seats=get_aircraft_info(df_aircraft,aircraft)

get_co2_emission(fuel_burn,num_of_seats,distance,num_of_pax)


import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import kayak

st.title('Zero-Carbon Travel')

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

from selenium import webdriver
from bs4 import BeautifulSoup
import time, datetime
import re

if st.sidebar.button('Submit'):
    with st.spinner('Finding flights...'):
        df = kayak.kayak_tickets(departure_airport_code,arrival_airport_code,month,day,year,class_type,carry_on_bag_number,checked_bag_number)
        #df = kayak.kayak_tickets("SEA","LAX","12","15","2021","business",1,0)
        #df = pd.read_excel(output)
        st.dataframe(df)
    st.success('Done!')





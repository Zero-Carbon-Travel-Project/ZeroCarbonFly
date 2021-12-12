'''
kayak is for crawling the flight information and calculating the carbon emission.
'''

import time
import datetime
import re

import pandas as pd
import math

from selenium import webdriver
from bs4 import BeautifulSoup

def kayak_tickets(
    departure_airport_code,arrival_airport_code,month,day,year,class_type,carry_on_bag_number,checked_bag_number):
    '''
    The function is used to crawl the flight ticket information from Kayak.com.
    The user need to install Chrome on their Windows and use chromedriver.exe as the same time.

    PARAMETERS
    ------
    departure_airport_code: Departure airport IATA code (Capital letters).
    arrival_airport_code: Arrival airport IATA code (Capital letters).
    month: 2-digit integer, such as 07.
    day: 2-digit integer, such as 07.
    year: 4-digit integer, such as 2022.
    class_type: economy, business, premium, first.
    carry_on_bag_number: 0 or 1.
    checked_bag_number: 0 0r 1 or 2.
    '''

    #no picture displayed in Chrome
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    #get the flight url
    root_url = "https://www.kayak.com/flights/"
    request_url = root_url + str(departure_airport_code) + "-" + str(arrival_airport_code) + "/" + str(year) + "-" + str(month) + "-" + str(day) + "/"+ str(class_type) + "?fs=cfc=" + str(carry_on_bag_number) + ";stops=~0;bfc=" + str(checked_bag_number) + "&sort=bestflight_a"

    #start the robot for Chrome and open the url
    bot = webdriver.Chrome(executable_path='assets/chromedriver',chrome_options=chrome_options)
    bot.get(request_url)
    print("open chrome finished")

    #create a new dataframe
    record_time = datetime.datetime.now()
    df = pd.DataFrame(columns=["departure_airport_code","arrival_airport_code","year","month","day","class_type","carry_on_bag_number","checked_bag_number","carrier","aircraft","depart_time","arrival_time","duration","price","record_time"])

    #click the "Show More Results" button until no more flights
    time.sleep(5)
    results = bot.find_elements_by_class_name('Flights-Results-ResultInfo')
    try:
        i = 0
        for i in range(3):
            morebutton = bot.find_element_by_class_name('moreButton')
            morebutton.click()
            time.sleep(10)
            i = i+1
    except: # pylint: disable=W0702
        pass
    time.sleep(10)

    #show details
    results = bot.find_elements_by_class_name('Flights-Results-ResultInfo')
    try:
        for result in results:
            result.click()
            time.sleep(1)
    except: # pylint: disable=W0702
        pass
    time.sleep(5)
    print("click buttoms finished")

    #crawl the whole page
    soup = BeautifulSoup(bot.page_source, 'html5lib')
    flights = soup.find_all("div",class_="resultWrapper")
    print("crawlor finished")

    for flight in flights:
        try:
            carrier = flight.find("div",class_=re.compile("carrier-text")).text.replace("\n","")
            aircraft = flight.find("div",class_=re.compile("aircraft-name")).text.replace("\n","")
            depart_time = flight.find("div",class_=re.compile("departure-row")).find("span",class_=re.compile("time")).text.replace("\n","")
            arrival_time = flight.find("div",class_=re.compile("arrival-row")).find("span",class_=re.compile("time")).text .replace("\n","")
            duration = flight.find("div",class_=re.compile("duration-text")).text.replace("\n","")
            price = flight.find("span", "unit-price").find("span", "").text.replace("\n","")

            record = pd.DataFrame([[departure_airport_code,arrival_airport_code,year,month,day,class_type,carry_on_bag_number,checked_bag_number,carrier,aircraft,depart_time,arrival_time,duration,price,record_time]],columns=["departure_airport_code","arrival_airport_code","year","month","day","class_type","carry_on_bag_number","checked_bag_number","carrier","aircraft","depart_time","arrival_time","duration","price","record_time"])
            df = df.append(record)
        except: # pylint: disable=W0702
            pass
    #clean the aircraft column
    df['aircraft'] = df['aircraft'].str.partition("/").loc[:,0].str.partition("(")[0]
    print("all finished")
    return df

def get_great_circle_distance(dept_lat_long,arrival_lat_long):
    x1 = math.radians(dept_lat_long[0])
    y1 = math.radians(dept_lat_long[1])
    x2 = math.radians(arrival_lat_long[0])
    y2 = math.radians(arrival_lat_long[1])
    angle = math.degrees(math.acos(math.sin(x1)*math.sin(x2)+math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))) 
    # Angel times 60 to get nautical miles, then times 1.852 to get km
    distance = 60 * angle * 1.852 
    return distance

# ICAO's carbon emissions formula. 
def get_co2_emission(fuel_burn,num_of_seats,distance,num_of_pax=1):
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
    total_fuel = fuel_burn * distance
    co2_per_pax = 3.16 * ( total_fuel * pax_to_freight_factor)/(num_of_seats * pax_load_factor)
    # kg carbon
    emission = co2_per_pax * num_of_pax
    return emission

def get_distance_from_df(df_row):
    dept_lat_long = df_row['arrival Airport lat long']
    arrival_lat_long =df_row['departure Airport lat long'] 
    distance=get_great_circle_distance(dept_lat_long,arrival_lat_long)
    return distance

def get_co2_emission_from_df(df_row):
    fuel_burn =df_row['fuelburn']
    distance = df_row['distance']
    num_of_seats=df_row['seats']
    emission= get_co2_emission(fuel_burn,num_of_seats,distance)
    return emission

# Raise sea level in inches
def cvt_sea_lvl(df_row):
    emission = df_row[['emission']].values[0]
    return emission*5.42*(10**(-3))

# Lit eiffel tower in hours
def cvt_lit_eiffel_tower(df_row):
    emission = df_row[['emission']].values[0]
    return emission*0.338

def crawl_and calculate(departure_airport_code,arrival_airport_code,month,day,year,class_type,carry_on_bag_number,checked_bag_number):
    df_data_in = kayak_tickets(departure_airport_code,arrival_airport_code,month,day,year,class_type,carry_on_bag_number,checked_bag_number)
    filename_airport = './airports.csv'
    filename_aircraft = './aircraft.csv'

    df_airport_in = pd.read_csv(filename_airport)
    df_airport_in['lat_long'] = df_airport_in[['latitude_deg','longitude_deg']].apply(tuple, axis=1)
    dict_airport = dict(df_airport_in[['iata_code','lat_long']].values)
    dict_airport = {k: v for k, v in dict_airport.items() if v}

    df_aircraft_in = pd.read_csv(filename_aircraft)
    dict_aircraft_fb = dict(df_aircraft_in[['Model','Fuel burn(kg/km)']].values)
    dict_aircraft_seats = dict(df_aircraft_in[['Model','Seats']].values)

    # Get lat and long for two airports
    df_data_in['arrival Airport lat long'] = df_data_in['arrival_airport_code'].map(dict_airport)
    df_data_in['departure Airport lat long'] = df_data_in['departure_airport_code'].map(dict_airport)

    # Get circle distances
    df_data_in['distance'] = df_data_in.apply(get_distance_from_df,axis=1).astype(float)
    # Get fuel burn and num of seats
    df_data_in['aircraft'] = df_data_in['aircraft'].str.strip()
    df_data_in['fuelburn'] = df_data_in['aircraft'].map(dict_aircraft_fb).astype(float)
    df_data_in['seats'] = df_data_in['aircraft'].map(dict_aircraft_seats).astype(float)
    # Get emission
    df_data_in['emission'] = df_data_in.apply(get_co2_emission_from_df,axis=1)
    df_data_in['sea_lvl_inches'] = df_data_in.apply(cvt_sea_lvl,axis=1)
    df_data_in['lit_eiffel_tower_hrs'] = df_data_in.apply(cvt_lit_eiffel_tower,axis=1)
    return df_data_in

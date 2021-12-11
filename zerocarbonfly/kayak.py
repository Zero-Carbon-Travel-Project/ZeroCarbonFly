'''
kayak is for crawling the flight information and calculating the carbon emission.
'''

import time
import datetime
import re

import pandas as pd

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

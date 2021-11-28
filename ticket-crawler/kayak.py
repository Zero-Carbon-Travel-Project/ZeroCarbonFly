def kayak_tickets(departure_airport_code,arrival_airport_code,month,day,year,class_type,carry_on_bag_number,checked_bag_number):
    
    from selenium import webdriver
    from bs4 import BeautifulSoup
    
    #import pandas as pd
    #import numpy as np
    #import requests as rq

    import time, datetime#, json
    import re

    root_url = "https://www.kayak.com/flights/"
    request_url = root_url + str(departure_airport_code) + "-" + str(arrival_airport_code) + "/" + str(year) + "-" + str(month) + "-" + str(day) + "/"+ str(class_type) + "?fs=cfc=" + str(carry_on_bag_number) + ";stops=~0;bfc=" + str(checked_bag_number) + "&sort=bestflight_a"
    file_name = str(departure_airport_code) + str(arrival_airport_code) + str(year) + str(month) + str(day) + str(class_type) + str(carry_on_bag_number) + str(checked_bag_number) 

    bot = webdriver.Chrome(executable_path='assets/chromedriver.exe')
    bot.get(request_url)

    f = open("assets/"+file_name+".csv", "a", encoding="utf-8") 
    f.write("carrier,aircraft,depart_time,arrival_time,duration,price,time \n") 
    start = datetime.datetime.now() 

    try:
        for i in range(10):
            moreButton = bot.find_element_by_class_name('moreButton')
            moreButton.click()
            time.sleep(5)
            i = i+1
    except:
        pass

    soup = BeautifulSoup(bot.page_source, 'html5lib')
    flights = soup.find_all("div",class_="resultWrapper") 
    time.sleep(15)

    for flight in flights:
        try:
            carrier = flight.find("div",class_=re.compile("carrier-text")).text.replace("\n","")
            aircraft = flight.find("div",class_=re.compile("-aircraft-name")).text.replace("\n","")
            depart_time = flight.find("div",class_=re.compile("-departure-row")).find("span",class_=re.compile("time")).text.replace("\n","")
            arrival_time = flight.find("div",class_=re.compile("-arrival-row")).find("span",class_=re.compile("time")).text .replace("\n","")
            duration = flight.find("div",class_=re.compile("duration-text")).text.replace("\n","")
            price = flight.find("span","price option-text").find("span", "price-text").text.replace("\n","")

            record = "%s,%s,%s,%s,%s,%s,%s \n" % (carrier,aircraft,depart_time,arrival_time,duration,price,start)
            f.write(record)
        except:
            pass

    f.close()
    #bot.close()
    print("finished")

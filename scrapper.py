from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/exoplane t-catalog/"

browser=webdriver.Chrome("/Users/MY PC/Desktop/C-126/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrap():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"] 
    planet_data = []

    for i in range(0,428):

        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            temp_list=[]
            for index,li_tags in enumerate(li_tags):
                if (index==0):
                    temp_list.append(li_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")
        
                planet_data.append(temp_list)
    
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

    with open("scrapper_2.csv", "w") as f: csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(planet_data)


scrap()
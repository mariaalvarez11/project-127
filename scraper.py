from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/falva/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["proper_name", "distance", "mass", "radius"]
    stars_data = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        for th_tag in soup.find_all("th", attrs={"class", "exoplanet"}):
            tr_tags = ul_tag.find_all("tr")
            temp_list = []

            for index, th_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(tr_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tags.contents[0])
                    except:
                        temp_list.append("")

            stars_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        
    with open("scraper2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)
scrape()

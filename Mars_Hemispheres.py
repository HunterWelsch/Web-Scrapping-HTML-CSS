# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd 
import datetime as dt
from datetime import datetime

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)

# Visit URL
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

#Get Cerberus Hemisphere image
# Visit cerberus hemisphere site
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
browser.visit(url)

#delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

# Find and click the full image button
full_image_elem = browser.find_by_id('wide-image-toggle')
full_image_elem.click()

# Find and save Cerberus Hemisphere image url
img_url_cerberus = img_soup.select_one('img.wide-image').get("src")
img_url_cerberus

# Find and save hemisphere title 
cerberus_title = img_soup.find("h2", class_='title').get_text()
cerberus_title

#Get Schiaparelli Hemisphere image
# Visit Schiaparelli Hemisphere site
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
browser.visit(url)

#delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

# Find and click the full image button
full_image_elem = browser.find_by_id('wide-image-toggle')
full_image_elem.click()

# Find and save Schiaparelli Hemisphere image url
img_url_schiaparelli = img_soup.select_one('img.wide-image').get("src")
img_url_schiaparelli

# Find and save hemisphere title 
schiaparelli_title = img_soup.find("h2", class_='title').get_text()
schiaparelli_title

#Get Syrtis Major Hemisphere image
# Visit Syrtis Major Hemisphere site
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
browser.visit(url)

#delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

# Find and click the full image button
full_image_elem = browser.find_by_id('wide-image-toggle')
full_image_elem.click()

# Find and save Syrtis Major image url
img_url_syrtismajor = img_soup.select_one('img.wide-image').get("src")
img_url_syrtismajor

# Find and save hemisphere title 
syrtismajor_title = img_soup.find("h2", class_='title').get_text()
syrtismajor_title

#Get Valles Marineris Hemisphere image
# Visit Valles Marineris Hemisphere site
url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
browser.visit(url)

#delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')

# Find and click the full image button
full_image_elem = browser.find_by_id('wide-image-toggle')
full_image_elem.click()

# Find and save Valles Marineris image url
img_url_vallesmarineris = img_soup.select_one('img.wide-image').get("src")
img_url_vallesmarineris

# Find and save hemisphere title 
vallesmarineris_title = img_soup.find("h2", class_='title').get_text()
vallesmarineris_title
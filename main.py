from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from time import sleep

# ------------------------ Scraping data -----------------------------------------
zillow_link = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(zillow_link)
zillow_page = response.text

soup = BeautifulSoup(zillow_page, "html.parser")
listing_list = soup.find_all(class_="StyledPropertyCardDataArea-anchor")
displayed_prices = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")

links = []
addresses = []
for listing in listing_list:
    links.append(listing.get("href"))
    addresses.append(listing.text.replace("|","").strip())

prices = []
for price in displayed_prices:
    clean_price = price.text
    clean_price = clean_price.replace("1 bd","")
    clean_price = clean_price.replace("1bd", "")
    clean_price = clean_price.replace("/mo", "")
    clean_price = clean_price.replace("+", "")
    prices.append(clean_price)

# ------------------------ Adding to form -----------------------------------------

form_link = "https://docs.google.com/forms/d/e/1FAIpQLSeM1aN5eCAi8uTrcokizjbBUESXgavyLk8RNtEP33N0y-P7bA/viewform?usp=sf_link"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(form_link)

# property_address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# price_per_month = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
# link_to_property = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
# submit_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

for i in range(len(links)):
    sleep(1)

    property_address = driver.find_element(By.XPATH,
                                           value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_per_month = driver.find_element(By.XPATH,
                                          value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_to_property = driver.find_element(By.XPATH,
                                           value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    property_address.click()
    property_address.send_keys(addresses[i])
    price_per_month.click()
    price_per_month.send_keys(prices[i])
    link_to_property.click()
    link_to_property.send_keys(links[i])
    submit_button.click()

    repeat_button = driver.find_element(By.XPATH,
                                        value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    repeat_button.click()

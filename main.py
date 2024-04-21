from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

form_link = "https://docs.google.com/forms/d/e/1FAIpQLSeM1aN5eCAi8uTrcokizjbBUESXgavyLk8RNtEP33N0y-P7bA/viewform?usp=sf_link"
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

# print(links)
# print(addresses)
# print(prices)

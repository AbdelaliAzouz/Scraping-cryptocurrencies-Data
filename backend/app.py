from flask import (
    Flask,
    render_template)

from unittest import result
import requests 
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

#MongoDB libraries
import pymongo
import pandas as pd 
import json


########Minimal flask app#########
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
##################################


coin_name = []
ticker = []
price = []
percentage = []
market_cap = []
total_coin = []

#def extract(page):
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36"}
url = f"https://www.worldcoinindex.com/"
r = requests.get(url,headers)                       #get the page attributes (code HTML)
soup = BeautifulSoup(r.content, "html.parser")      #Create soup object to parse content
    #return soup

coin_names = soup.find_all("td", {"class":"bitcoinName"})
tickers = soup.find_all("td", {"class":"ticker"})
prices = soup.find_all("td", {"class":"number pricekoers lastprice"})
percentages = soup.find_all("td", {"class":"percentage"})
market_caps = soup.find_all("td", {"class":"marketcap"})
total_coins = soup.find_all("td", {"class":"supply"})

file_list = [coin_name, ticker, price, percentage, market_cap, total_coin]
exported = zip_longest(*file_list)
for i in range(len(coin_names)):
    coin_name.append(coin_names[i].text.strip())
    ticker.append(tickers[i].text.strip())
    price.append(prices[i].text)
    percentage.append(percentages[i].text)
    market_cap.append(market_caps[i].text)
    total_coin.append(total_coins[i].text)

print(coin_name)
print("****************")
print(ticker)

#Save values into csv file : put it inside a function
with open("D:/MST/S2/NoSQL/Projet fin de module/Scrape cryptocurrencies Data/backend/coines_infos.csv","w", newline="") as myfile:
     wr = csv.writer(myfile)
     wr.writerow(["coin Name","ticker","price","percentage","market_cap","total_coin"])
     wr.writerows(exported)


#put it inside a function
client = pymongo.MongoClient("mongodb://localhost:27017")
df = pd.read_csv("coines_infos.csv")
data = df.to_dict(orient="records")
db = client["FlaskData"]
db.CryptoData.insert_many(data)

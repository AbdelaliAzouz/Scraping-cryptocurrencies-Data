import requests#pour aller chercher l'URL  
from bs4 import BeautifulSoup#pour le parsing
import csv#pour stocker le scrape dans un fichier csv
from itertools import zip_longest#pour faire binder chaque ligne avec colonne
import pymongo

def scrape_mongo():
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Safari/537.36"}
    url = f"https://www.worldcoinindex.com/"
    r = requests.get(url,headers)                        #get the page attributes (code HTML)
    soup = BeautifulSoup(r.content, "html.parser")  #Create soup object to parse content 
    coin_name = []
    ticker = []
    price = []
    percentage = []
    market_cap = []
    total_coin = []
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
        price.append(prices[i].text.strip('$'))
        percentage.append(percentages[i].text.strip('%'))
        market_cap.append(market_caps[i].text)
        total_coin.append(total_coins[i].text)

    with open("D:/NOSQL_PROJECT/backend/coines_infos.csv","w", newline="") as myfile:
        wr = csv.writer(myfile)
        wr.writerow(["coin Name","ticker","price","percentage","market_cap","total_coin"])
        wr.writerows(exported)

    filename ="coines_infos.csv"
    currencies = []

    with open(filename, 'r') as data:
        
        for line in csv.DictReader(data):
            currencies.append(line)

    client = pymongo.MongoClient('localhost:27017')
    db = client.scrape.crypto
    try:
        db.insert_many(currencies)
        print(f'inserted {len(currencies)} crypto')
    except:
        print('an error occurred crypto data were not stored to db')

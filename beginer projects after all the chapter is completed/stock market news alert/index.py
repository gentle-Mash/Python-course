import requests
import smtplib
import os

EMAIL = "practicecode254@gmail.com"
app_pass = "zbrrchnvyowtarrf"



API_KEY_STOCK = "HIJYEI5BDR2G9VQX"
API_KEY_NEWS = "d73023ce6cd94f868a994db99ed25cdf"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

Stock_Endpoint = "https://www.alphavantage.co/query"
News_Endpoint = "https://newsapi.org/v2/everything"

parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : API_KEY_STOCK
}

response = requests.get(Stock_Endpoint, params=parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]

close_stock_data = [value["4. close"] for (key, value) in data.items()]
# print(data.keys())
# print(close_stock_data)

yesterday_closing_price = close_stock_data[0]
day_before_yesterday_closing_price = close_stock_data[1]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
difference_percentage = round(float(difference/float(yesterday_closing_price))*100)
# print(round(difference_percentage))

up_down = None
if difference > 0:
    up_down = "⬆"
else:
    up_down = "⬇"

if abs(difference_percentage) > 5:
    news_parameters = {
        "apiKey" : API_KEY_NEWS,
        "q" : COMPANY_NAME
    }

    news_response = requests.get(News_Endpoint, params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()["articles"]
    three_articles = news_data[0:3]
    # print(three_articles)

    news = [f"{STOCK_NAME} {difference_percentage}%{up_down}  Headline: {item['title']}\nBrief: {item['description']}" for item in three_articles]
    # print(news)
    
    for item in news:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=app_pass)
            connection.sendmail(from_addr=EMAIL, to_addrs="practicecode254@gmail.com", msg=f"Subject:Breaking News\n\n{item}".encode('utf-8'))


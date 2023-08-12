from bs4 import BeautifulSoup
import smtplib
import requests
import lxml

header = {
    "Accept-Language" : "en-US,en;q=0.9",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get("https://www.amazon.com/Panasonic-Compact-Microwave-Cooking-Popcorn/dp/B07PML2DC6/ref=sr_1_4?keywords=micro+oven+for+kitchen&qid=1691370730&sprefix=micro+ove%2Caps%2C510&sr=8-4", headers=header)
response.raise_for_status()
# print(response.text)

soup = BeautifulSoup(response.text, "lxml")
spans = soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay")

# soup2 = BeautifulSoup(spans, "lxml")
print(int(spans.span.getText().split("$")[1]))
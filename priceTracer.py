import requests
from bs4 import BeautifulSoup
class PriceTracer:
    def __init__(self, url):
        self.url= url
        self.user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
        self.response = requests.get(url= self.url, headers= self.user_agent).text
        self.soup = BeautifulSoup (self.response,"html.parser")
    def product_title(self):
        title = self.soup.find("span",{"id" : "productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag Not Found"
    def product_price(self):
        price = self.soup.find("span",{"class" : "a-price-whole"})
        if price is not None:
            return price.text.strip()
        else:
            return "Tag Not Found"
device = PriceTracer (url="https://www.amazon.in/Samsung-Galaxy-Storage-6000mAh-Battery/dp/B0B4F2TTTS/ref=sr_1_3?crid=3E1HRUFUHK4MM&keywords=phones&qid=1698301879&sprefix=phones%2Caps%2C276&sr=8-3")
print (device.product_title())
print (device.product_price())
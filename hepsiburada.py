from cgitb import text
from bs4 import BeautifulSoup
import requests
import asyncio

#https://www.trendyol.com/sr?q=
#
headers= {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}


class web():
    urls = []
    productInfo = []

    def __init__(self,product,page):
        self.product = product
        self.page = page

    def getProduct(self):
        global headers
        productPage = (f'{self.page}{self.product}')
        head = requests.get(productPage, headers=headers)
        soup = BeautifulSoup(head.content, 'html.parser')
        products = soup.findAll("ul", {"class": "productListContent-wrapper"})
        for product in products:
            for link in product.select(".productListContent-item a"):
                endpoint = link["href"]
               
                web.urls.append('https://www.hepsiburada.com' + endpoint)
        
        for i in web.urls:
            req = requests.get(i, headers=headers)
            soup1 = BeautifulSoup(req.content, 'html.parser')

            getName = soup1.find("h1", attrs={'class',"product-name best-price-trick"})
            rating = soup1.find('span', attrs={'class', "rating-star"})
            
            getPrice = soup1.select('''span[data-bind="markupText:'currentPriceBeforePoint'"]''')
            
        
            print(getName.text.strip())
            print(getPrice[0].getText())
            if(rating):
                print(rating.text)
            else:
                print("Rating Yok")

            
            

        

    
    


hepsiBurada = web(product='kale',page='https://www.hepsiburada.com/ara?q=')




hepsiBurada.getProduct()






        

        

        

    
    


hepsiBurada = web(product='computer',page='https://www.hepsiburada.com/ara?q=')




hepsiBurada.getProduct()








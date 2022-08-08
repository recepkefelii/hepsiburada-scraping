from bs4 import BeautifulSoup
import requests

headers= {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

class web():
    products = []

    def __init__(self,product,page, filters):
        self.product = product
        self.page = page
        self.filters = filters

    def getProduct(self):
        global headers
        productPage = f'{self.page}{self.product}&filtreler={self.filters}'
        head = requests.get(productPage, headers=headers)
        soup = BeautifulSoup(head.content, 'html.parser')
        products = soup.findAll("ul", {"class": "productListContent-wrapper"})

        for product in products:
            for aTag in product.select(".productListContent-item a"):
                productSchema = {
                    "name" : None,
                    "price" : None,
                    "rates" : [],
                    "ratingCount" : "The product hasn't rating",
                    "productImage" : None,
                    "productURL" : None
                }
                print("----------------------------------------------------------------------------------------------")
                productSchema["name"] = aTag.select("a div:last-child h3")[0].text
                productSchema["price"] = aTag.select("a div:last-child div div[data-test-id='price-current-price']")[0].text
                productSchema["productURL"] = f"https://www.hepsiburada.com/{aTag['href']}"
                productSchema["productImage"] = aTag.select("img[src^='https://productimages']")[0]["src"]
                if len(aTag.select("div[data-test-id = 'review'] div:last-child"))>0:
                    productSchema["ratingCount"] = aTag.select("div[data-test-id = 'review'] div:last-child")[0].text

                for rate in aTag.select("a li[class^='moria-ProductCard'] div"):
                    productSchema["rates"].append(rate["width"])

                print(productSchema)
                self.products.append(productSchema)
                    

hepsiBurada = web(product='salıncak',page='https://www.hepsiburada.com/ara?q=', filters="fiyat:100-200")

hepsiBurada.getProduct()








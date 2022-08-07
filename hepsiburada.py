
from bs4 import BeautifulSoup
import requests




headers= {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
# bu kisim sizde calismazsa kendinize gore degisin

class web(): # web isminde bir class olusturuyorum
    urls = []
    productInfo = []

    def __init__(self,product,page): # selfime product,page parametlerini ekliyorum
        self.product = product
        self.page = page

    def getProduct(self): # web classın altinda getProduct adli bir fonksiyon olusturdum
        global headers
        productPage = (f'{self.page}{self.product}')
        head = requests.get(productPage, headers=headers) # olusturdugumuz headers burda kullaniyoruz
        soup = BeautifulSoup(head.content, 'html.parser') # html.parse ile parse ediyoruz
        products = soup.findAll("ul", {"class": "productListContent-wrapper"})
        for product in products:
            for link in product.select(".productListContent-item a"): # https://www.hepsiburada.com/ara?q= linkinden sonra gelicek olan urun ismini ariyoruz
                endpoint = link["href"]
               
                web.urls.append('https://www.hepsiburada.com' + endpoint) # burdada ekliyoruz urun ismini linkiminiz sonuna
        
        for i in web.urls: # bu bolumde aldıgımız linklerin icine girip fiyat rating ve isimlerini cekiyoruz
            req = requests.get(i, headers=headers)
            soup1 = BeautifulSoup(req.content, 'html.parser')

            getName = soup1.find("h1", attrs={'class',"product-name best-price-trick"})
            rating = soup1.find('span', attrs={'class', "rating-star"})
            
            getPrice = soup1.select('''span[data-bind="markupText:'currentPriceBeforePoint'"]''')
            
        
            print(getName.text.strip())
            print(getPrice[0].getText())
            if(rating): # rating degeri none gelirse rating degeri yok yazmasini sagliyoruz
                print(rating.text)
            else:
                print("Rating Yok")

            
            

        

    
    


hepsiBurada = web(product='kale',page='https://www.hepsiburada.com/ara?q=') # son kisim da ise self olusturup product ve page parametlerine deger veriyoruz




hepsiBurada.getProduct() # fonksiyonu cagırıyoruz






        

        

        

    
    


hepsiBurada = web(product='computer',page='https://www.hepsiburada.com/ara?q=')




hepsiBurada.getProduct()








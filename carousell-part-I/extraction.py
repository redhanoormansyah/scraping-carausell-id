import csv
import requests
from bs4 import BeautifulSoup
html_doc = requests.get('https://id.carousell.com/categories/health-and-beauty-11/')
soup = BeautifulSoup(html_doc.text, 'html.parser')

beuty_populer = soup.find(attrs={'class':'_2RJeLsMmpi'})
file = open('result-beutty-populer-extraction.csv','w', newline='')
writer= csv.writer(file)
headers = ['Nama Toko', 'Nama Produk','Harga', 'Deskripsi Produk']
writer.writerow(headers)

titles = beuty_populer.findAll(attrs={'class':'TpQXuJG_eo'})
for title in titles:
    #Nama Toko
    toko = (title.find('p',attrs={'class': '_1gJzwc_bJS _2NNa9Zomqk Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)
    # Nama Barang
    barang=(title.find('p',attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)
     # Harga
    harga=(title.find('p',attrs={'class': '_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6'}).text)
    #     Deskripsi Barang
    deskripsi=(title.find('p',attrs={'class': '_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _30RANjWDIv'}).text)
    # Img
    image=(title.find('span',attrs={'class':'_3nH6adLACP _3k9K3fuPdS _14ECgRVNZW'}).find('img')['src'])
    print(image)
    
    with open('images/'+ barang + '.jpg','wb') as f:
        img = requests.get(image)
        f.write(img.content)
    
    file = open('result-beutty-populer-extraction.csv','a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([toko, barang, harga, deskripsi])
file.close()





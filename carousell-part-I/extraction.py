import csv
import requests
from bs4 import BeautifulSoup
html_doc = requests.get('https://id.carousell.com/categories/health-and-beauty-11/')
# html_doc = requests.get('https://sukabumikab.sipd.kemendagri.go.id/daerah/main/plan/asmas/2022/22/0')
# print(html_doc.text)
soup = BeautifulSoup(html_doc.text, 'html.parser')

beuty_populer = soup.find(attrs={'class':'_2RJeLsMmpi'})
# print(beuty_populer)

file = open('result-beutty-populer-extraction.csv','w', newline='')
writer= csv.writer(file)
headers = ['Nama Toko', 'Nama Produk','Harga']
writer.writerow(headers)


titles = beuty_populer.findAll(attrs={'class':'TpQXuJG_eo'})
for title in titles:
    #Nama Toko
    toko = (title.find('p',attrs={'class': '_1gJzwc_bJS _2NNa9Zomqk Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)
    # Nama Barang
    barang=(title.find('p',attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)
     # Harga
    harga=(title.find('p',attrs={'class': '_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6'}).text)

    file = open('result-beutty-populer-extraction.csv','a', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow([toko, barang, harga])
    file.close()





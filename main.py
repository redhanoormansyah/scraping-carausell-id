
import requests
from bs4 import BeautifulSoup
html_doc = requests.get('https://id.carousell.com/categories/health-and-beauty-11/')
# html_doc = requests.get('https://sukabumikab.sipd.kemendagri.go.id/daerah/main/plan/asmas/2022/22/0')
# print(html_doc.text)
soup = BeautifulSoup(html_doc.text, 'html.parser')

beuty_populer = soup.find(attrs={'class':'_2RJeLsMmpi'})
# print(beuty_populer)





titles = beuty_populer.findAll(attrs={'class':'TpQXuJG_eo'})
for title in titles:
    # Nama Barang
    print(title.find('p',attrs={'class':'_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz uxIDPd3H13 _30RANjWDIv'}).text)
    # Img
    print(title.find('span',attrs={'class':'_3nH6adLACP _3k9K3fuPdS _14ECgRVNZW'}).find('img')['src'])
    # Harga
    print(title.find('p',attrs={'class': '_1gJzwc_bJS _2rwkILN6KA Rmplp6XJNu mT74Grr7MA nCFolhPlNA lqg5eVwdBz _19l6iUes6V _3k5LISAlf6'}).text)






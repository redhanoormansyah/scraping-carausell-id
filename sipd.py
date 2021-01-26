import requests
from bs4 import BeautifulSoup
html_doc = requests.get('https://sukabumikab.sipd.kemendagri.go.id/daerah/main/plan/asmas/2022/22/0')
soup = BeautifulSoup(html_doc.text, 'html.parser')
print(soup)
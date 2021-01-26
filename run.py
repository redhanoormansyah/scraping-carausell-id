import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def home():
    return render_template('input.html')

@app.route('/beuty-populer')
def beuty_populer():

    html_doc = requests.get('https://id.carousell.com/categories/health-and-beauty-11/')
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    beuty_populer = soup.find(attrs={'class': '_2RJeLsMmpi'})
    titles = beuty_populer.findAll(attrs={'class': 'TpQXuJG_eo'})
    
    return render_template('input.html',titles=titles)


if __name__ == '__main__':
    app.run(debug=True)
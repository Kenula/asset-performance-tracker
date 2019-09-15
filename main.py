from bs4 import BeautifulSoup
import requests
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage

# loads the webpage to allow for scraping
class Client(QWebPage):
    
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec()
    
    def on_page_load(self):
        self.app.quit()
        
url = 'https://iaclarington.com/en/price-performance/fund?fund_id=4201&series=4401'
client_response = Client(url)
source = client_response.mainFrame().toHtml()


# source = requests.get('https://iaclarington.com/en/price-performance/fund?fund_id=4201&series=4401').text

soup = BeautifulSoup(source, 'lxml')

main = soup.find('div', class_='main-content')
# print(main.prettify())
fund_value = main.find('div', id='fundValue').text
print(fund_value)

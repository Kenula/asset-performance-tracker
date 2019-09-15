from bs4 import BeautifulSoup
import requests
import sys
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebPage
import csv

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

# handling the csv file
csv_file = open('performance.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Value', 'Performance Date', 'Performance (1mo)', 'Performance (3mo)'])


# source = requests.get('https://iaclarington.com/en/price-performance/fund?fund_id=4201&series=4401').text

soup = BeautifulSoup(source, 'lxml')

main = soup.find('div', class_='main-content')
# print(main.prettify())
fund_name = main.find('h3', id='fundName').text
fund_value = main.find('div', id='fundValue').text
unformatted_date = main.find('div', id='perf-date').text
perf_date = unformatted_date.split(' ')[3]
perf_1mo = main.find('td', id='fp1MO').text
perf_3mo = main.find('td', id='fp3MO').text

print(fund_name)
print(fund_value)
print(perf_date)
print(perf_1mo)
print(perf_3mo)

csv_writer.writerow([fund_name, fund_value, perf_date, perf_1mo, perf_3mo])
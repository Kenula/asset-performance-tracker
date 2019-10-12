from bs4 import BeautifulSoup
from requests_html import HTMLSession
import csv

urls = ['https://iaclarington.com/en/price-performance/fund?fund_id=4201&series=4401',
        'https://iaclarington.com/en/price-performance/fund?fund_id=4303&series=7400',
        'https://iaclarington.com/en/price-performance/fund?fund_id=4509',
        'https://iaclarington.com/en/price-performance/fund?fund_id=4215']

# loads the webpage to allow for scraping
session = HTMLSession()


# handling the csv file
csv_file = open('performance.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "Value", "Performance Date", "Performance (1mo)", "Performance (3mo)"])
# csv_writer.writerow('\n')


# source = requests.get('https://iaclarington.com/en/price-performance/fund?fund_id=4201&series=4401').text



for url in urls:
    print(url)
    response = session.get(url)
    response.html.render()

    soup = BeautifulSoup(response.html.html, 'lxml')

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


csv_file.close()
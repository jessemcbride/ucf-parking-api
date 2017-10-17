import math
import urllib2

from bs4 import BeautifulSoup

url = 'http://secure.parking.ucf.edu/GarageCount/'


def scrape():
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'html.parser')
    rows = soup.find_all('tr', class_='dxgvDataRow_DevEx')

    garages = []

    for row in rows:
        data = row.find_all(class_='dxgv')

        garage = data[0].text.replace('Garage ', '')
        available, total = tuple(map(int, data[1].text.strip().split('/')))
        percentage = math.floor(100 - (float(available) / float(total)) * 100)

        garages.append(
            {
                'name': garage,
                'available': available,
                'total': total,
                'percentage': percentage
            }
        )

    return garages

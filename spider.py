from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def main():
    url = 'https://en.wikipedia.org/wiki/Local_government_areas_of_Nigeria'
    html = urlopen(url)
    bs_obj = BeautifulSoup(html, 'html.parser')

    table = bs_obj.find('table', attrs={'class':'wikitable'})
    rows = table.find_all('tr')

    for row in rows:
        for col in row.find_all(['td','th']):
            print(col.get_text())
    
        print('-'*10)

if __name__ == '__main__':
    main()

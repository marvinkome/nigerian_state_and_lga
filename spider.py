from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def main():
    url = 'https://en.wikipedia.org/wiki/Local_government_areas_of_Nigeria'
    html = urlopen(url)
    bs_obj = BeautifulSoup(html, 'html.parser')

    states = set()
    d = {}
    table = bs_obj.find('table', attrs={'class':'wikitable'})
    rows = table.find_all('tr')

    for row in rows:
        cols = row.find_all(['td','th'])
        states.add(cols[1].get_text())

    for state in list(states):
        l = []
        for row in rows:
            cols = row.find_all(['td', 'th'])          
            if cols[1].get_text() == state:
                l.append(cols[0].get_text())
                #print()
        d[state] = l

    print(d)

if __name__ == '__main__':
    main()

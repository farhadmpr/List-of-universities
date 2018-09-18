import requests
from bs4 import BeautifulSoup
import csv

csv_file_path = "c:/app/uni.csv"
data=[['name', 'type', 'province', 'city']]

def read(page):
    r = requests.get('http://msrt.ir/fa/institute?page='+str(page))
    html = r.text.encode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')
    tr_in_tbody = soup.find_all('tbody')[0].find_all('tr')
    for tr in tr_in_tbody:
        td = tr.find_all('td')
        name=td[0].find('a').text
        type=td[1].text
        province=td[2].text
        city=td[3].text
        data.append([name, type, province, city])
    print("Readed page", page)

for i in range(1,152):
    read(i)

writer = csv.writer(open(csv_file_path, 'w', encoding='utf-8', newline=''))
writer.writerow(data)

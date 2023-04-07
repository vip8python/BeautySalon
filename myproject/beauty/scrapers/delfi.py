from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.delfi.lt/stilius/grozis/').text
soup = BeautifulSoup(source, 'html.parser')
divas = soup.find('div', class_='C-block-type-102')

links = []
for link in divas.find_all('a'):
    href = link.get('href')
    if href and href not in links and not href.endswith('/diskusija'):
        new_link = 'https://www.delfi.lt' + href
        if new_link not in links:
            links.append(new_link)
            link['href'] = new_link

img_title = []
for img in divas.find_all('img'):
    alt = img.get('alt')
    img_title.append(alt)


img_links = []
for img in divas.find_all('img'):
    src = img.get('src')
    img_links.append(src)

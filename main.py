import requests
from bs4 import BeautifulSoup


def get_html(URL):
    response = requests.get(URL)
    return response.text


URL = 'https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv'
html = get_html(URL)

soup = BeautifulSoup(html, 'html.parser')
content = soup.find('div', {'class':'lister'}).find('tbody', {'class':'lister-list'})
shows = content.find_all('tr')

print('''Most Popular TV Shows
As determined by IMDb Users''')

for i, s in enumerate(shows, start=1):
    title = s.find('td', {'class': 'titleColumn'}).find('a').text
    year = s.find('td', {'class': 'titleColumn'}).find('span').text
    rating = s.find('td', {'class': 'ratingColumn'}).text.strip()
    print(f'{i}) {title} {year} rating: {rating}')
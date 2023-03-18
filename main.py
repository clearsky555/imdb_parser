import requests
from bs4 import BeautifulSoup

from database import TVShowsManager, engine


manager = TVShowsManager(engine=engine)


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


def write_data(data):
    result = manager.insert_show(data)
    return result

def main():
    for i, s in enumerate(shows, start=1):
        title = s.find('td', {'class': 'titleColumn'}).find('a').text
        year = s.find('td', {'class': 'titleColumn'}).find('span').text
        rating = s.find('td', {'class': 'ratingColumn'}).text.strip()
        href = s.find('a').get('href')
        full_url = 'https://www.imdb.com' + href
        print(f'{i}) {title} {year} rating: {rating} link: {full_url}')
        data = {
            'place':i,
            'title':title,
            'year':year,
            'rating':rating,
            'link':full_url
        }
        write_data(data)



if __name__ == '__main__':
    manager.delete_table()
    manager.create_table()
    main()
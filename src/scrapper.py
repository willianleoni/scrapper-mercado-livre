from bs4 import BeautifulSoup
import requests

class MercadoLivreScraper:
    def __init__(self, url):
        self.url = url

    def fetch_page_data(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return BeautifulSoup(response.content, 'html.parser')
            else:
                print(f"Error fetching data from URL: {self.url}, Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Exception occurred while fetching data: {e}")
            return None

    def get_next_page_url(self, soup):
        next_page_tag = soup.find('a', class_='andes-pagination__link', title='Seguinte')
        return next_page_tag['href'] if next_page_tag else None

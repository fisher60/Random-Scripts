from bs4 import BeautifulSoup
import requests


class Scraper:
    def __init__(self, url):
        self.url = url
        self.scraped_data = None

    def __str__(self):
        return str(self.scraped_data.prettify())

    def data_is_current(self):
        return self.scraped_data == True

    def scrape(self):
        self.scraped_data = BeautifulSoup(requests.get(self.url).text, 'lxml')

    def find_tags(self, tag, classes):
        if not self.scraped_data:
            self.scrape()
        return self.scraped_data.find(tag, class_=classes)

    def find_all_tags(self, tag, classes):
        if not self.scraped_data:
            self.scrape()
        return self.scraped_data.find_all(tag, class_=classes)

    def sort_data_from_tags(self, tag, classes):
        dict_data = {}
        to_sort = self.find_all_tags(tag, classes)

        for each in to_sort:
            try:
                dict_data[each.find('div', class_='card-header').h4.strong.text] = each.find('div',
                                                                                             class_='card-body').text
            except Exception as e:
                pass

        return dict_data


test_scrape = Scraper('https://thewizardslair.us/docs.html')

print(test_scrape.sort_data_from_tags('div', 'card'))


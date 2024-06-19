import Util
from bs4 import BeautifulSoup
from Pages.CollectionPage import CollectionPage
import time


class ResultsPage(object):
    def __init__(self, driver, config_data, page_id, page_url, collection_id):
        self.driver = driver
        self.config_data = config_data
        self.page_id = page_id
        self.page_url = page_url
        self.collection_id = collection_id

    def get_page_results(self):
        self.driver.get(self.page_url)
        time.sleep(self.config_data['WAIT_TIME_SMALL'])
        html = self.driver.page_source
        soup = BeautifulSoup(html, parser='html.parser', features="lxml")
        data = soup.findAll("li", class_='SearchModule-results-item')[self.collection_id]

        collection = CollectionPage(
            driver=self.driver,
            config_data=self.config_data,
            page_id=self.page_id,
            collection_id=self.collection_id,
            collection_data=data
        ).get_collection()

        return collection

import time
from typing import List
from bs4 import BeautifulSoup
from selenium import webdriver

from Pages.CollectionPage import CollectionPage
from entities import Collection


class ResultsPage(object):
    def __init__(self, driver: webdriver, config_data: dict, page_id: int, page_url: str) -> None:
        self.driver = driver
        self.config_data = config_data
        self.page_id = page_id
        self.page_url = page_url

    def get_page_results(self) -> List[Collection]:
        self.driver.get(self.page_url)
        time.sleep(self.config_data['WAIT_TIME_SMALL'])
        html = self.driver.page_source
        soup = BeautifulSoup(html, parser='html.parser', features="lxml")
        collections_data = soup.findAll("li", class_='SearchModule-results-item')

        collections = []
        for collection_id, collection_data in enumerate(collections_data):
            collection = CollectionPage(
                driver=self.driver,
                config_data=self.config_data,
                page_id=self.page_id,
                collection_id=collection_id,
                collection_data=collection_data
            ).get_collection()
            collections.append(collection)

        return collections

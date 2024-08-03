import Util
from selenium import webdriver
from bs4 import BeautifulSoup
from Pages import ItemsPage
from entities import Collection


class CollectionPage(object):
    def __init__(self, driver: webdriver, config_data: dict,
                 page_id: int, collection_id: int, collection_data: BeautifulSoup) -> None:
        self.driver = driver
        self.config_data = config_data
        self.page_id = page_id
        self.collection_id = collection_id
        self.collection_data = collection_data

    def get_collection(self) -> Collection:
        category = Util.get_text(self.collection_data, 'div', 'Card-category')
        title = Util.get_text(self.collection_data, 'div', 'Card-title')
        details = Util.get_text(self.collection_data, 'div', 'Card-details')
        price = Util.get_text(self.collection_data, 'div', 'Card-salePrice')
        link = self.collection_data.find('a', class_='Card-info-container')['href']

        items_page = ItemsPage.ItemsPage(self.driver, self.config_data, self.page_id, self.collection_id, link)
        items = items_page.get_collection_items()

        collection = Collection(
            page_id=self.page_id,
            collection_id=self.collection_id,
            category=category,
            title=title,
            details=details,
            price=price,
            link=link,
            items=items
        )
        collection.print()
        return collection

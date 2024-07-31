from Pages import ItemsPage
import Util


class CollectionPage(object):
    def __init__(self, driver, config_data, page_id, collection_id, collection_data):
        self.driver = driver
        self.config_data = config_data
        self.page_id = page_id
        self.collection_id = collection_id
        self.collection_data = collection_data

    def get_collection(self):
        category = Util.get_text(self.collection_data, 'div', 'Card-category')
        title = Util.get_text(self.collection_data, 'div', 'Card-title')
        details = Util.get_text(self.collection_data, 'div', 'Card-details')
        price = Util.get_text(self.collection_data, 'div', 'Card-salePrice')
        link = self.collection_data.find('a', class_='Card-info-container')['href']

        items_page = ItemsPage.ItemsPage(self.driver, self.config_data, self.page_id, self.collection_id, link)
        items = items_page.get_collection_items()

        collection = {
            'page_id': self.page_id,
            'collection_id': self.collection_id,
            'category': category,
            'title': title,
            'details': details,
            'price': price,
            'link': link,
            'items': items}
        self.print(collection)
        return collection

    @staticmethod
    def print(collection):
        print('page id:', collection['page_id'])
        print('collection id:', collection['collection_id'])
        print('category:', collection['category'])
        print('title', collection['title'])
        print('details', collection['details'])
        print('price', collection['price'])
        print('link', collection['link'])
        print('items:')
        for item in collection['items']:
            print('\tpage id:', item['page_id'])
            print('\tcollection_id:', item['collection_id'])
            print('\tauthor:', item['author'])
            print('\ttitle', item['title'])
            print('\testimated_price', item['estimated_price'])
            print('\tprice_sold', item['price_sold'])
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
        print('page id:', collection[0])
        print('collection id:', collection[1])
        print('category:', collection[2])
        print('title', collection[3])
        print('details', collection[4])
        print('price', collection[5])
        print('link', collection[6])

        for item in collection[7]:
            print('\tpage id:', item[0])
            print('\tcollection_id:', item[1])
            print('\tauthor:', item[2])
            print('\ttitle', item[3])
            print('\testimated_price', item[4])
            print('\tprice_sold', item[5])


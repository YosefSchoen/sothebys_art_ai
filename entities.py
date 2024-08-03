from typing import List, Dict


class Item:
    def __init__(self, page_id: int, collection_id: int, author: str, title: str,
                 estimated_price: str, price_sold: str) -> None:
        self.page_id = page_id
        self.collection_id = collection_id
        self.author = author
        self.title = title
        self.estimated_price = estimated_price
        self.price_sold = price_sold

    def to_dict(self) -> Dict[str, str]:
        item_dict = {
            'page_id': self.page_id,
            'collection_id': self.collection_id,
            'author': self.author,
            'title': self.title,
            'estimated_price': self.estimated_price,
            'price_sold': self.price_sold
        }
        return item_dict

    def print(self):
        item_dict = self.to_dict()
        for key in item_dict:
            print(key, item_dict[key])


class Collection:
    def __init__(self, page_id: int, collection_id: int, category: str, title: str,
                 details: str, price: str, link: str, items: List[Item]) -> None:
        self.page_id = page_id
        self.collection_id = collection_id
        self.category = category
        self.title = title
        self.details = details
        self.price = price
        self.link = link
        self.items = items

    def to_dict(self) -> Dict:
        collections_dict = {
            'page_id': self.page_id,
            'collection_id': self.collection_id,
            'category': self.category,
            'title': self.title,
            'details': self.details,
            'price': self.price,
            'link': self.link,
            'items': list(map(lambda item: item.to_dict(), self.items))
        }

        return collections_dict

    def print(self):
        collection_dict = self.to_dict()
        for key in collection_dict:
            if not key == 'items':
                print(key, str(collection_dict[key]))

        for item in self.items:
            item.print()

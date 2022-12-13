

from inventory_client import InventoryClient

if __name__ == '__main__':
    client = InventoryClient()
    isbnList = ["1001", "1002"]
    for isbn in isbnList:
        print(isbn)
        result = client.getBook(isbn)
        print(result.title)
        # print(isbn.title)

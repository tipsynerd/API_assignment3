from inventory_client import InventoryClient


def main():
    client = InventoryClient()
    isbnList = ["1001", "1002"]
    titles = []
    for isbn in isbnList:
        print(isbn)
        result = client.getBook(isbn)
        print(result.title)
        titles.append(result.title)
    return titles


if __name__ == '__main__':
    main()

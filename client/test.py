import unittest
from unittest.mock import MagicMock, Mock, patch
import get_book_titles

import service.inventorySystem_pb2 as pb_2
from inventory_client import InventoryClient


class TestGrpcApi(unittest.TestCase):
    @patch('inventory_client.InventoryClient')
    def testGetBook(self, client):
        client.getBook.return_value=pb_2.Book(
        isbn="1001",
        title="Ivanhoe",
        author="Kiu Huiy",
        genre=pb_2.GENRE_FICTION,
        publishing_year=1998)

        result = client.getBook("1001")
        self.assertEqual(result.title, "Ivanhoe")

    @patch('inventory_client.InventoryClient')
    def testCreateBook(self, client):
        client.createBook.return_value = True
        result = client.getBook("1001")
        self.assertTrue(result)

    @patch('get_book_titles.main')
    def testGetBookTitles(self, get_book_titles):
        titles = ["Ivanhoe", "To Kill a Mockingbird"]
        get_book_titles.return_value = ["Ivanhoe", "To Kill a Mockingbird"]
        result = get_book_titles()
        self.assertEqual(result, titles)

# ------ Below Tests would pass only when server is running! ------
    def testGetBookLiveServer(self):
        client = InventoryClient()
        isbn = "1001"
        result = client.getBook(isbn)
        self.assertEqual(result.isbn, isbn)
        self.assertEqual(result.title, "Ivanhoe")
        self.assertEqual(result.author, "Kiu Huiy")

    def testCreateBookLiveServer(self):
        client = InventoryClient()
        result = client.createBook("1003", "Harry Potter", "J.K Rowling", 0, 1995)
        self.assertTrue(result)

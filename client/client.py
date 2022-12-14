import grpc
from concurrent import futures
import service.inventorySystem_pb2_grpc as pb_2_grpc
import service.inventorySystem_pb2 as pb_2
from inventory_client import InventoryClient


# To test the RPCs defined in the server
def run():
    client = InventoryClient()
    #   Testing getBook
    isbn = "1001"
    response = client.getBook(isbn)
    print(response)

    #   Testing createBook
    isbn = "1003"
    title = "Straight Up"
    genre = pb_2.GENRE_FICTION
    publishing_year = 2000
    author = "Travis Scott"
    response = client.createBook(isbn, title, author, genre, publishing_year)
    print("CreateBook was success: " + str(response.success))


if __name__ == "__main__":
    run()

import grpc
import service.inventorySystem_pb2_grpc as pb_2_grpc
import service.inventorySystem_pb2 as pb_2


class InventoryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb_2_grpc.InventoryStub(self.channel)

    def getBook(self, isbn):
        isbnObj = pb_2.isbn(isbn=isbn)
        result = self.stub.getBook(isbnObj)
        return result

    def createBook(self, isbn, title, author, genre, publishing_year):
        result = self.stub.createBook(pb_2.Book(
            isbn=isbn,
            title=title,
            author=author,
            genre=genre,
            publishing_year=publishing_year
        ))
        return result

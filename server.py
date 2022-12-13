import grpc
from concurrent import futures
import service.inventorySystem_pb2_grpc as pb_2_grpc
import service.inventorySystem_pb2 as pb_2

books = [

    pb_2.inventorySystem(
        isbn="1001",
        book=pb_2.Book(
            isbn="1001",
            title="Ivanhoe",
            author="Kiu Huiy",
            genre=pb_2.GENRE_FICTION,
            publishing_year=1998
        ),
        status=pb_2.STATUS_AVAILABLE,
    ),
    pb_2.inventorySystem(
        isbn="1002",
        book=pb_2.Book(
            isbn="1002",
            title="To Kill a Mockingbird",
            author="Hellen Keller",
            genre=pb_2.GENRE_NON_FICTION,
            publishing_year=1998
        ),
        status=pb_2.STATUS_TAKEN,
    ),
]


class InventoryServicer(pb_2_grpc.InventoryServicer):
    def createBook(self, request, context):
        print(request)
        isbn = request.isbn
        title = request.title
        author = request.author
        genre = request.genre
        publishing_year = request.publishing_year

        if isbn is None or title is None or author is None or genre is None or publishing_year is None:
            return pb_2.response(success=False)

        invObj = pb_2.inventorySystem(
        isbn=isbn,
        book=pb_2.Book(
            isbn=isbn,
            title=title,
            author=author,
            genre=genre,
            publishing_year=publishing_year
        ),
        status=pb_2.STATUS_AVAILABLE,
        )
        books.append(invObj)

        return pb_2.response(success=True)

    def getBook(self, request, context):
        for book in books:
            # print(book.isbn)
            # print(request.isbn)
            if book.isbn == request.isbn:
                print(request.isbn)
                print(book)

                return book.book
        return pb_2.Book()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb_2_grpc.add_InventoryServicer_to_server(InventoryServicer(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    print("Server started!")

    server.wait_for_termination()


if __name__ == "__main__":
    serve()

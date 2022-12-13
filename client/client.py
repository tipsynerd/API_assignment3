import grpc
from concurrent import futures
import service.inventorySystem_pb2_grpc as pb_2_grpc
import service.inventorySystem_pb2 as pb_2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb_2_grpc.InventoryStub(channel)
        # print("1. Create Book")
        # print("2. Search for book using ISBN")
        print("I am dead")
        book = pb_2.Book(
            isbn="420",
            title="Straight Up",
            genre=pb_2.GENRE_FICTION,
            publishing_year=2000,
            author="Travis Scott"
        )
        stub.createBook(book)
        print("Client Called")


# if __name__ == "__main__":
#     run()

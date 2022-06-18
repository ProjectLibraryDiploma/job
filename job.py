import logging

from libs.API import API
from libs.books import Books

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s"
    )

    test_api = API('https://127.0.0.1')
    books = Books('books/books.csv')

    test_api.post_new_books(books.by_category)

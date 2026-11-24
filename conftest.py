from main import BooksCollector
import pytest
import data

@pytest.fixture 
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture 
def shelf():
    collector = BooksCollector()
    collector.add_new_book(data.NAME)
    collector.set_book_genre(data.NAME, data.GENRE)
    return collector
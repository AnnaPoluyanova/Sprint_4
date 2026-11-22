from main import BooksCollector
import pytest

@pytest.fixture 
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture 
def name():
    return 'Гордость и предубеждение и зомби'

@pytest.fixture 
def genre():
    return 'Ужасы'

@pytest.fixture 
def shelf(name, genre):
    collector = BooksCollector()
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    return collector

class TestBooksCollector:
# добавляем две книги
    def test_add_new_book_add_two_books(self, shelf, name):
        shelf.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(shelf.books_genre) == 2

# устанавливаем книге жанр
    def test_set_book_genre_valid_book_sets_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

# получаем жанр книги по её имени
    def test_get_book_genre_valid_name_returns_book_genre(self, shelf, name, genre):
        assert shelf.get_book_genre(name) == genre

# выводим список книг с определённым жанром
    def test_get_books_with_specific_genre_valid_genre_returns_books_list(self, shelf, name, genre):
        assert shelf.get_books_with_specific_genre(genre) == [name]

# получаем словарь books_genre
    def test_get_books_genre_one_book_returns_books_dict(self, shelf, name, genre):
        assert shelf.get_books_genre() == {name: genre}

# возвращаем книги, подходящие детям
    @pytest.mark.parametrize('genres', ['Фантастика','Мультфильмы', 'Комедии'])
    def test_get_books_for_children_valid_genre_returns_book(self, collector, name, genres):
        collector.add_new_book(name)
        collector.set_book_genre(name, genres)
        assert collector.get_books_for_children() == [name]

# не возвращаем книги не подходящие детям
    @pytest.mark.parametrize('genres_age_rating', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_age_rating_genre_returns_empty_list(self, collector, name, genres_age_rating):
        collector.add_new_book(name)
        collector.set_book_genre(name, genres_age_rating)
        assert collector.get_books_for_children() == []

# добавляем книгу в Избранное
    def test_add_book_in_favorites_one_book_saved_in_favorites(self, shelf, name):
        shelf.add_book_in_favorites(name)
        assert shelf.favorites == [name]

# удаляем книгу из Избранного
    def test_delete_book_from_favorites_one_book_favorites_becomes_empty(self, shelf, name):
        shelf.add_book_in_favorites(name)
        shelf.delete_book_from_favorites(name)
        assert shelf.favorites == []

# получаем список Избранных книг
    def test_get_list_of_favorites_books_one_book_returns_favorites_list(self, shelf, name):
        shelf.add_book_in_favorites(name)
        assert shelf.get_list_of_favorites_books() == [name]
        
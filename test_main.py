from main import BooksCollector
import pytest
import data

class TestBooksCollector:
# добавляем две книги
    def test_add_new_book_add_two_books(self, shelf):
        shelf.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(shelf.books_genre) == 2

# устанавливаем книге жанр
    def test_set_book_genre_valid_book_sets_genre(self):
        collector = BooksCollector()
        collector.add_new_book(data.NAME)
        collector.set_book_genre(data.NAME, data.GENRE)
        assert collector.books_genre[data.NAME] == data.GENRE

# получаем жанр книги по её имени
    def test_get_book_genre_valid_name_returns_book_genre(self, shelf):
        assert shelf.get_book_genre(data.NAME) == data.GENRE

# выводим список книг с определённым жанром 
    def test_get_books_with_specific_genre_valid_genre_returns_books_list(self, shelf):
        shelf.add_new_book('Аэлита')
        shelf.set_book_genre('Аэлита', 'Фантастика')
        assert shelf.get_books_with_specific_genre(data.GENRE) == [data.NAME]

# получаем словарь books_genre
    def test_get_books_genre_one_book_returns_books_dict(self, shelf):
        assert shelf.get_books_genre() == {data.NAME: data.GENRE}

# возвращаем книги, подходящие детям
    @pytest.mark.parametrize('genres', ['Фантастика','Мультфильмы', 'Комедии'])
    def test_get_books_for_children_valid_genre_returns_book(self, collector, genres):
        collector.add_new_book(data.NAME)
        collector.set_book_genre(data.NAME, genres)
        assert collector.get_books_for_children() == [data.NAME]

# не возвращаем книги не подходящие детям
    @pytest.mark.parametrize('genres_age_rating', ['Ужасы', 'Детективы'])
    def test_get_books_for_children_age_rating_genre_returns_empty_list(self, collector, genres_age_rating):
        collector.add_new_book(data.NAME)
        collector.set_book_genre(data.NAME, genres_age_rating)
        assert collector.get_books_for_children() == []

# добавляем книгу в Избранное
    def test_add_book_in_favorites_one_book_saved_in_favorites(self, shelf):
        shelf.add_book_in_favorites(data.NAME)
        assert shelf.favorites == [data.NAME]

# удаляем книгу из Избранного
    def test_delete_book_from_favorites_one_book_favorites_becomes_empty(self, shelf):
        shelf.add_book_in_favorites(data.NAME)
        shelf.delete_book_from_favorites(data.NAME)
        assert shelf.favorites == []

# получаем список Избранных книг
    def test_get_list_of_favorites_books_one_book_returns_favorites_list(self, shelf):
        shelf.add_book_in_favorites(data.NAME)
        assert shelf.get_list_of_favorites_books() == [data.NAME]
        
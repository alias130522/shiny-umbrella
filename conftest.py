import pytest

from Program import BooksCollector

@pytest.fixture
def books_dict():
    collector = BooksCollector()
    collector.add_new_book('Реликт')
    collector.set_book_genre('Реликт', 'Фантастика')
    return collector
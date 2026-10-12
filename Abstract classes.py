from abc import ABC, abstractmethod


# 1. Абстрактний клас
class LibraryItem(ABC):

    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author

    # Властивість Title (getter/setter)
    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    # Властивість Author (getter/setter)
    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        self._author = value

    # Абстрактний метод
    @abstractmethod
    def get_info(self) -> str:
        pass


# 2. Інтерфейс (у Python це абстрактний клас без реалізації)
class IDownloadable(ABC):

    @abstractmethod
    def download(self):
        pass


# 3. Клас Book (наслідує LibraryItem)
class Book(LibraryItem):

    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    # Перевизначення абстрактного методу
    def get_info(self) -> str:
        return f'[Друкована книга] "{self.title}" — {self.author} ({self.page_count} стор.)'


# 4. Клас EBook (наслідує LibraryItem та "інтерфейс" IDownloadable)
class EBook(LibraryItem, IDownloadable):

    def __init__(self, title: str, author: str, file_size_mb: float):
        super().__init__(title, author)
        self.file_size_mb = file_size_mb

    # Перевизначення абстрактного методу з LibraryItem
    def get_info(self) -> str:
        return f'[Електронна книга] "{self.title}" — {self.author} ({self.file_size_mb} MB)'

    # Реалізація методу з IDownloadable
    def download(self):
        print(
            f'-> Завантаження файлу "{self.title}" ({self.file_size_mb} MB) розпочато...'
        )


# 5. Демонстрація роботи в консолі
if __name__ == "__main__":
    # Створення об'єктів
    paper_book = Book("Кобзар", "Тарас Шевченко", 480)
    ebook1 = EBook("Чистий код", "Роберт Мартін", 4.5)
    ebook2 = EBook("1984", "Джордж Орвелл", 2.1)

    # Список елементів бібліотеки (поліморфізм)
    library: list[LibraryItem] = [paper_book, ebook1, ebook2]

    print("=== СПИСОК ЕЛЕМЕНТІВ БІБЛІОТЕКИ (get_info) ===")
    for item in library:
        # Виклик перевизначеного методу
        print(item.get_info())

        # Перевірка, чи реалізує об'єкт "інтерфейс" IDownloadable
        if isinstance(item, IDownloadable):
            item.download()

        print("-" * 40)
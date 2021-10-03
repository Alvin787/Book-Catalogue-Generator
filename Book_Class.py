class Book:
    def __init__(self, title, author, categories, description, book_format, isbn_13, language, publication_date, rating_avg, rating_count):
        self._title = title
        self._author = author
        self._categories = categories
        self._description = description
        self._book_format = book_format
        self._isbn_13 = isbn_13
        self._language = language
        self._publication_date = publication_date
        self._rating_avg = rating_avg
        self._rating_count = rating_count
    
    def __str__(self):
        return f'title: {self._title}, author: {self._author}, categories: {self._categories}, description: {self._description}, book_format: {self._book_format}, isbn_13: {self._isbn_13}, language: {self._language}, publication_date: {self._publication_date}, rating_avg: {self._rating_avg}, rating_count: {self._rating_count}'

    def __repr__(self):
        return f'Book({self._title}, {self._author}, {self._categories}, {self._description}, {self._book_format}, {self._isbn_13}, {self._language}, {self._publication_date}, {self._rating_avg}, {self._rating_count})'
    
    def title(self):
        return self._title

    def author(self):
        return self._author

    def categories(self):
        return self._categories
    
    def description(self):
        return self._description
    
    def book_format(self):
        return self._book_format
    
    def isbn_13(self):
        return self._isbn_13
    
    def language(self):
        return self._language
    
    def publication_date(self):
        return self._publication_date
    
    def rating_avg(self):
        return self._rating_avg
    
    def rating_count(self):
        return self._rating_count

    def __eq__(self, other):
        return self._rating_avg == other.rating_avg()

    def __lt__(self, other):
        return self._rating_avg < other.rating_avg()

    def __gt__(self, other):
        return self._rating_avg > other.rating_avg()

    def __le__(self, other):
        return self._rating_avg <= other.rating_avg()

    def __ge__(self, other):
        return self._rating_avg >= other.rating_avg()
    
    def __ne__(self, other):
        return self._rating_avg != other.rating_avg()


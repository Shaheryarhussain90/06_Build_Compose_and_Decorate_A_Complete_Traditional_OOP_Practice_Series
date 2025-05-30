
class Book:
    total_book = 0

    @classmethod
    
    def increament_book_count(cls):
        cls.total_book += 1

Book.increament_book_count()
Book.increament_book_count()
Book.increament_book_count()

print(Book.total_book)

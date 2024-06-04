"""
ZADANIE 1
Stwórz iterator printujący kolejne liczby ciągu Fibonacciego podobnie to iteratora NieskonczonyIterator opisanego powyżej..
Wykorzystaj metody __iter__ oraz __next__.
"""


class Fibonacci:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


fib = Fibonacci()
for i in range(10):
    print(next(fib))

"""
ZADANIE 2
Napisz klasę LibraryBook, która będzie symulować operacje na książkach bibliotecznych.

Wymagania:

Konstruktor:
__init__(self, title, author, isbn, copies=1): Konstruktor powinien przyjmować tytuł książki (title), autora (author), numer ISBN (isbn) oraz opcjonalnie liczbę kopii (copies), która domyślnie wynosi 1.

Metody instancji:
borrow_book(self): Ta metoda powinna zmniejszać liczbę dostępnych kopii o 1, jeśli są dostępne kopie. Jeśli nie ma dostępnych kopii, metoda powinna wyświetlać komunikat o braku dostępnych egzemplarzy.
return_book(self): Ta metoda powinna zwiększać liczbę dostępnych kopii o 1.
get_info(self): Ta metoda powinna zwracać informację o książce (tytuł, autor, ISBN, dostępne kopie).
reserve_book(self): Ta metoda rezerwuje książkę, zmniejszając liczbę dostępnych kopii o 1, ale tylko wtedy, gdy jest przynajmniej jedna dostępna kopia. Rezerwacja powinna być wyświetlana jako komunikat: "Książka została zarezerwowana".

Metoda klasowa:
get_library_name(cls): Ta metoda powinna zwracać nazwę biblioteki. Nazwa biblioteki powinna być przechowywana jako atrybut klasy (np. library_name).

Metoda statyczna:
is_valid_isbn(isbn): Ta metoda powinna sprawdzać, czy numer ISBN jest poprawny. Dla uproszczenia załóżmy, że poprawny numer ISBN to taki, który składa się z 13 cyfr.

Właściwość:
copies: Zdefiniuj właściwość, która pozwala na pobieranie i ustawianie liczby kopii. Przy ustawianiu liczby kopii, jeśli nowa wartość jest mniejsza niż 0, powinna być wyświetlana odpowiednia wiadomość o błędzie.
"""


class LibraryBook:
    library_name = "MyLibrary"

    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    @property
    def copies(self):
        return self._copies

    @copies.setter
    def copies(self, value):
        if value < 0:
            print("Number of copies cannot be less than 0.")
        else:
            self._copies = value

    @classmethod
    def get_library_name(cls):
        return cls.library_name

    @staticmethod
    def is_valid_isbn(isbn):
        return len(isbn) == 13

    def borrow_book(self):
        if self.copies > 0:
            self.copies -= 1
        else:
            return Exception("Not enough copies.")

    def return_book(self):
        self.copies += 1

    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}"

    def reserve_book(self):
        result = self.borrow_book()
        if isinstance(result, Exception):
            return Exception("Reservation failed. " + str(result))
        print("Reservation has been created.")


"""
Zadanie 3
1. Stwórz funkcję wyliczającą liczby z zakresu od 0 do n (argumentu funkcji).
2. Utwórz funkcję w formie dekoratora tej funkcji, która będzie podwajała print każdej liczby.
"""


class Digits:

    def iter_digits(max):
        for i in range(max):
            yield i

    @staticmethod
    def double_print(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(result * 2)
        return wrapper

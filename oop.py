#Create a class called Car with attributes brand and color. Instantiate an object
#of the Car class and print its attributes.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

# Instantiate an object of the Car class
my_car = Car("Toyota", "Red")

# Print the attributes of the car
print("Car Brand:", my_car.brand)
print("Car Color:", my_car.color)


#Add a method called start_engine to the Car class that prints a
#message saying the engine of the car has started. Create an instance of Car and call
#the method.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.color} car has started.")

# Instantiate an object of the Car class
my_car = Car("Toyota", "Red")

# Call the start_engine method
my_car.start_engine()



#Create a class called BankAccount with attributes account_number and balance. 
#Add methods to:
# Deposit an amount.
# Withdraw an amount (only if sufficient balance exists).
# Print the account balance.

class BankAccount:
    def __init__(self, account_number, balance=0):  #ensures that when the account is created, it has a starting balance of 0 unless a different balance is specified.
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposit an amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        """Withdraw an amount from the account if sufficient balance exists."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Insufficient balance to withdraw.")

    def print_balance(self):
        """Print the current account balance."""
        print(f"Account balance: ${self.balance}")

account = BankAccount("12345678", 500)

account.deposit(200)

account.withdraw(100)

account.print_balance()


#: Implement a class called Library that manages a collection of books. Each
#book has a title, author, and available status. The Library class should have
#methods to:
# Add a book to the library.
# Remove a book from the library.
# Check if a book is available by title.
# Borrow a book (mark it as unavailable if it’s available).
# Return a book (mark it as available again if it was borrowed


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)
        print(f'Book "{book.title}" added to the library.')

    def remove_book(self, title):
        """Remove a book from the library by its title."""
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f'Book "{title}" removed from the library.')
                return
        print(f'Book "{title}" not found in the library.')

    def is_available(self, title):
        """Check if a book is available by its title."""
        for book in self.books:
            if book.title == title:
                return book.is_available
        print(f'Book "{title}" not found in the library.')
        return False

    def borrow_book(self, title):
        """Borrow a book (mark it as unavailable)."""
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f'You have borrowed "{book.title}".')
                    return
                else:
                    print(f'Book "{title}" is already borrowed.')
                    return
        print(f'Book "{title}" not found in the library.')

    def return_book(self, title):
        """Return a book (mark it as available)."""
        for book in self.books:
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print(f'You have returned "{book.title}".')
                    return
                else:
                    print(f'Book "{title}" was not borrowed.')
                    return
        print(f'Book "{title}" not found in the library.')



if __name__ == "__main__":
    library = Library()
    
    # Add books to the library
    book1 = Book("The Way to success", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    library.add_book(book1)
    library.add_book(book2)

    # Check availability
    print(library.is_available("The Way to success"))  # True

    # Borrow a book
    library.borrow_book("The Way to success")
    
    # Check availability again
    print(library.is_available("The Way to success"))  # False

    # Return a book
    library.return_book("The Way to success")
    
    # Check availability again
    print(library.is_available("The Way to success"))  # True

    # Remove a book
    library.remove_book("1984")
    print(library.is_available("1984"))  # False

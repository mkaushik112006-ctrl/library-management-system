from utils import books, issued_books

def show_books():
    if len(books) == 0:
        print("No books in library.")
        return
    
    print("\nBook Name               Total    Available")
    print("-" * 45)
    for name in books:
        issued = len(issued_books.get(name, []))
        available = books[name] - issued
        print(f"{name:<24} {books[name]:<9} {available}")
    print("-" * 45)

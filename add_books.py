from utils import books

def add_book():
    name = input("Enter book name: ").upper()
    copies = int(input("Enter number of copies: "))
    
    if name in books:
        books[name] += copies
        print("Book already exists. Copies updated. Total copies:", books[name])
    else:
        books[name] = copies
        print("Book added successfully.")

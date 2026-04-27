from utils import books, issued_books
from datetime import date, timedelta

def issue_book():
    name = input("Enter book name: ").upper()
    
    if name not in books:
        print("Book not found.")
        return
    
    issued = len(issued_books.get(name, []))
    available = books[name] - issued
    
    if available == 0:
        print("No copies available right now.")
        return
    
    student = input("Enter student name: ")
    days = int(input("Enter number of days to issue: "))
    
    issue_date = date.today()
    due_date = issue_date + timedelta(days=days)
    
    record = {
        "student": student,
        "issue_date": issue_date,
        "due_date": due_date,
        "days": days
    }
    
    if name not in issued_books:
        issued_books[name] = []
    issued_books[name].append(record)
    
    print("\nBook issued successfully.")
    print("Student   :", student)
    print("Book      :", name)
    print("Issue Date:", issue_date)
    print("Due Date  :", due_date)
    print("\nFine if returned late:")
    print("Week 1 - Rs. 10 per day")
    print("Week 2 - Rs. 20 per day")
    print("Week 3 - Rs. 60 per day")
    print("And so on...")

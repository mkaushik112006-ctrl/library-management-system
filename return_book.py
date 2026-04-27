from utils import issued_books
from datetime import date

def calculate_fine(due_date, return_date):
    overdue_days = (return_date - due_date).days
    if overdue_days <= 0:
        return 0
    
    fine = 0
    week = 1
    remaining = overdue_days
    rate = 10
    
    while remaining > 0:
        days_this_week = min(7, remaining)
        fine += days_this_week * rate
        remaining -= days_this_week
        week += 1
        rate = rate * week
    
    return fine

def return_book():
    name = input("Enter book name: ").upper()
    
    if name not in issued_books or len(issued_books[name]) == 0:
        print("No issued record found for this book.")
        return
    
    student = input("Enter student name: ")
    
    record = None
    for r in issued_books[name]:
        if r["student"] == student:
            record = r
            break
    
    if record is None:
        print("No record found for this student and book.")
        return
    
    return_date = date.today()
    due_date = record["due_date"]
    fine = calculate_fine(due_date, return_date)
    
    issued_books[name].remove(record)
    
    print("\nBook returned.")
    print("Student    :", student)
    print("Book       :", name)
    print("Due Date   :", due_date)
    print("Return Date:", return_date)
    
    if fine == 0:
        print("Returned on time. No fine.")
    else:
        overdue = (return_date - due_date).days
        print("Days Late  :", overdue)
        print("Fine Amount: Rs.", fine)

# Import libraries
import csv
from os import system, name

# Codes
# Functions
def clrscr():
    # This function clears the screen
    system('cls') if name == 'nt' else system('clear')

def displaybook():
    clrscr()
    with open(filename) as dbfile:
        reader = csv.DictReader(dbfile)
        books = [dict(row) for row in reader]
        print(*(f'{field:25}' for field in fields))
        for row in books:
            print(*(f'{value:25}' for value in row.values()))
    input("Press Enter to go back...")

def addbook():
    clrscr()
    print("Add another book to database:")
    global last_id
    newbook = {
            'ID' : last_id + 1,
            'Title' : input("Book's title    : "),
            'Author' : input("Book's Author   : "),
            'Genre' : input("Book's Genre    : "),
            'Year' : input("Book's Year     : ")
            }
    valid = input("Are you sure to add the book above? y/n\n>> ")
    if valid.lower() == "y":
        last_id += 1
        with open(filename, 'a') as dbfile:
            writer = csv.DictWriter(dbfile, fieldnames=fields)
            writer.writerow(newbook)
        input("Books added! Press Enter to continue...")
    else:
        input("Cancelled! Press Enter to continue...")

def searchbook():
    clrscr()
    print("""---Search function---
            Search by:
                1 - Title
                2 - Author
                3 - Genre
                4 - Year""")
    method = input(">> ")
    searchkey = input(f"Input the book's {fields[int(method)]}\n>> ")
    with open(filename) as dbfile:
        reader = csv.DictReader(dbfile)
        books = [dict(row) for row in reader]
        print(*(f'{field:25}' for field in fields))
        print(*(f'{value:25}' for row in books for value in row.values() if row[fields[int(method)]] == searchkey))
    print()
    input("Press Enter to Continue...")


## initial variables
fields = ['ID', 'Title', 'Author', 'Genre', 'Year']
filename = 'database.csv'
with open(filename) as dbfile:
    reader = csv.DictReader(dbfile)
    data = [dict(row) for row in reader]
last_id = int(data[-1].get('ID')) if data != [] else 0
choice = ''

## Main Menu
while(choice.lower() != "x"):
    clrscr()
    print("""---Python Library Organizer---
        Menu :
            1 - Display books
            2 - Add a book
            3 - Search books
            x - Quit the apps""")
    choice = input(">> ")
    switcher = {
            '1' : displaybook,
            '2' : addbook,
            '3' : searchbook,
            'x' : lambda : print("Thank you for using our apps!")
            }.get(choice, lambda: input("Invalid Choice!"))()

# Import libraries
import csv
from os import system, name

# Codes
# Functions
def clrscr():
    # This function clears the screen
    system('cls') if name == 'nt' else system('clear')

def displaybook():
    pass

def addbook():
    pass

## initial variables
fields = ['ID', 'Title', 'Author', 'Genre', 'Year']
filename = 'database.csv'
with open(filename) as dbfile:
    reader = csv.DictReader(dbfile)
    data = [dict(row) for row in reader]
last_id = data[-1].get('ID') if data != [] else 0
choice = ''

## Main Menu
while(choice.lower() != "x"):
    clrscr()
    print("""---Python Library Organizer---
        Menu :
            1 - Display books
            2 - Add a book
            x - Quit the apps""")
    choice = input(">> ")
    if choice == '1':
        displaybook()
    elif choice.lower() == 'x':
        print("Thank you for using our apps!")
    else:
        input("Invalid Choice!")

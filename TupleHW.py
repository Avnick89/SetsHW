#Tuple Itinerary

itinerary1=[("Anthony", 'Texas', 'Paris'), ('Elmer', 'Mexico', 'Spain')]
def tuple_(itinerary1):
    for index, itinerary in enumerate(itinerary1): # Pull out the index and each item inside
        name, origin, destination = itinerary # Assign each item in the tupke a variable
        print(f"Itinerary {index + 0}: {name} - From {origin} to {destination}") # fancy print statement with all elements
    
tuple_(itinerary1)

    
  
 

#Library System
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
def library_system(book, author):
    new_book = (book, author)
    if new_book in library: 
        print("This book is already in the library")
    else:
        library.append(new_book) 
        print("Book has been added to the library")
    print(library)
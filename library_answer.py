Library Management System
"""

library = []

def add_book(id, title, author, **kwargs):
    """Add a new book into the library with flexible details."""
    book = {
        "id": id,
        "title": title,
        "author": author,
        "available": True
    }
    # Add optional details like year, genre
    book.update(kwargs)
    library.append(book)
    return f"Book '{title}' added successfully!"

def search_books(*args):
    """Search for books by multiple keywords (title, author)."""
    results = []
    for book in library:
        for keyword in args:
            if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
                results.append(book)
                break
    return results if results else "No books found."

def borrow_book(book_id):
    """Borrow a book if available."""
    for book in library:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                return f"You borrowed '{book['title']}'."
            else:
                return f"Book '{book['title']}' not available."
    return "Book not found."

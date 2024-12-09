from flask import Blueprint, request, jsonify, abort
from .models import db, Book

# Create a Blueprint for organizing routes
bp = Blueprint('library', __name__)


# Create Book
@bp.route('/book', methods=['POST'])
def add_book():
    data = request.get_json()  # Extract data from the request
    new_book = Book(title=data['title'], author=data['author'], year=data['year'])

    db.session.add(new_book)
    db.session.commit()

    return jsonify({"message": "Book added successfully!"}), 201


# Read all Books
@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()  # Get all books from the database
    return jsonify([{"id": book.id, "title": book.title, "author": book.author, "year": book.year} for book in books])


# Update Book
@bp.route('/book/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = Book.query.get_or_404(id)

    book.title = data['title']
    book.author = data['author']
    book.year = data['year']

    db.session.commit()
    return jsonify({"message": "Book updated successfully!"})


# Delete Book
@bp.route('/book/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": "Book deleted successfully!"})

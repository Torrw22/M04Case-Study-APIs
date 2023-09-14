from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for initial testing
books = [
    {"id": 1, "book_name": "Book 1", "author": "Author 1", "publisher": "Publisher 1"},
    {"id": 2, "book_name": "Book 2", "author": "Author 2", "publisher": "Publisher 2"},
]

# Create (POST) a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    if not data or 'book_name' not in data or 'author' not in data or 'publisher' not in data:
        return jsonify({"error": "Incomplete book data"}), 400
    
    new_book = {
        "id": len(books) + 1,
        "book_name": data['book_name'],
        "author": data['author'],
        "publisher": data['publisher']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Read (GET) all books
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books)

# Read (GET) a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book)

# Update (PUT) a specific book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((b for b in books if b['id'] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    book['book_name'] = data.get('book_name', book['book_name'])
    book['author'] = data.get('author', book['author'])
    book['publisher'] = data.get('publisher', book['publisher'])
    
    return jsonify(book)

# Delete (DELETE) a specific book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    books.remove(book)
    return jsonify({"message": "Book deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
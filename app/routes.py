from flask import Blueprint, jsonify

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello_world", methods=["GET"])
def say_hello():
    response = "Hello World!"
    return response, 200

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    response = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    return response, 200

@hello_world_bp.route("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
]

books_bp = Blueprint("hello_world", __name__)

@books_bp.route("", methods=["GET"], url_prefix="/books")
def handle_books():
    book_response = []
    for book in books:
        book_response.append({
            'id': book.id,
            'title': book.title,
            'description': book.description
        })
    return jsonify(book_response), 200
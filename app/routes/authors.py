from os import abort
from app import db
from app.models.author import Author
from app.routes.books import validate_model
from flask import Blueprint, jsonify, abort, make_response, request

authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")

@authors_bp.route("", methods=['GET'])
def get_authors():
    authors = Author.query.all()
    response_body = []
    for author in authors:
        response_body.append(author.to_dict())

    return jsonify(response_body), 200

@authors_bp.route("", methods=["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author.from_dict(request_body)

    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f"Author {new_author.name} successfully created."), 201)

@authors_bp.route('/<author_id>/books', methods=["POST"])
def create_book(author_id):
    author = validate_model(Author, author_id)
    request_body = request.get_json()
    
    new_book = Book(title=request_body['title'],
                    description=request_body['description'],
                    author=author)
    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} successfully created"), 201)

@authors_bp.route("/<author_id>/books", methods=["GET"])
def read_books(author_id):
    author = validate_model(Author, author_id)

    book_response = []
    for book in author.books:
        book_response.append(book.to_dict())

    return jsonify(book_response), 200
import pytest
from app import db
from app import create_app
from flask.signals import request_finished
from app.models.book import Book

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_books():
    ocean_book = Book(title="Ocean Book", description='water 4ever')
    mountain_book = Book(title="Mountain Book", description='I climb rocks!')

    db.session.add_all([ocean_book, mountain_book])
    db.session.commit()
# Test get books with no records
def test_get_books_with_no_records(client):
    # Act
    response = client.get('/books')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# Test get one book
def test_get_one_book(client, two_saved_books):
    response = client.get('/books/1')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "description": "water 4ever",
        "title": "Ocean Book"
    }

# GET /books/1 with no data in test database (no fixture) returns a 404
def test_get_one_book_with_no_records(client):
    response = client.get('/books/1')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"Book 1 not found"}

# GET /books with valid test data (fixtures) returns a 200 with an array including appropriate test data
def test_get_all_books(client, two_saved_books):
    # Act
    response = client.get('/books')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{
        "id": 1,
        "description": "water 4ever",
        "title": "Ocean Book"
    },{
        "id": 2,
        "description": "I climb rocks!",
        "title": "Mountain Book"
    }]


#POST /books with a JSON request body returns a 201
def test_post_book(client):
    response = client.post('/books', json={"title": "Harry potter 1", "description": "Book1"})
    response_body = response.get_data(as_text=True)

    # Assert
    assert response.status_code == 201
    assert response_body == "Book Harry potter 1 successfully created"
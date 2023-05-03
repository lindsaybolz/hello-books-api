# Test get books with no records
def test_get_books_with_no_records(client):
    # Act
    response = client.get('/books')
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_root_redirect(client):
    # Arrange
    # テストクライアントはfixtureで準備済み
    # Act
    response = client.get("/")
    # Assert
    assert response.status_code in (200, 307, 308)
    assert "text/html" in response.headers["content-type"]

from fastapi.testclient import TestClient

def test_index_page(client):
    """Test that the main page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    # Verify key elements of the page
    assert "<title>HTMX + FastAPI Example</title>" in response.text
    assert 'id="counter"' in response.text
    assert "Count: 0" in response.text
    assert 'hx-post="/submit"' in response.text

def test_counter_endpoint(client):
    """Test that the counter endpoint increments correctly."""
    # Test with starting value 0
    response = client.get("/count/0")
    assert response.status_code == 200
    assert 'id="counter"' in response.text
    assert "Count: 1" in response.text
    assert 'hx-get="/count/1"' in response.text
    
    # Test with starting value 5
    response = client.get("/count/5")
    assert response.status_code == 200
    assert 'id="counter"' in response.text
    assert "Count: 6" in response.text
    assert 'hx-get="/count/6"' in response.text

def test_form_submission(client):
    """Test that the form submission endpoint works correctly."""
    # Test with valid name
    response = client.post("/submit", data={"name": "Alice"})
    assert response.status_code == 200
    assert "<div style='color: green;'>Hello, Alice! Your form was submitted successfully.</div>" in response.text
    
    # Test with empty name
    response = client.post("/submit", data={"name": ""})
    assert response.status_code == 200
    assert "<div style='color: red;'>Please enter your name</div>" in response.text
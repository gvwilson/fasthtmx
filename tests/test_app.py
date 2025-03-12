from fastapi.testclient import TestClient

def test_main_page_loads_correctly(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "<title>HTMX + FastAPI Example</title>" in response.text
    assert 'id="counter"' in response.text
    assert "Count: 0" in response.text
    assert 'hx-post="/submit"' in response.text

def test_counter_endpoint_increments_zero(client):
    response = client.get("/count/0")
    assert response.status_code == 200
    assert 'id="counter"' in response.text
    assert "Count: 1" in response.text
    assert 'hx-get="/count/1"' in response.text
    
def test_counter_endpoint_increments_nonzero(client):
    response = client.get("/count/5")
    assert response.status_code == 200
    assert 'id="counter"' in response.text
    assert "Count: 6" in response.text
    assert 'hx-get="/count/6"' in response.text

def test_form_submission_with_valid_text(client):
    response = client.post("/submit", data={"name": "Alice"})
    assert response.status_code == 200
    assert '<p id="result" class="ok">Hello, Alice!</p>' in response.text
    
def test_form_submission_with_empty_text(client):
    response = client.post("/submit", data={"name": ""})
    assert response.status_code == 200
    assert '<p id="result" class="error">Please enter your name</p>' in response.text

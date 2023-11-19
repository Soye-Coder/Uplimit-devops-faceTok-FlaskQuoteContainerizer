import sys
sys.path.append("./")
import pytest
from unittest.mock import patch

from quote_gen.app import app as gen_app
from quote_disp.app import app as disp_app

@pytest.fixture
def gen_client():
    with gen_app.test_client() as client:
        yield client

@pytest.fixture
def disp_client():
    with disp_app.test_client() as client:
        yield client

def test_quote_gen_endpoint(gen_client):
    response = gen_client.get('/quote')
    assert response.status_code == 200

def test_quote_disp_endpoint_health(gen_client):
    response = gen_client.get('/health')
    assert response.data.decode('utf-8') == "healthy"

@patch("random.randrange")
def test_quote_endpoint(mock_randrange, gen_client):
    # Mock the return value of random.randrange to always be 0
    mock_randrange.return_value = 0

    # Make a request to the /quote endpoint
    response = gen_client.get("/quote")

    # Check if the status code is 200
    assert response.status_code == 200

    # Check if the response matches the expected quote
    expected_quote = "The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela"
    assert response.data.decode("utf-8") == expected_quote

def test_quote_disp_endpoint(disp_client):
    response = disp_client.get('/get_quote')
    assert response.status_code == 200
    
def test_quote_disp_endpoint_health(disp_client):
    response = disp_client.get('/health')
    assert response.data.decode('utf-8') == "healthy"
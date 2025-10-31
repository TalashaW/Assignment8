# tests/integration/test_fastapi_calculator.py

"""
Integration Tests for FastAPI Calculator Application

This module contains integration tests that verify the correct interaction between
the FastAPI application endpoints and the underlying calculator business logic.
These tests use FastAPI's TestClient to simulate HTTP requests without running
a live server, ensuring that the API routes, request validation, error handling,
and response formatting work correctly together.
"""

import pytest  # Import the pytest framework for writing and running tests
from fastapi.testclient import TestClient  # Import TestClient for simulating API requests
from main import app  # Import the FastAPI app instance from your main application file
from unittest.mock import patch, MagicMock
# ---------------------------------------------
# Pytest Fixture: client
# ---------------------------------------------

@pytest.fixture
def client():
    """
    Pytest Fixture to create a TestClient for the FastAPI application.

    This fixture initializes a TestClient instance that can be used to simulate
    requests to the FastAPI application without running a live server. The client
    is yielded to the test functions and properly closed after the tests complete.

    Benefits:
    - Speeds up testing by avoiding the overhead of running a server.
    - Allows for testing API endpoints in isolation.
    """
    with TestClient(app) as client:
        yield client  # Provide the TestClient instance to the test functions

# ---------------------------------------------
# Test Function: test_add_api
# ---------------------------------------------

def test_add_api(client):
    """
    Test the Addition API Endpoint.

    This test verifies that the `/add` endpoint correctly adds two numbers provided
    in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/add` endpoint with JSON data `{'a': 10, 'b': 5}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`15`).
    """
    # Send a POST request to the '/add' endpoint with JSON payload
    response = client.post('/add', json={'a': 10, 'b': 5})
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Assert that the JSON response contains the correct 'result' value
    assert response.json()['result'] == 15, f"Expected result 15, got {response.json()['result']}"

# ---------------------------------------------
# Test Function: test_subtract_api
# ---------------------------------------------

def test_subtract_api(client):
    """
    Test the Subtraction API Endpoint.

    This test verifies that the `/subtract` endpoint correctly subtracts the second number
    from the first number provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/subtract` endpoint with JSON data `{'a': 10, 'b': 5}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`5`).
    """
    # Send a POST request to the '/subtract' endpoint with JSON payload
    response = client.post('/subtract', json={'a': 10, 'b': 5})
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Assert that the JSON response contains the correct 'result' value
    assert response.json()['result'] == 5, f"Expected result 5, got {response.json()['result']}"

# ---------------------------------------------
# Test Function: test_multiply_api
# ---------------------------------------------

def test_multiply_api(client):
    """
    Test the Multiplication API Endpoint.

    This test verifies that the `/multiply` endpoint correctly multiplies two numbers
    provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/multiply` endpoint with JSON data `{'a': 10, 'b': 5}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`50`).
    """
    # Send a POST request to the '/multiply' endpoint with JSON payload
    response = client.post('/multiply', json={'a': 10, 'b': 5})
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Assert that the JSON response contains the correct 'result' value
    assert response.json()['result'] == 50, f"Expected result 50, got {response.json()['result']}"

# ---------------------------------------------
# Test Function: test_divide_api
# ---------------------------------------------

def test_divide_api(client):
    """
    Test the Division API Endpoint.

    This test verifies that the `/divide` endpoint correctly divides the first number
    by the second number provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/divide` endpoint with JSON data `{'a': 10, 'b': 2}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`5`).
    """
    # Send a POST request to the '/divide' endpoint with JSON payload
    response = client.post('/divide', json={'a': 10, 'b': 2})
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Assert that the JSON response contains the correct 'result' value
    assert response.json()['result'] == 5, f"Expected result 5, got {response.json()['result']}"

# ---------------------------------------------
# Test Function: test_divide_by_zero_api
# ---------------------------------------------

def test_divide_by_zero_api(client):
    """
    Test the Division by Zero API Endpoint.

    This test verifies that the `/divide` endpoint correctly handles division by zero
    by returning an appropriate error message and status code.

    Steps:
    1. Send a POST request to the `/divide` endpoint with JSON data `{'a': 10, 'b': 0}`.
    2. Assert that the response status code is `400 Bad Request`.
    3. Assert that the JSON response contains an 'error' field with the message "Cannot divide by zero!".
    """
    # Send a POST request to the '/divide' endpoint with JSON payload attempting division by zero
    response = client.post('/divide', json={'a': 10, 'b': 0})
    
    # Assert that the response status code is 400 (Bad Request), indicating an error occurred
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
    
    # Assert that the JSON response contains an 'error' field
    assert 'error' in response.json(), "Response JSON does not contain 'error' field"
    
    # Assert that the 'error' field contains the correct error message
    assert "Cannot divide by zero!" in response.json()['error'], \
        f"Expected error message 'Cannot divide by zero!', got '{response.json()['error']}'"

# ---------------------------------------------
# Test Function: test_root_endpoint
# ---------------------------------------------

@pytest.mark.integration
def test_root_endpoint(client):
    """
    Test the Root Endpoint (Homepage).

    This test verifies that the root endpoint `/` serves the HTML template correctly.

    Steps:
    1. Send a GET request to the `/` endpoint.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the response content type is `text/html`.
    """
    # Send a GET request to the root endpoint
    response = client.get('/')
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Assert that the response content type is HTML
    assert 'text/html' in response.headers['content-type'], \
        f"Expected content-type to contain 'text/html', got {response.headers['content-type']}"

# ---------------------------------------------
# Test Function: test_add_missing_field
# ---------------------------------------------

@pytest.mark.integration
def test_add_missing_field(client):
    """
    Test Addition Endpoint with Missing Field.

    This test verifies that the `/add` endpoint correctly handles requests with missing fields.

    Steps:
    1. Send a POST request to the `/add` endpoint with only 'a' parameter (missing 'b').
    2. Assert that the response status code is `400 Bad Request`.
    3. Assert that the JSON response contains an 'error' field.
    """
    # Send a POST request with missing 'b' parameter
    response = client.post('/add', json={'a': 10})
    
    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
    
    # Assert that the JSON response contains an 'error' field
    assert 'error' in response.json(), "Response JSON does not contain 'error' field"


# ---------------------------------------------
# Test Function: test_subtract_missing_field
# ---------------------------------------------

@pytest.mark.integration
def test_subtract_missing_field(client):
    """
    Test Subtraction Endpoint with Missing Field.

    This test verifies that the `/subtract` endpoint correctly handles requests with missing fields.

    Steps:
    1. Send a POST request to the `/subtract` endpoint with only 'b' parameter (missing 'a').
    2. Assert that the response status code is `400 Bad Request`.
    3. Assert that the JSON response contains an 'error' field.
    """
    # Send a POST request with missing 'a' parameter
    response = client.post('/subtract', json={'b': 5})
    
    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
    
    # Assert that the JSON response contains an 'error' field
    assert 'error' in response.json(), "Response JSON does not contain 'error' field"

# ---------------------------------------------
# Test Function: test_multiply_invalid_type
# ---------------------------------------------

@pytest.mark.integration
def test_multiply_invalid_type(client):
    """
    Test Multiplication Endpoint with Invalid Data Type.

    This test verifies that the `/multiply` endpoint correctly handles requests with invalid data types.

    Steps:
    1. Send a POST request to the `/multiply` endpoint with 'a' as a string instead of a number.
    2. Assert that the response status code is `400 Bad Request`.
    3. Assert that the JSON response contains an 'error' field.
    """
    # Send a POST request with invalid type for 'a' parameter
    response = client.post('/multiply', json={'a': 'invalid', 'b': 5})
    
    # Assert that the response status code is 400 (Bad Request)
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
    
    # Assert that the JSON response contains an 'error' field
    assert 'error' in response.json(), "Response JSON does not contain 'error' field"

# ---------------------------------------------
# Test Function: test_add_unexpected_exception
# ---------------------------------------------

@pytest.mark.integration
def test_add_unexpected_exception(client):
    """
    Test Addition Endpoint with Unexpected Exception.

    This test uses mocking to simulate an unexpected exception in the add operation
    to ensure that the generic exception handler is covered.

    Steps:
    1. Mock the `add` function to raise a RuntimeError.
    2. Send a POST request to the `/add` endpoint.
    3. Assert that the response status code is `400 Bad Request`.
    4. Assert that the JSON response contains an 'error' field.
    """
    # Mock the add function to raise an unexpected exception
    with patch('main.add') as mock_add:
        mock_add.side_effect = RuntimeError("Unexpected error")
        
        # Send a POST request to the '/add' endpoint
        response = client.post('/add', json={'a': 10, 'b': 5})
        
        # Assert that the response status code is 400 (Bad Request)
        assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
        
        # Assert that the JSON response contains an 'error' field
        assert 'error' in response.json(), "Response JSON does not contain 'error' field"

# ---------------------------------------------
# Test Function: test_subtract_unexpected_exception
# ---------------------------------------------
@pytest.mark.integration
def test_subtract_unexpected_exception(client):
    """
    Test Subtraction Endpoint with Unexpected Exception.

    This test uses mocking to simulate an unexpected exception in the subtract operation
    to ensure that the generic exception handler is covered.

    Steps:
    1. Mock the `subtract` function to raise a RuntimeError.
    2. Send a POST request to the `/subtract` endpoint.
    3. Assert that the response status code is `400 Bad Request`.
    4. Assert that the JSON response contains an 'error' field.
    """
    # Mock the subtract function to raise an unexpected exception
    with patch('main.subtract') as mock_add:
        mock_add.side_effect = RuntimeError("Unexpected error")
        
        # Send a POST request to the '/subtract' endpoint
        response = client.post('/subtract', json={'a': 10, 'b': 5})
        
        # Assert that the response status code is 400 (Bad Request)
        assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
        
        # Assert that the JSON response contains an 'error' field
        assert 'error' in response.json(), "Response JSON does not contain 'error' field"

# ---------------------------------------------
# Test Function: test_multiply_unexpected_exception
# ---------------------------------------------

@pytest.mark.integration
def test_multiply_unexpected_exception(client):
    """
    Test Multiplication Endpoint with Unexpected Exception.

    This test uses mocking to simulate an unexpected exception in the multiply operation
    to ensure that the generic exception handler is covered.

    Steps:
    1. Mock the `multiply` function to raise a RuntimeError.
    2. Send a POST request to the `/multiply` endpoint.
    3. Assert that the response status code is `400 Bad Request`.
    4. Assert that the JSON response contains an 'error' field.
    """
    # Mock the multiply function to raise an unexpected exception
    with patch('main.multiply') as mock_multiply:
        mock_multiply.side_effect = RuntimeError("Unexpected error")
        
        # Send a POST request to the '/multiply' endpoint
        response = client.post('/multiply', json={'a': 10, 'b': 5})
        
        # Assert that the response status code is 400 (Bad Request)
        assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
        
        # Assert that the JSON response contains an 'error' field
        assert 'error' in response.json(), "Response JSON does not contain 'error' field"

# ---------------------------------------------
# Test Function: test_divide_unexpected_exception
# ---------------------------------------------

@pytest.mark.integration
def test_divide_unexpected_exception(client):
    """
    Test Division Endpoint with Unexpected Exception.

    This test uses mocking to simulate an unexpected exception in the divide operation
    to ensure that the generic exception handler is covered.

    Steps:
    1. Mock the `divide` function to raise a RuntimeError (not ValueError).
    2. Send a POST request to the `/divide` endpoint.
    3. Assert that the response status code is `500 Internal Server Error`.
    4. Assert that the JSON response contains an 'error' field with "Internal Server Error".
    """
    # Mock the divide function to raise an unexpected exception (not ValueError)
    with patch('main.divide') as mock_divide:
        mock_divide.side_effect = RuntimeError("Unexpected error")
        
        # Send a POST request to the '/divide' endpoint
        response = client.post('/divide', json={'a': 10, 'b': 2})
        
        # Assert that the response status code is 500 (Internal Server Error)
        assert response.status_code == 500, f"Expected status code 500, got {response.status_code}"
        
        # Assert that the JSON response contains the correct error message
        assert response.json()['error'] == "Internal Server Error", \
            f"Expected error 'Internal Server Error', got '{response.json()['error']}'"
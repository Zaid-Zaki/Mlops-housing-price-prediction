# test.py
import pytest
from flask import Flask
from app import app_flask as app

@pytest.fixture
def client():
    # Set up the testing client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page_get(client):
    """Test the home page renders correctly with a GET request."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mean Absolute Error" in response.data  # Check if MAE is displayed on the page

def test_prediction_post(client):
    """Test making a prediction with POST request."""
    # Create sample input data for prediction
    sample_data = {
        'avg_area_income': 65000,
        'avg_area_house_age': 5,
        'avg_area_rooms': 7,
        'avg_area_bedrooms': 4,
        'area_population': 30000
    }

    # Send POST request to the prediction route
    response = client.post('/', data=sample_data)

    # Check if the response is OK
    assert response.status_code == 200

    # Check if the prediction and metrics are displayed in the response
    assert b"Prediction" in response.data
    assert b"Mean Absolute Error" in response.data
    assert b"Mean Squared Error" in response.data
    assert b"Root Mean Squared Error" in response.data

    # Ensure that the prediction value appears on the page (check a number format)
    assert any(char.isdigit() for char in response.data.decode())  # Check for digits in response

def test_invalid_input_post(client):
    """Test POST request with invalid input to ensure proper handling."""
    invalid_data = {
        'avg_area_income': 'invalid',  # Invalid non-numeric input
        'avg_area_house_age': 'invalid',
        'avg_area_rooms': 'invalid',
        'avg_area_bedrooms': 'invalid',
        'area_population': 'invalid'
    }

    response = client.post('/', data=invalid_data)

    # Check that it does not crash and handles the invalid input gracefully
    assert response.status_code == 400 or response.status_code == 200
    assert b"Please enter valid numerical values" in response.data or b"Prediction" not in response.data

if __name__ == '__main__':
    pytest.main()

import pytest
import requests

@pytest.mark.parametrize("api_endpoint", [
    "https://gorest.co.in/public/v2/posts/",  # Modify this with your actual API endpoint
])
def test_json_response(api_endpoint):
    response = requests.get(api_endpoint)
    assert response.status_code == 200
import pytest
import requests
import sys

@pytest.mark.parametrize("api_endpoint", [
    "https://gorest.co.in/public/v2/posts/",  # Modify this with your actual API endpoint
])
def test_json_response(api_endpoint):
    response = requests.get(api_endpoint)
    assert response.status_code == 200

if __name__ == '__main__':
    test_case_num = int(sys.argv[1])
    test_json_response(test_case_num)

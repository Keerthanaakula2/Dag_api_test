import pytest
import requests
import os

test_case_num = int(os.environ.get('TEST_CASE_NUM'))

@pytest.mark.parametrize("api_endpoint", [
    "https://gorest.co.in/public/v2/posts/",  # Modify this with your actual API endpoint
])
def test_json_response(api_endpoint):
    response = requests.get(api_endpoint)
    assert response.status_code == 200

if __name__ == '__main__':
    test_json_response(test_case_num)



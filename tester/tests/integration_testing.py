import requests
import os
import pytest

APP_NAME, APP_PORT = os.getenv('APP_NAME'), os.getenv('APP_PORT')


@pytest.mark.parametrize("endpoint,expected_code", [("/", 200), ("/files", 200)])
def test_return_codes(endpoint, expected_code):
        url = f"http://{APP_NAME}:{APP_PORT}/{endpoint}"
        status_code = int(requests.get(url).status_code)
        assert expected_code == status_code, (f"Wrong status code. Expected {expected_code}, "
                                                     f"received {status_code}")

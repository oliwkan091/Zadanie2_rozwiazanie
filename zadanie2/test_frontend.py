import time

import requests
from lxml import html

HOST = "http://localhost:9001"

time.sleep(10)


def test_frontend_connection():
    response = requests.get(f"{HOST}/")
    assert response.status_code == 200

    tree = html.fromstring(response.content)
    element = tree.xpath('//p[contains(text(), "Data from backend API")]')

    assert element
    assert "Data from backend API" in element[0].text_content()

if __name__ == '__main__':
    test_frontend_connection()
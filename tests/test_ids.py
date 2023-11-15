import pytest


@pytest.mark.parametrize('index', [
    5,
    45,
    654,
    1798,
    2567,
    5523,
    7698,
    13567,
    18643
])
def test_ids(index: int, client):
    response = client.get(f'/id/{index}')
    assert response.status_code == 200

import pytest


@pytest.mark.parametrize('rating', [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
])
def test_ratings(rating: int, client):
    response = client.get(f'/ratings/{rating}')
    assert response.status_code == 200

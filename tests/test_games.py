import pytest


@pytest.mark.parametrize('name, date, rating, genre', [
    ('spider', 2011, 6, 'action'),
    ('war', 2005, 8, 'adventure'),
    ('disney', 1996, 7, 'family'),
    ('world', 2000, 8, 'science_fiction')
])
def test_filter_games(name: str, date: int, rating: int, genre: str, client):
    response = client.get('/games/', params={'name': name, 'date': date, 'rating': rating, 'genre': genre})
    assert response.status_code == 200


@pytest.mark.parametrize('id', [
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
def test_et_single_game(id: int, client):
    response = client.get(f'/games/{id}')
    assert response.status_code == 200

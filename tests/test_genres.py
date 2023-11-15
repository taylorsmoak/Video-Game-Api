import pytest
from app import schemas


@pytest.mark.parametrize('genre', [
    'action',
    'adventure',
    'comedy',
    'crime',
    'family',
    'fantasy',
    'mystery',
    'science_fiction',
    'thriller'
])
def test_genres(genre: schemas.genres, client):
    response = client.get(f'/genres/{genre}')
    assert response.status_code == 200

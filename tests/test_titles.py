import pytest


@pytest.mark.parametrize('title', [
    'spider',
    'war',
    'fight',
    'shoot',
    'america',
    'world'
])
def test_titles(title: str, client):
    response = client.get(f'/titles/{title}')
    assert response.status_code == 200


@pytest.mark.parametrize('title', [
    'Spider-Man',
    'Call of Duty',
    'Fallout: New Vegas',
    'Banjo-Kazooie'
])
def test_exact_titles(title: str, client):
    response = client.get(f'/titles/exact/{title}')
    assert response.status_code == 200

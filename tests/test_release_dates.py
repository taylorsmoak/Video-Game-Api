import pytest


@pytest.mark.parametrize('date', [
    2000,
    2003,
    2007,
    2010,
    2014,
    2017,
    2019,
    2021,
    2023
])
def test_release_dates(date: int, client):
    response = client.get(f'/release-dates/{date}')
    assert response.status_code == 200

from flask import Response

from tests.test_client import flask_app
from pypi_org.views import home_views


def test_homepage(client):
    r: Response = client.get('/')
    assert r.status_code == 200
    assert b'Find, install and publish Python packages' in r.data


def test_homepage_directly():
    with flask_app.test_request_context(path='/'):
        r: Response = home_views.index()

    assert r.status_code == 200
    # noinspection PyUnresolvedReferences
    assert len(r.model.get('releases')) > 0

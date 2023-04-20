import pytest
from app.webapp import create_app


def test_instantiate_app():
    app = create_app()
    assert app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_not_found_resource(client):
    response = client.get("/non_existing_url")
    assert b"<title>404 Not Found</title>" in response.data

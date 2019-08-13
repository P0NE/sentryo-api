import pytest

from src.app import create_app

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
    })
    
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

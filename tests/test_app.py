import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def app(dash_duo):
    # import index.py from project root
    app = import_app("index")
    dash_duo.start_server(app)
    return dash_duo


def test_header_present(app):
    header = app.find_element("h1")
    assert header.text == "Soul Foods – Pink Morsel Sales Dashboard"


def test_visualisation_present(app):
    graph = app.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(app):
    radio = app.find_element("#region-filter")
    assert radio is not None

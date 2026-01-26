from dash.testing.application_runners import import_app

def test_header_is_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")

    assert header.text == "Pink Morsel Visualizer"
    assert header

def test_visualization_is_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    visualization = dash_duo.wait_for_element("#sales-line-chart", timeout=10)

    assert visualization

def test_region_picker_is_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    region_picker = dash_duo.wait_for_element("#region-picker", timeout=10)

    assert region_picker
from routes.routes import app
import json

def test_home_page():
    test_client = app.test_client()
    response = test_client.get('/')
    assert response.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(response.get_data(as_text=True))

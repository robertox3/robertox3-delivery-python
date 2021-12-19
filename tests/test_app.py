def test_app_is_creatade(app):
    assert app.name == 'delivery.app'

def test_config_is_loaded(config):
    assert config["DEBUG"] is False

def test_request_returns(client):
    assert client.get("/url_que_nao_existe").status_code == 404

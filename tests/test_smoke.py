def test_fastapi_app_is_configured():
    import web

    assert web.app.title == "GCLI2API"
    assert any(getattr(route, "path", None) == "/keepalive" for route in web.app.routes)

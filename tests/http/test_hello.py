async def test_hello_page(app, test_cli):
    """
    testing response (GET: /hello/world)
    """
    resp = await test_cli.get('/hello/world')
    assert resp.status == 200
    body = await resp.read()
    assert body == b'Hello, World!!'


async def test_hello_api(app, test_cli):
    """
    testing response (GET: /api/hello/world)
    """
    resp = await test_cli.get('/api/hello/world')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == {'hello': 'world'}

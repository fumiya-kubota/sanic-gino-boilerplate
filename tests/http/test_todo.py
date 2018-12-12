import pytest
import json


@pytest.mark.usefixtures('cleanup_db')
async def test_todo_api(app, test_cli):
    """
    testing todo api
    """
    resp = await test_cli.get('/api/v1/todo')
    assert resp.status == 200
    resp_json = await resp.json()
    assert len(resp_json['todo_list']) == 0

    resp = await test_cli.post(
        '/api/v1/todo',
        data=json.dumps({
            'name': 'new_todo',
        }),
        headers={'Content-Type': 'application/json'}
    )
    assert resp.status == 201

    resp = await test_cli.get('/api/v1/todo')
    assert resp.status == 200
    resp_json = await resp.json()
    assert len(resp_json['todo_list']) == 1
    assert resp_json['todo_list'][0]['name'] == 'new_todo'

    resp = await test_cli.delete(
        '/api/v1/todo/1',
    )
    assert resp.status == 200

    resp = await test_cli.get('/api/v1/todo')
    assert resp.status == 200
    resp_json = await resp.json()
    assert len(resp_json['todo_list']) == 0

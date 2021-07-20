import json
from fastapi.testclient import TestClient


def test_get_node_success(monkeypatch, test_app):
    node = {
        'node_id': 1,
        "value": 'test_value',
        'parent_id': 2,
        'is_deleted': False
    }
    test_app.tree_cache = {}

    async def first(query, params):
        return node

    with TestClient(test_app) as client:
        monkeypatch.setattr(test_app.db, 'first', first, raising=True)
        response = client.post(
            'v1/nodes/add',
            json=dict({
                'node_id': 1
            })
        )
        assert response.status_code == 200
        assert response.json() == {'success': True,
                                   'msg': f"node {node} has been added to cache",
                                   'tree': {
                                       '1': {'node_id': 1, 'value': 'test_value', 'parent_id': 2, 'is_deleted': False,
                                             'children': {},
                                             'level': 1}},
                                   'flat_tree': [
                                       {'node_id': 1, 'value': 'test_value', 'parent_id': 2, 'is_deleted': False,
                                        'level': 1}]}


def test_get_node_no_id(monkeypatch, test_app):
    async def first(query, params):
        return {}

    with TestClient(test_app) as client:
        monkeypatch.setattr(test_app.db, 'first', first, raising=True)
        response = client.post(
            'v1/nodes/add',
            json=dict({'node_id': 777})

        )
        assert response.status_code == 200
        assert response.json() == {'success': False, 'msg': 'Invalid node: 777',
                                   'tree': {'1': {'node_id': 1, 'value': 'test_value', 'parent_id': 2,
                                                  'is_deleted': False, 'children': {}, 'level': 1}},
                                   'flat_tree': [
                                       {'node_id': 1, 'value': 'test_value', 'parent_id': 2,
                                        'is_deleted': False, 'level': 1}
                                   ]
                                   }


def test_get_all_node_success(monkeypatch, test_app):
    async def select(query, params):
        return [{
            'node_id': 1,
            'parent_id': None,

        }, {
            'node_id': 2,
            'parent_id': 1,
        }, {
            'node_id': 3,
            'parent_id': 1
        }
        ]

    with TestClient(test_app) as client:
        monkeypatch.setattr(test_app.db, 'select', select, raising=True)
        response = client.get(
            'v1/nodes/',
        )
        assert response.status_code == 200
        assert response.json() == {'success': True, 'tree': {'1': {'node_id': 1, 'parent_id': None, 'children': {
            '2': {'node_id': 2, 'parent_id': 1, 'children': {}, 'level': 2},
            '3': {'node_id': 3, 'parent_id': 1, 'children': {}, 'level': 2}}, 'level': 1}},
                                   'flat_tree': [{'node_id': 1, 'parent_id': None, 'level': 1},
                                                 {'node_id': 2, 'parent_id': 1, 'level': 2},
                                                 {'node_id': 3, 'parent_id': 1, 'level': 2}]}

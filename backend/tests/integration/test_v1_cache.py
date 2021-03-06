from fastapi.testclient import TestClient


def test_get_cache(test_app):
    with TestClient(test_app) as client:
        test_app.tree_cache = {}
        response = client.get(
            'v1/cache/',
        )
        assert response.status_code == 200
        assert response.json() == {'success': True, 'msg': 'OK', 'flat_tree': []}

        test_app.tree_cache = {
            1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1, 'children': {}},
            6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'children': {}}}
        response = client.get(
            'v1/cache/',
        )
        assert response.status_code == 200
        assert response.json() == {'success': True, 'msg': 'OK', 'flat_tree': [
            {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1},
            {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'level': 1}]}


def test_remove_from_cache(test_app):
    with TestClient(test_app) as client:
        # delete from root
        test_app.tree_cache = {
            1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1, 'children': {}},
            6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'children': {}}}
        response = client.post(
            'v1/cache/remove',
            json=dict({'node_id': 1})
        )
        assert response.status_code == 200
        assert response.json() == {'success': True, 'msg': 'OK', 'flat_tree': [
            {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'level': 1}]}

        # delete from middle
        test_app.tree_cache = {1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1,
                                   'children': {
                                       2: {'node_id': 2, 'value': 'value_2', 'parent_id': 1, 'is_deleted': False,
                                           'children': {
                                               6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2,
                                                   'is_deleted': False,
                                                   'children': {}}}}}},
                               8: {'node_id': 8, 'value': 'value_2', 'parent_id': 5, 'is_deleted': False, 'children': {
                                   10: {'node_id': 10, 'value': 'value_2', 'parent_id': 8, 'is_deleted': False,
                                        'children': {}}}}}
        response = client.post(
            'v1/cache/remove',
            json=dict({'node_id': 2})
        )
        assert response.status_code == 200
        assert response.json() == {'success': True, 'msg': 'OK', 'flat_tree': [
            {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1},
            {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'level': 3},
            {'node_id': 8, 'value': 'value_2', 'parent_id': 5, 'is_deleted': False, 'level': 1},
            {'node_id': 10, 'value': 'value_2', 'parent_id': 8, 'is_deleted': False, 'level': 2}]}


def test_add_new_node(test_app):
    with TestClient(test_app) as client:
        test_app.temp_node_id_counter = 0
        test_app.tree_cache = {
            1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1, 'children': {}},
            6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'children': {}}}

        # add to existed node
        response = client.post(
            'v1/cache/add',
            json=dict({'parent_id': 1, })
        )
        assert response.status_code == 200
        assert response.json() == {'success': True, 'msg': 'OK', 'flat_tree': [
            {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1},
            {'node_id': -1, 'value': 'new_node', 'parent_id': 1, 'is_deleted': False, 'level': 2, 'is_new': True},
            {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'level': 1}]}

        # add new to new
        response = client.post(
            'v1/cache/add',
            json=dict({'parent_id': -1, })
        )
        assert response.status_code == 200
        assert response.json() == {'success': True, 'msg': 'OK', 'flat_tree': [
            {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1},
            {'node_id': -1, 'value': 'new_node', 'parent_id': 1, 'is_deleted': False, 'level': 2, 'is_new': True},
            {'node_id': -2, 'value': 'new_node', 'parent_id': -1, 'is_deleted': False, 'level': 3, 'is_new': True},
            {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'level': 1}]}

        # add to deleted node
        client.post(
            'v1/cache/del',
            json=dict({'node_id': 6})
        )
        response = client.post(
            'v1/cache/add',
            json=dict({'parent_id': 6, })
        )
        assert response.status_code == 200
        assert response.json() == {'success': False, 'msg': "Parent node is deleted, so new node can't be added",
                                   'flat_tree': [
                                       {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False,
                                        'level': 1},
                                       {'node_id': -1, 'value': 'new_node', 'parent_id': 1, 'is_deleted': False,
                                        'level': 2, 'is_new': True},
                                       {'node_id': -2, 'value': 'new_node', 'parent_id': -1, 'is_deleted': False,
                                        'level': 3, 'is_new': True},
                                       {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': True,
                                        'level': 1}]}


def test_del_node(test_app):
    with TestClient(test_app) as client:
        # just delete
        test_app.tree_cache = {
            1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1, 'children': {}},
            6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'children': {}}}

        response = client.post(
            'v1/cache/del',
            json=dict({'node_id': 6})
        )

        assert response.status_code == 200
        assert response.json() == {'success': True, 'msg': 'OK', 'flat_tree': [
            {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1},
            {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': True, 'level': 1}]}

        # delete newly created
        response = client.post(
            'v1/cache/add',
            json=dict({'parent_id': 1, })
        )

        response = client.post(
            'v1/cache/del',
            json=dict({'node_id': -4})
        )
        assert response.status_code == 200
        assert response.json() == {'success': False, 'msg': 'newly created element cannot be deleted', 'flat_tree': []}




def test_save_node(test_app):
    with TestClient(test_app) as client:
        test_app.tree_cache = {
            1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1, 'children': {}},
            6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'children': {}}}

        response = client.post(
            'v1/cache/save',
            json=dict({'node_id': 6, 'value': 'test test test'})
        )
        assert response.status_code == 200
        assert response.json() == {'success': True, 'msg': 'OK',
                                   'flat_tree': [
                                       {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False,
                                        'level': 1},
                                       {'node_id': 6, 'value': 'test test test', 'parent_id': 2, 'is_deleted': False,
                                        'level': 1,
                                        'is_edited': True}]}

from app.utils.nodes import put_node_to_cache
from .cache import cache_success_1, cache_success_2, cache_success_3, cache_success_4, cache_success_5


def test_success(test_app):
    test_app.tree_cache = {}

    # add to empty
    node = {"node_id": 1, "value": "value_1", "parent_id": None, "is_deleted": False, "level": 1}
    result, msg = put_node_to_cache(test_app, node)
    assert test_app.tree_cache == cache_success_1
    assert result
    assert msg == f'node {str(node)} has been added to cache'

    # add another to empty
    node = {"node_id": 6, "value": "value_6", "parent_id": 2, "is_deleted": False}
    result, msg = put_node_to_cache(test_app, node)
    assert test_app.tree_cache == cache_success_2
    assert result
    assert msg == f'node {str(node)} has been added to cache'

    # add child of one of and parent for another
    node = {"node_id": 2, "value": "value_2", "parent_id": 1, "is_deleted": False}
    result, msg = put_node_to_cache(test_app, node)
    assert test_app.tree_cache == cache_success_3
    assert result
    assert msg == f'node {str(node)} has been added to cache'

    # parent for empty
    node = {"node_id": 10, "value": "value_2", "parent_id": 8, "is_deleted": False}
    result, msg = put_node_to_cache(test_app, node)
    node = {"node_id": 8, "value": "value_2", "parent_id": 5, "is_deleted": False}
    result, msg = put_node_to_cache(test_app, node)
    assert test_app.tree_cache == cache_success_4
    assert result
    assert msg == f'node {str(node)} has been added to cache'

    # bind two branches with node
    node = {"node_id": 5, "value": "value_5", "parent_id": 2, "is_deleted": False}
    result, msg = put_node_to_cache(test_app, node)
    assert test_app.tree_cache == cache_success_5
    assert result
    assert msg == f'node {str(node)} has been added to cache'


def test_duplicate(test_app):
    test_app.tree_cache = {1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'children': {}}}
    # add to empty
    node = {"node_id": 1, "value": "value_1", "parent_id": None, "is_deleted": False}
    result, msg = put_node_to_cache(test_app, node)
    assert test_app.tree_cache == {1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'children': {}}}
    assert not result
    assert msg == f'node {str(node)} is already cached'

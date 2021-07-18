from app.utils.nodes import make_tree_flat
from .cache import cache_for_flat


def test_success(test_app):
    flattened_tree = make_tree_flat(cache_for_flat)
    assert flattened_tree == [{'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1},
                              {'node_id': 2, 'value': 'value_2', 'parent_id': 1, 'is_deleted': False, 'level': 2},
                              {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'level': 3},
                              {'node_id': 5, 'value': 'value_5', 'parent_id': 2, 'is_deleted': False, 'level': 3},
                              {'node_id': 8, 'value': 'value_2', 'parent_id': 5, 'is_deleted': False, 'level': 4},
                              {'node_id': 10, 'value': 'value_2', 'parent_id': 8, 'is_deleted': False, 'level': 5}]

from typing import List, Dict
from fastapi import FastAPI


def build_tree(nodes: List[Dict]) -> Dict:
    node_tree = {}

    def _check_duplicates(d, node):
        for k in d.keys():
            if k != node['node_id']:
                res = _check_duplicates(d[k]['children'], node)
                if res:
                    return True
            else:
                return True
        return False

    def _find_parent(d, node):
        for k in d.keys():
            if k == node['parent_id']:
                d[k]['children'][node['node_id']] = {**node, 'children': {}} if 'children' not in node else node
                return True
            else:
                res = _find_parent(d[k]['children'], node)
                if res:
                    return True
        return False

    def _find_children(d, node):
        keys = [k for k in d.keys()]
        for k in keys:
            if k in d and k != node['node_id']:
                if d[k]['parent_id'] != node['node_id']:
                    if d[k]['children']:
                        _find_children(d[k]['children'], node)
                    else:
                        continue
                else:
                    res = _find_parent(node_tree, d[k])
                    if res:
                        del d[k]
                        continue
        return False

    for node in nodes:
        is_added_as_child = _find_parent(node_tree, node)
        if not is_added_as_child:
            node_tree[node['node_id']] = {**node, 'children': {}}
        _find_children(node_tree, node)

    return node_tree


def put_node_to_cache(app: FastAPI, node: dict) -> (bool, str):

    def _check_duplicates(d, node):
        for k in d.keys():
            if k != node['node_id']:
                res = _check_duplicates(d[k]['children'], node)
                if res:
                    return True
            else:
                return True
        return False

    def _find_parent(d, node):
        for k in d.keys():
            if k == node['parent_id']:
                d[k]['children'][node['node_id']] = {**node, 'children': {}} if 'children' not in node else node
                if d[k]['is_deleted'] and d[k]['children']:
                    def _set_children_deleted(d2):
                        for k2 in d2:
                            d2[k2]['is_deleted'] = True
                            if d2[k2]['children']:
                                _set_children_deleted(d2[k2]['children'])
                        return
                    _set_children_deleted(d[k]['children'])
                return True
            else:
                res = _find_parent(d[k]['children'], node)
                if res:
                    return True
        return False

    def _find_children(d, node):
        keys = [k for k in d.keys()]
        for k in keys:
            if k in d and k != node['node_id']:
                if d[k]['parent_id'] != node['node_id']:
                    if d[k]['children']:
                        _find_children(d[k]['children'], node)
                    else:
                        continue
                else:
                    res = _find_parent(app.tree_cache, d[k])
                    if res:
                        del d[k]
                        continue
        return False

    if _check_duplicates(app.tree_cache, node):
        return False, f'node {str(node)} is already cached'

    is_added_as_child = _find_parent(app.tree_cache, node)
    if not is_added_as_child:
        app.tree_cache[node['node_id']] = {**node, 'children': {}}
    _find_children(app.tree_cache, node)
    return True, f'node {str(node)} has been added to cache'


def make_tree_flat(tree: Dict) -> List:
    flatted_data = []

    def _recursively_traverse_tree(d: Dict, level: int = 0):
        level = level + 1
        for k, v in d.items():
            v['level'] = level
            flatted_data.append({x: y for x, y in v.items() if x != 'children'})
            if v:
                _recursively_traverse_tree(v['children'], level)

    _recursively_traverse_tree(tree)
    return flatted_data



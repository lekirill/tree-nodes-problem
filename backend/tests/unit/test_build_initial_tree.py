from app.utils.nodes import build_tree
from .nodes import case_one_root, case_one_root_result, case_two_roots, case_two_roots_result


def test_success_one_root(monkeypatch, test_app):
    tree = build_tree(case_one_root)
    assert tree == case_one_root_result


def test_success_two_roots(monkeypatch, test_app):
    tree = build_tree(case_two_roots)
    assert tree == case_two_roots_result

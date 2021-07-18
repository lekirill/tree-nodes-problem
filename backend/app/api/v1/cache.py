from fastapi import APIRouter, Request

from app.schemas import cache_scheme
from app.utils.nodes import make_tree_flat, build_tree

router = APIRouter(
    prefix='/v1/cache'
)


@router.get("/", response_model=cache_scheme.CacheBase)
async def get_cache(request: Request):
    """
    Get current Cache
    :param request:
    :return:
    """
    response = cache_scheme.CacheBase()
    flat_tree = make_tree_flat(request.app.tree_cache)
    response.flat_tree = flat_tree
    return response


@router.post("/remove", response_model=cache_scheme.CacheBase)
async def remove_from_cache(request: Request):
    """
    Remove node from Cache
    :param request:
    :return:
    """
    response = cache_scheme.CacheBase()
    data = await request.json()
    node_id = data['node_id']
    ind_to_delete = None
    flat_tree = make_tree_flat(request.app.tree_cache)
    for ind, node in enumerate(flat_tree):
        if node['node_id'] == node_id:
            ind_to_delete = ind
            break
    if ind_to_delete is not None:
        flat_tree.pop(ind_to_delete)
    request.app.tree_cache = build_tree(flat_tree)
    response.flat_tree = flat_tree
    return response


@router.post("/add", response_model=cache_scheme.CacheBase)
async def add_new_node(request: Request):
    """
    Add new node to Cache
    :param request:
    :return:
    """
    response = cache_scheme.CacheBase()
    ind_to_insert = None
    flat_tree = make_tree_flat(request.app.tree_cache)
    temp_node_id = -1
    data = await request.json()
    parent_id = data['parent_id']
    for ind, node in enumerate(flat_tree):
        if node['node_id'] == temp_node_id:
            temp_node_id = temp_node_id - 1
        if node['node_id'] == parent_id:
            ind_to_insert = ind

    if ind_to_insert is not None:
        flat_tree.insert(ind_to_insert + 1,
                         {"node_id": temp_node_id,
                          "value": "new_node",
                          "parent_id": parent_id,
                          "is_deleted": False,
                          "level": flat_tree[ind_to_insert]['level'] + 1,
                          "is_new": True
                          }
                         )
    request.app.tree_cache = build_tree(flat_tree)
    response.flat_tree = flat_tree
    return response


@router.post("/del", response_model=cache_scheme.CacheBase)
async def del_node(request: Request):
    """
    Delete node
    :param request:
    :return:
    """
    response = cache_scheme.CacheBase()
    data = await request.json()
    node_id = data['node_id']
    flat_tree = make_tree_flat(request.app.tree_cache)
    for node in flat_tree:
        if node['node_id'] == node_id:
            node['is_deleted'] = True
            break
    request.app.tree_cache = build_tree(flat_tree)
    response.flat_tree = flat_tree
    return response


@router.post("/save", response_model=cache_scheme.CacheBase)
async def save_node(request: Request):
    """
    Save new node value
    :param request:
    :return:
    """
    response = cache_scheme.CacheBase()
    data = await request.json()
    node_id = data['node_id']
    value = data['value']
    flat_tree = make_tree_flat(request.app.tree_cache)
    for node in flat_tree:
        if node['node_id'] == node_id:
            node['value'] = value
            node['is_edited'] = True
            break
    request.app.tree_cache = build_tree(flat_tree)
    response.flat_tree = flat_tree
    return response

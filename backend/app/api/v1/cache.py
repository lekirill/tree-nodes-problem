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
async def remove_from_cache(request: Request, data: cache_scheme.CacheRemove):
    """
    Remove node from Cache
    :param request:
    :return:
    """
    response = cache_scheme.CacheBase()
    node_id = data.node_id
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
async def add_new_node(request: Request, data: cache_scheme.CacheAdd):
    """
    Add new node to Cache
    :param request:
    :return:
    """
    response = cache_scheme.CacheBase()
    ind_to_insert = None
    flat_tree = make_tree_flat(request.app.tree_cache)
    request.app.temp_node_id_counter -= 1
    temp_node_id = request.app.temp_node_id_counter
    parent_id = data.parent_id
    for ind, node in enumerate(flat_tree):
        if node['node_id'] == parent_id:
            if node['is_deleted']:
                response.success = False
                response.msg = "Parent node is deleted, so new node can't be added"
                response.flat_tree = flat_tree
                return response
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
async def del_node(request: Request, data: cache_scheme.CacheDel):
    """
    Delete node
    :param request:
    :return:
    """
    def _delete_nodes(d):
        for k in d:
            d[k]['is_deleted'] = True
            if d[k]['children']:
                _delete_nodes(d[k]['children'])

    def _delete_node_and_children(id, d):
        for k in d:
            if k == id:
                d[k]['is_deleted'] = True
                _delete_nodes(d[k]['children'])
                break
            else:
                _delete_node_and_children(id, d[k]['children'])

    response = cache_scheme.CacheBase()
    node_id = data.node_id
    if node_id < 0:  # means new
        response.success = False
        response.msg = 'newly created element cannot be deleted'
        response.flat_tree = []
        return response
    _delete_node_and_children(node_id, request.app.tree_cache)
    flat_tree = make_tree_flat(request.app.tree_cache)
    response.flat_tree = flat_tree
    return response


@router.post("/save", response_model=cache_scheme.CacheBase)
async def save_node(request: Request, data: cache_scheme.CacheSave):
    """
    Save new node value
    Save new node value
    :param request:
    :return:
    """
    response = cache_scheme.CacheBase()
    node_id = data.node_id
    value = data.value
    flat_tree = make_tree_flat(request.app.tree_cache)
    for node in flat_tree:
        if node['node_id'] == node_id:
            node['value'] = value
            node['is_edited'] = True
            break
    request.app.tree_cache = build_tree(flat_tree)
    response.flat_tree = flat_tree
    return response

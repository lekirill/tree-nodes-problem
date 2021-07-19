from fastapi import APIRouter, Request

from app.schemas import node_scheme
from app.utils.http_error_responses import node_id_absence
from app.utils.nodes import build_tree, put_node_to_cache, make_tree_flat
from app.crud import nodes_crud

router = APIRouter(
    prefix='/v1/nodes'
)


@router.post("/add",
            response_model=node_scheme.AddNode, )
async def add_node_to_cache(request: Request, data: node_scheme.AddToCache):
    """
    Adds new node from DB to Cache and return actual Cache
    :param request:
    :param node_id:
    :return:
    """
    response = node_scheme.AddNode()
    node_id = data.node_id
    node = await nodes_crud.get_node(request.app.db, node_id)
    if node and not node['is_deleted']:
        result, msg = put_node_to_cache(request.app, node)
        response.success = result
        response.msg = msg
        response.tree = request.app.tree_cache
        response.flat_tree = make_tree_flat(request.app.tree_cache)
        return response
    else:
        return node_id_absence(f'No actual node with id: {node_id}')


@router.post("/update",
             response_model=node_scheme.UpdateNodes)
async def update_nodes(request: Request):
    """
    Update DB from Cache
    :param request:
    :return:
    """
    response = node_scheme.UpdateNodes()
    nodes = request.app.tree_cache
    db = request.app.db
    flattened_tree = make_tree_flat(nodes)
    last_node_id = None
    request.app.tree_cache = {}
    for node in flattened_tree:
        if node['parent_id']:
            node['parent_id'] = last_node_id if node['parent_id'] < 0 else node['parent_id']
        if node.get('is_new', None):
            last_node_id = await nodes_crud.insert_node(db, node)
            node['node_id'] = last_node_id
            node['is_new'] = False
            node['is_edited'] = False
        elif node.get('is_deleted', None):
            await nodes_crud.delete_node(db, node)
        elif node.get('is_edited', None):
            await nodes_crud.update_node(db, node)
            node['is_edited'] = False
        put_node_to_cache(request.app, node)
    return response


@router.get("/",
            response_model=node_scheme.GetAllNodes)
async def get_all_nodes(request: Request):
    """
    Fetch all nodes from DB and compose to flatted tree
    :param request:
    :return:
    """
    response = node_scheme.GetAllNodes()
    all_nodes = await nodes_crud.get_all_nodes(request.app.db)
    response.tree = build_tree(all_nodes)
    response.flat_tree = make_tree_flat(response.tree)
    return response


@router.post("/reset",
               response_model=node_scheme.ResetNodes)
async def reset_nodes(request: Request):
    """
    Reset Cache and DB to initial state
    :param request:
    :return:
    """
    response = node_scheme.ResetNodes()
    await nodes_crud.reset(request.app.db)
    request.app.tree_cache = {}
    return response

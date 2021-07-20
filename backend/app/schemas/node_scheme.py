from pydantic import BaseModel
from typing import Optional, Dict, List


class NodeBase(BaseModel):
    node_id: Optional[int] = None
    value: Optional[str] = None
    parent_id: Optional[int] = None
    is_deleted: bool = False


class NodeBaseUpdate(BaseModel):
    node_id: Optional[int] = None
    value: Optional[str] = None
    parent_id: Optional[int] = None
    is_deleted: bool = False
    is_new: bool = False


class AddNodeResponse(BaseModel):
    success: bool = True
    msg: Optional[str] = None
    tree: Dict = {}
    flat_tree: List[Dict] = []


class GetAllNodesResponse(BaseModel):
    success: bool = True
    tree: Dict = {}
    flat_tree: List[Dict] = []


class UpdateNodesResponse(BaseModel):
    success: bool = True
    msg: str = 'All changes have been done'


class ResetNodesResponse(BaseModel):
    success: bool = True
    msg: str = 'database has been reset'


class AddToCache(BaseModel):
    node_id: int

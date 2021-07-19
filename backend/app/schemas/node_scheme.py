from pydantic import BaseModel
from typing import Optional, Dict, List


class NodeBase(BaseModel):
    node_id: Optional[int] = None
    value: Optional[str] = None
    parent_id: Optional[int] = None
    is_deleted: Optional[bool] = False


class NodeBaseUpdate(BaseModel):
    node_id: Optional[int] = None
    value: Optional[str] = None
    parent_id: Optional[int] = None
    is_deleted: Optional[bool] = False
    is_new: Optional[bool] = False


class AddNode(BaseModel):
    success: bool = True
    msg: Optional[str] = None
    tree: Optional[Dict] = None
    flat_tree: List[Dict] = []


class GetAllNodes(BaseModel):
    success: bool = True
    tree: Optional[Dict] = None
    flat_tree: List[Dict] = []


class UpdateNodes(BaseModel):
    success: bool = True
    msg: str = 'All changes have been done'


class ResetNodes(BaseModel):
    success: bool = True
    msg: str = 'database has been reset'


class AddToCache(BaseModel):
    node_id: int

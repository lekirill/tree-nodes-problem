from pydantic import BaseModel
from typing import List


class CacheBaseResponse(BaseModel):
    success: bool = True
    msg: str = 'OK'
    flat_tree: List = []


class CacheRemove(BaseModel):
    node_id: int


class CacheAdd(BaseModel):
    parent_id: int


class CacheDel(BaseModel):
    node_id: int


class CacheSave(BaseModel):
    node_id: int
    value: str

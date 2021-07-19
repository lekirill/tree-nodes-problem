from pydantic import BaseModel
from typing import List, Optional


class CacheBase(BaseModel):
    success: bool = True
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

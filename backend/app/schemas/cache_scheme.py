from pydantic import BaseModel
from typing import List


class CacheBase(BaseModel):
    success: bool = True
    flat_tree: List = []

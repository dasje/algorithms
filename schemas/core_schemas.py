from typing import TypeVar, List
from enum import Enum
from pydantic import BaseModel

T = TypeVar("T")

class ExecutionLineCountReturnType(BaseModel):
    sorted_list: list
    executed_lines_count: int

class XY(BaseModel):
    x_values: List[T]
    y_values: List[T]

class AlgoNames(str, Enum):
    insert_sort="insertion_sort"
    linear_search="linear_search"
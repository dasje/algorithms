from pydantic import BaseModel
from typing import List, TypeVar

T = TypeVar("T")

class LinearSearchDataType(BaseModel):
    input: List[T]
    output: T

linear_search_data: List[LinearSearchDataType] = [
    LinearSearchDataType(
        input=[3,5,2,3,1,6],
        output=6
    ),
]
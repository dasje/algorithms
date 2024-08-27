from pydantic import BaseModel
from typing import List
from schemas.core_schemas import T

class LinearSearchDataType(BaseModel):
    input: List[T]
    output: T

linear_search_data: List[LinearSearchDataType] = [
    LinearSearchDataType(
        input=[3,5,2,3,1,6],
        output=6
    ),
]
from pydantic import BaseModel
from typing import List

class InsertionSortDataType(BaseModel):
    input: List[int]
    output: List[int]

insertion_sort_data: List[InsertionSortDataType] = [
    InsertionSortDataType(
        input=[5,2,4,6,1,3],
        output=[1,2,3,4,5,6]
    ),
    InsertionSortDataType(
        input=[31,41,59,26,41,58],
        output=[26, 31, 41, 41, 58, 59]
    )
]
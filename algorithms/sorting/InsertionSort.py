from typing import Generator, List

def insertion_sort_gen(list_to_sort: List[int]) -> Generator[int, None, list]:
    # We start from 1st index (not zero) to ensure the list has a base case of one item.
    # If the list is length 1 or less, it is already sorted (trivially).
    yield 1
    if len(list_to_sort) <= 1:
        yield 1
        return list_to_sort
    # Iterating over range of indicies the length of input list ensures the termination case
    # of output the same length as input.
    for j in range(1, len(list_to_sort)): 
        current_item = list_to_sort[j]
        yield 2
        for idx in range(0, j):
            yield 1
            if current_item <= list_to_sort[idx]:
                list_to_sort = list_to_sort[:j] + list_to_sort[j + 1:]
                list_to_sort.insert(idx, current_item)
                yield 4
                break
    yield 1
    return list_to_sort

def insertion_sort(list_to_sort: List[int]) -> List[int]:
    # We start from 1st index (not zero) to ensure the list has a base case of one item.
    # If the list is length 1 or less, it is already sorted (trivially).
    if len(list_to_sort) <= 1:
        return list_to_sort
    # Iterating over range of indicies the length of input list ensures the termination case
    # of output the same length as input.
    for j in range(1, len(list_to_sort)): 
        current_item = list_to_sort[j]
        for idx in range(0, j):
            if current_item <= list_to_sort[idx]:
                list_to_sort = list_to_sort[:j] + list_to_sort[j + 1:]
                list_to_sort.insert(idx, current_item)
                break
    return list_to_sort

from typing import List, Generator, TypeVar

T = TypeVar("T")

def linear_search(list_to_search: List[T], value_to_find: T) -> Generator[int, None, int|None]:
    """An algorithm that searches an input array for a specific value.
    If it can't find the value it returns None.
    If it finds the value, it return the index.

    Args:
        list_to_search (List[T])
        value_to_find (T)

    Yields:
        Generator[int, None, int|None]
    """
    yield 1
    # Return if input array is empty. This ensures the search algorithm can be correctly initialized with a base case.
    if len(list_to_search) == 0:
        yield 1
        return None
    # Searching over indicies the length of the array, ensures there is a correct termination point in the algorithm.
    for i in range(len(list_to_search)):
        yield 1
        if list_to_search[i] == value_to_find:
            yield 2
            return i
    yield 1
    # This ensures a default failure case when the search yields no result.
    return None
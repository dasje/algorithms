from typing import Generator
from utils.GeneratorWrapper import GeneratorWrapper
from algorithms.sorting.InsertionSort import insertion_sort, insertion_sort_gen
from algorithms.search.LinearSearch import linear_search
from data.insertion_sort_data import insertion_sort_data
from data.linear_search_data import linear_search_data

class Algo:
    def count_execution_lines_from_gen(func: Generator, *func_args) -> tuple[list, int]:
        """
        This counts the number of lines executed in the running of a function.
        The function must be a generator that yields the number of lines executed throughout runtime.

        Args:
            func (Callable)

        Returns:
            tuple[list, int]
        """
        line_count = 0
        gen = GeneratorWrapper(func(*func_args))
        for n in gen:
            line_count += n  
        return gen.value, line_count
    

print(Algo.count_execution_lines_from_gen(insertion_sort_gen, insertion_sort_data[0].input))
print(Algo.count_execution_lines_from_gen(linear_search, linear_search_data[0].input, linear_search_data[0].output))
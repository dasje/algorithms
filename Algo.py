from typing import Generator, List, Dict, Callable
import matplotlib.pyplot as plt
import itertools

from utils.GeneratorWrapper import GeneratorWrapper
from algorithms.sorting.InsertionSort import insertion_sort, insertion_sort_gen
from algorithms.search.LinearSearch import linear_search
from data.insertion_sort_data import insertion_sort_data, insertion_sort_step_comparison_data
from data.linear_search_data import linear_search_data
from schemas.core_schemas import T, AlgoNames, ExecutionLineCountReturnType, XY



class Algo:
    __algo_ref: Dict[AlgoNames, Callable] = {
        AlgoNames.insert_sort: insertion_sort_gen,
        AlgoNames.linear_search: linear_search
    }

    def __init__(self, input_data: List[T]) -> None:
        self.input_data: List[T] = input_data
        self.data_permutations: List[List[T]]|None = None

    def execute(self, algo_type: AlgoNames, perms: bool, *fargs):
        """
        Execute an algorithm on the object's "input_data" and generate a graph with execution speed data.
        If "perms" is true, the algorithm will be executed on all permutations of the input data.

        Args:
            algo_type (AlgoNames)
            perms (bool)
        """
        self.get_input_data_permutations()
        speed_data = self.gen_execution_speed_data(self.__algo_ref[algo_type], perms)
        self.plot_executed_lines_against_input(speed_data.x_values, speed_data.y_values)


    def get_input_data_permutations(self) -> List[List[T]]:
        """
        Generate permutations for the input data, and save to object variable "data_permutations".

        Returns:
            List[List[T]]
        """
        self.data_permutations = [
            list(i) for i in list(
                itertools.permutations(self.input_data, len(self.input_data))
            )
        ]

    def plot_executed_lines_against_input(self, input_size: list, lines_executed: list):
        """
        Generate a graph mapping input size/data set number, against lines executed to run the algorithm.s

        Args:
            input_size (list): _description_
            lines_executed (list): _description_
        """
        plt.plot(input_size, lines_executed)
        plt.show()


    def count_execution_lines_from_gen(self, func: Generator, *func_args) -> ExecutionLineCountReturnType:
        """
        This counts the number of lines executed in the running of a function.
        The function must be a generator that yields the number of lines executed throughout runtime.

        Args:
            func (Generator)

        Returns:
            tuple[list, int]
        """
        line_count = 0
        gen = GeneratorWrapper(func(*func_args))
        for n in gen:
            line_count += n  
        return ExecutionLineCountReturnType(
            sorted_list=gen.value,
            executed_lines_count=line_count
        )
    
    def gen_execution_speed_data(self, algo_generator: Generator, perms: bool) -> XY:
        """
        Generate 2d plotting data from the input data. 
        If "perms" is true, it will generate plotting data on all permutations.

        Args:
            algo_generator (Generator)
            perms (bool)

        Returns:
            XY
        """
        x_input_number, y_exec_steps = [], []

        for p_input in range(len(self.input_data if not perms else self.data_permutations)):
            x_input_number.append(p_input)
            r: ExecutionLineCountReturnType = self.count_execution_lines_from_gen(algo_generator, self.input_data[p_input] if not perms else self.data_permutations[p_input])
            y_exec_steps.append(r.executed_lines_count)

        return XY(x_values=x_input_number, y_values=y_exec_steps)
    

Insertion = Algo(insertion_sort_step_comparison_data[0].input)
Insertion.execute(algo_type=AlgoNames.insert_sort, perms=True)
"""
Printing only even values from the list.
"""

from typing import List

def printing_only_even_values_from_list(list_of_integer: List[int]) -> None:
    if len(list_of_integer) == 0:
        return
    list_of_integer_id = 0
    printing_from_list_recursion(list_of_integer, list_of_integer_id)

def printing_from_list_recursion(list_of_integer: List[int],
                                 list_of_integer_id: int
                                ) -> None:
    if list_of_integer[list_of_integer_id] % 2 == 0:
        print(list_of_integer[list_of_integer_id])
    list_of_integer_id += 1
    if list_of_integer_id == len(list_of_integer):
        return
    printing_from_list_recursion(list_of_integer, list_of_integer_id)

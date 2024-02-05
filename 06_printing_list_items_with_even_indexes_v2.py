"""
Printing list items with even indexes v2.
"""

from typing import List, Any

def printing_list_items_with_even_indexes_v2(list_of_different: List[Any]) -> None:
    if len(list_of_different) == 0:
        return
    list_of_different_id = 0
    printing_list_items_recursion(list_of_different, list_of_different_id)

def printing_list_items_recursion(list_of_different: List[Any], 
                                  list_of_different_id: int
                                 ) -> None:
    print(list_of_different[list_of_different_id])
    list_of_different_id += 2
    if list_of_different_id >= len(list_of_different):
        return
    printing_list_items_recursion(list_of_different, list_of_different_id)

"""
Finding the second maximum number in the list (taking into account that there may be several maximum numbers if they are equal).
"""

from typing import List, Union

def find_second_maximum_number_in_list(list_of_integer: List[int]) -> Union[int, None]:
    if len(list_of_integer) < 2:
        return None
    list_of_integer_id = 1
    if list_of_integer[0] > list_of_integer[1]:
        return find_second_maximum_number_recursion(list_of_integer, 
                                                    list_of_integer_id,
                                                    list_of_integer[0],
                                                    list_of_integer[1]
                                                   )
    return find_second_maximum_number_recursion(list_of_integer, 
                                                list_of_integer_id,
                                                list_of_integer[1],
                                                list_of_integer[0]
                                               )

def find_second_maximum_number_recursion(list_of_integer: List[int], 
                                         list_of_integer_id: int,
                                         first_maximum_number: int,
                                         second_maximum_number: int
                                        ) -> Union[int, None]:
    if list_of_integer_id == len(list_of_integer) - 1:
        return second_maximum_number
    list_of_integer_id += 1
    if (    list_of_integer[list_of_integer_id] <= first_maximum_number
        and list_of_integer[list_of_integer_id] > second_maximum_number
       ):
        second_maximum_number = list_of_integer[list_of_integer_id]
    if list_of_integer[list_of_integer_id] > first_maximum_number:
        second_maximum_number = first_maximum_number
        first_maximum_number = list_of_integer[list_of_integer_id]
    return find_second_maximum_number_recursion(list_of_integer, 
                                                list_of_integer_id,
                                                first_maximum_number,
                                                second_maximum_number
                                               )

"""
Generating all correct balanced combinations of parentheses.
"""

from collections import namedtuple
from typing import List

def generating_combinations_of_parentheses(number_of_opening_parentheses: int) -> List[str]:
    result_list = []
    current_combination = ""
    left_parentheses_count = number_of_opening_parentheses
    right_parentheses_count = number_of_opening_parentheses
    return generating_combinations_recursion(left_parentheses_count,
                                             right_parentheses_count,
                                             current_combination,
                                             result_list
                                            )

def generating_combinations_recursion(left_parentheses_count: int, 
                                      right_parentheses_count: int,
                                      current_combination: str,
                                      result_list: List[str]
                                     ) -> List[str]:
    if (    left_parentheses_count == 0
        and right_parentheses_count == 0):
        result_list.append(current_combination)
        return result_list   
    stack = []
    Data_For_Next_Recursion = namedtuple('Data_For_Next_Recursion',
                                         ['left_parentheses_count_new',
                                          'right_parentheses_count_new',
                                          'combination_new'])
    if right_parentheses_count > left_parentheses_count:
        stack.append(Data_For_Next_Recursion
                     (left_parentheses_count,
                      right_parentheses_count - 1,
                      current_combination + ")"
                     )
                    )
    if left_parentheses_count > 0:
        stack.append(Data_For_Next_Recursion
                     (left_parentheses_count - 1,
                      right_parentheses_count,
                      current_combination + "("
                     )
                    )
    while len(stack) > 0:
        data_for_next_recursion = stack.pop()
        generating_combinations_recursion(data_for_next_recursion.left_parentheses_count_new,
                                          data_for_next_recursion.right_parentheses_count_new,
                                          data_for_next_recursion.combination_new,
                                          result_list
                                         )
    return result_list


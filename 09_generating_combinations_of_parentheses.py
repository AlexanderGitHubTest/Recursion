"""
Generating all correct balanced combinations of parentheses.
"""

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
    if left_parentheses_count > 0:
        generating_combinations_recursion(left_parentheses_count - 1,
                                          right_parentheses_count,
                                          current_combination + "(",
                                          result_list
                                         )
    if right_parentheses_count > left_parentheses_count:
        generating_combinations_recursion(left_parentheses_count,
                                          right_parentheses_count - 1,
                                          current_combination + ")",
                                          result_list
                                         )
    return result_list


"""
Calculating the length of the list v2.
"""

from typing import List, Any

def calculating_length_of_list_v2(original_list: List[Any]) -> int:
    if len(original_list) == 0:
        return 0
    _ = original_list.pop(0)
    return (1 + calculating_length_of_list_v2(original_list))

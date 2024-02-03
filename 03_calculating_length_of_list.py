"""
Calculating the length of the list.
"""

from typing import List, Any

def calculating_length_of_list(original_list: List[Any]) -> int:
    try:
        _ = original_list.pop(0)
        return (1 + calculating_length_of_list(original_list))
    except IndexError:
        return 0

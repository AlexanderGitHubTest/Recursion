"""
Is the string a palindrome v4.
"""

def is_string_palindrome_v4(string: str) -> bool:
    iteration_depth = 0
    return is_string_palindrome_recursion(string, iteration_depth)

def is_string_palindrome_recursion(string: str, iteration_depth: int) -> bool:
    if iteration_depth == len(string) // 2:
        return True
    iteration_depth += 1
    if string[iteration_depth - 1] != string[-iteration_depth]:
        return False
    return is_string_palindrome_recursion(string, iteration_depth)

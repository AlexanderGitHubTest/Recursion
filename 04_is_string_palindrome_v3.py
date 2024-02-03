"""
Is the string a palindrome v3.
"""

def is_string_palindrome_v3(string: str) -> bool:
    iteration_depth = 0
    return is_string_palindrome_recursion(string, iteration_depth)

def is_string_palindrome_recursion(string: str, iteration_depth: int) -> bool:
    if iteration_depth == len(string) // 2:
        return True
    iteration_depth += 1
    return (    string[iteration_depth - 1] == string[-iteration_depth]
            and is_string_palindrome_recursion(string, iteration_depth)
           )

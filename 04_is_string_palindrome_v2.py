"""
Is the string a palindrome v2.
"""

def is_string_palindrome_v2(string: str) -> bool:
    iteration_depth = 0
    def is_string_palindrome_recursion(string: str) -> bool:
        nonlocal iteration_depth
        if iteration_depth == len(string) // 2:
            return True
        iteration_depth += 1
        return (    string[iteration_depth - 1] == string[-iteration_depth]
                and is_string_palindrome_recursion(string)
               )
    return is_string_palindrome_recursion(string)

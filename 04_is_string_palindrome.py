"""
Is the string a palindrome.
"""

def remove_nonalphabetic_char_on_left(string: str) -> str:
    if not string[:1].isalpha() and len(string) > 0:
        return remove_nonalphabetic_char_on_left(string[1:])
    return string

def remove_nonalphabetic_char_on_right(string: str) -> str:
    if not string[-1:].isalpha() and len(string) > 0:
        return remove_nonalphabetic_char_on_right(string[:-1])
    return string

def is_string_palindrome(string: str) -> bool:
    string = remove_nonalphabetic_char_on_left(string)
    string = remove_nonalphabetic_char_on_right(string)
    if len(string) == 0 or len(string) == 1:
        return True
    return (    string[0].lower() == string[-1].lower()
            and is_string_palindrome(string[1:-1])
           )

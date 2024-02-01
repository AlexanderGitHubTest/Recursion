"""
Сalculating the sum of the digits of a number.
"""

def calculating_sum_of_digits_of_number(number: int) -> int:
    if number < 0:
        return calculating_sum_of_digits_of_number(-number)
    if number < 10:
        return number
    return (  number 
            - (number // 10) * 10 
            + calculating_sum_of_digits_of_number(number // 10)
           )

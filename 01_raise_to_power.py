"""
Raise to power.
"""

from typing import Union

def raise_to_power(base_of_power: Union[int, float] , index_of_power: int) -> Union[int, float]:
    if index_of_power == 0:
        return 1
    if index_of_power == 1:
        return base_of_power
    if index_of_power < 0 and base_of_power == 0:
        raise ZeroDivisionError("0.0 cannot be raised to a negative power")
    if index_of_power < 0:
        return (1 / raise_to_power(base_of_power, -index_of_power))
    if index_of_power % 2 == 0:
        return (  raise_to_power(base_of_power, index_of_power // 2) 
                * raise_to_power(base_of_power, index_of_power // 2)
               )
    return (  base_of_power 
            * raise_to_power(base_of_power, index_of_power - 1)
           )

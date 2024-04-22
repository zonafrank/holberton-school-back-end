#!/usr/bin/python3
from typing import Union, Tuple
"""Module for function to_kv"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments
        and returns a tuple.
    """
    return (k, float(v * v))

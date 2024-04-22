#!/usr/bin/python3
"""Module for element_length function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes as argument a list of sequence objects and returns
        a list of tuples where each tuple contains the sequence
        object as the first item and the length of the sequence
        object as the second item
    """
    return [(i, len(i)) for i in lst]

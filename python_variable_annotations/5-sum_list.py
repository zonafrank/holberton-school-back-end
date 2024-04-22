#!/usr/bin/python3
"""Module for the sum_list function"""
from typing import List


def sum_list(input_list: List[int]) -> float:
    """Returns the sum a list of integers
        input_list: [int]

        Returns: float
    """
    return float(sum(input_list))

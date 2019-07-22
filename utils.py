###################################################################################################
# Copyright (C) 2019 Maxim Integrated Products, Inc. All Rights Reserved.
#
# Maxim Integrated Products, Inc. Default Copyright Notice:
# https://www.maximintegrated.com/en/aboutus/legal/copyrights.html
#
# Written by RM
###################################################################################################
"""
Various small utility functions
"""


def ffs(x):
    """
    Returns the index, counting from 0, of the least significant set bit in `x`.
    """
    return (x & -x).bit_length() - 1


def fls(x):
    """
    Returns the index, counting from 0, of the most significant set bit in `x`.
    """
    return x.bit_length() - 1


def popcount(x):
    """
    Return the number of '1' bits in `x`.
    """
    return bin(x).count('1')


def argmin(values):
    """
    Given an iterable of `values` return the index of the smallest value.
    """
    def argmin_pairs(pairs):
        """
        Given an iterable of `pairs` return the key corresponding to the smallest value
        """
        return min(pairs, key=lambda x: x[1])[0]

    return argmin_pairs(enumerate(values))


def s2u(i):
    """
    Convert signed 8-bit integer `i` to unsigned.
    """
    if i < 0:
        i += 256
    return i


def u2s(i):
    """
    Convert unsigned 8-bit integer `i` to signed.
    """
    if i > 127:
        i -= 256
    return i
